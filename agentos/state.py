import operator
from typing import Annotated, TypedDict, Sequence, List, Dict, Any
from langchain_core.messages import BaseMessage

class GlobalState(TypedDict):
    """
    Estado global compartido para el Product Operating Model (POM).
    Actúa como la 'memoria' accesible para todos los agentes.
    """
    messages: Annotated[Sequence[BaseMessage], operator.add]
    okrs: Dict[str, Any]
    budget: float
    decision_log: Annotated[List[Dict[str, Any]], operator.add]
