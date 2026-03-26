import operator
from typing import Annotated, TypedDict, Sequence, Literal
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode

from agentos.state import GlobalState
from agentos.agents.cpo_agent import CPOAgent
from agentos.agents.discovery_agent import DiscoveryAgent

cpo_agent = CPOAgent()
discovery_agent = DiscoveryAgent()

# Nodos de herramientas basados en las herramientas extraídas por BasePOMAgent
discovery_tools_node = ToolNode(discovery_agent.tools)
cpo_tools_node = ToolNode(cpo_agent.tools) if cpo_agent.tools else None

def cpo_router(state: GlobalState) -> Literal["cpo_tools_node", "discovery_node", "__end__"]:
    last_msg = state["messages"][-1]
    
    # Manejo de múltiples casos: llamada a tools
    if hasattr(last_msg, 'tool_calls') and last_msg.tool_calls:
        return "cpo_tools_node" if cpo_tools_node else "__end__"
    
    # Si desea delegar
    content = str(last_msg.content)
    if "<delegate_to>discovery_agent</delegate_to>" in content:
        return "discovery_node"
        
    # Si no, asumimos que tomó la decisión final
    return "__end__"

def discovery_router(state: GlobalState) -> Literal["discovery_tools_node", "cpo_node"]:
    last_msg = state["messages"][-1]
    if hasattr(last_msg, 'tool_calls') and last_msg.tool_calls:
        return "discovery_tools_node"
    # Una vez acabada su respuesta asíncrona, vuelve al CPO
    return "cpo_node"


# Construcción del grafo
graph_builder = StateGraph(GlobalState)

graph_builder.add_node("cpo_node", cpo_agent.create_node())
graph_builder.add_node("discovery_node", discovery_agent.create_node())
graph_builder.add_node("discovery_tools_node", discovery_tools_node)
if cpo_tools_node:
    graph_builder.add_node("cpo_tools_node", cpo_tools_node)

graph_builder.add_edge(START, "cpo_node")

graph_builder.add_conditional_edges("cpo_node", cpo_router)
graph_builder.add_conditional_edges("discovery_node", discovery_router)

graph_builder.add_edge("discovery_tools_node", "discovery_node")
if cpo_tools_node:
    graph_builder.add_edge("cpo_tools_node", "cpo_node")

# Compilar un motor de transiciones (workflow)
discovery_loop_app = graph_builder.compile()
