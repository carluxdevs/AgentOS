import os
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import Runnable
from .tools_parser import extract_xml_tools_from_md, xml_to_langchain_tool

class BasePOMAgent:
    """
    Clase base para todos los agentes de AgentOS.
    Obliga a usar la etiqueta <thinking> y lee las tools desde XML.
    """
    
    def __init__(self, agent_id: str, md_file_path: str, tool_implementations: dict):
        self.agent_id = agent_id
        self.md_file_path = md_file_path
        self.tool_implementations = tool_implementations
        
        # Leer el contenido base del agente (prompts y tools XML)
        with open(self.md_file_path, 'r', encoding='utf-8') as f:
            self.raw_content = f.read()
            
        # Extraer System Prompt
        # El markdown completo sirve como system prompt pero podemos limpiarlo
        # Para forzar <thinking>:
        self.system_prompt = self.raw_content + """
        
# [MANDATORY DIRECTIVE: CHAIN OF THOUGHT]
You MUST always wrap your reasoning process in <thinking> tags before making ANY decision or calling ANY tool.
Failure to do so will result in a critical system fault.
        """
        
        # Extraer e instanciar las tools
        self.tools = []
        xml_blocks = extract_xml_tools_from_md(self.raw_content)
        for xml_str in xml_blocks:
            # Obtener el nombre directamente del XML con regex rápido o pasándolo
            import re
            name_match = re.search(r'<tool_name>(.*?)</tool_name>', xml_str)
            if name_match:
                tool_name = name_match.group(1).strip()
                if tool_name in self.tool_implementations:
                    func = self.tool_implementations[tool_name]
                    langchain_tool = xml_to_langchain_tool(xml_str, func)
                    self.tools.append(langchain_tool)
                    
        # Configurar el LLM
        # Para demostración, instanciamos el modelo Claude 3 Haiku o Sonnet
        self.llm = ChatAnthropic(
            model_name="claude-3-haiku-20240307", 
            temperature=0,
            max_tokens=4096
        )
        
        if self.tools:
            self.runnable = self.llm.bind_tools(self.tools)
        else:
            self.runnable = self.llm

    def create_node(self):
        """Devuelve una función invocable por el grafo de LangGraph."""
        prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            MessagesPlaceholder(variable_name="messages")
        ])
        
        chain = prompt | self.runnable
        
        def node_logic(state):
            response = chain.invoke({"messages": state["messages"]})
            return {"messages": [response]}
            
        return node_logic
