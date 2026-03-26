from fastapi import FastAPI
from pydantic import BaseModel
from agentos.workflows.discovery_loop import discovery_loop_app
from langchain_core.messages import HumanMessage
import os

app = FastAPI(title="AgentOS - Discovery API")

class WorkflowRequest(BaseModel):
    message: str

@app.post("/api/discovery")
async def run_discovery(req: WorkflowRequest):
    if not os.getenv("ANTHROPIC_API_KEY"):
        return {"error": "Missing ANTHROPIC_API_KEY environment variable. Asegúrate de configurarlo en Vercel."}
        
    initial_state = {
        "messages": [HumanMessage(content=req.message)],
        "okrs": {"Q3": "Priorizar retención sobre adquisición"},
        "budget": 50000.0,
        "decision_log": []
    }
    
    # Ejecutar el grafo de LangGraph
    try:
        result_state = discovery_loop_app.invoke(initial_state)
        last_message = result_state["messages"][-1].content
        
        return {
            "status": "success",
            "response": last_message
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/api/health")
def health_check():
    return {"status": "ok", "system": "AgentOS"}
