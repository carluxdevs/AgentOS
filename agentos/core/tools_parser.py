import re
import xml.etree.ElementTree as ET
from typing import List, Dict, Any, Type
from pydantic import create_model, Field
from langchain_core.tools import StructuredTool

def extract_xml_tools_from_md(md_content: str) -> List[str]:
    """Extrae bloques XML de tool_description de un texto Markdown."""
    # Buscar todo lo que esté entre <tool_description> y </tool_description>
    pattern = r'(<tool_description>.*?</tool_description>)'
    matches = re.findall(pattern, md_content, re.DOTALL)
    return matches

def xml_to_langchain_tool(xml_string: str, func) -> StructuredTool:
    """
    Parsea un bloque <tool_description> y crea una StructuredTool de Langchain.
    Implementa el parseo de Flat Schemas (Pattern 1) para evitar alucinaciones.
    """
    root = ET.fromstring(xml_string)
    
    tool_name = root.findtext('tool_name')
    if not tool_name:
        raise ValueError("Missing tool_name in XML schema")
        
    description = root.findtext('description', default="").strip()
    
    # Parse input_schema
    input_schema = root.find('input_schema')
    fields: Dict[str, Any] = {}
    
    if input_schema is not None:
        for prop in input_schema.findall('property'):
            prop_name = prop.get('name')
            prop_type = prop.get('type')
            prop_desc = prop.get('description', '')
            
            # Mapeo simple de tipos
            python_type = str
            if prop_type == 'number':
                python_type = float
            elif prop_type == 'boolean':
                python_type = bool
                
            fields[prop_name] = (python_type, Field(description=prop_desc))
            
    # Crear modelo Pydantic dinámicamente para el schema de la tool
    args_schema = create_model(f"{tool_name}_schema", **fields)
    
    return StructuredTool.from_function(
        func=func,
        name=tool_name,
        description=description,
        args_schema=args_schema
    )
