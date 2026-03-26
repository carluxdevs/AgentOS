import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from agentos.workflows.discovery_loop import discovery_loop_app

load_dotenv()

def print_message(message):
    print(f"\n====== [{message.type.upper()}] ======\n")
    if message.content:
        print(message.content)
    if hasattr(message, 'tool_calls') and message.tool_calls:
        print(f"\n[🔧 TOOL CALLS]: {message.tool_calls}")

def run():
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("⚠️  Warning: ANTHROPIC_API_KEY no detectado. Si Claude se requiere, la llamada fallará.")

    initial_state = {
        "messages": [
            HumanMessage(
                content="[CONTEXT INFO] OKRs vigentes: Priorizar retención sobre adquisición. Presupuesto disponible: $50000. \n\n"
                        "[MERCADO]: Un gran competidor (CompetitorX) acaba de bajar sus precios B2B un 20%. "
                        "Nuestros usuarios principales están pidiendo un ajuste o amenazan con churn. ¿Cuál es el plan estratégico?"
            )
        ],
        "okrs": {"Q3": "Priorizar retención sobre adquisición"},
        "budget": 50000.0,
        "decision_log": []
    }

    print("🚀 Iniciando Discovery Loop de AgentOS...\n")
    
    # stream_mode="values" devolverá el state actual cada vez que haga commit un nodo
    for event in discovery_loop_app.stream(initial_state, stream_mode="values"):
        message = event["messages"][-1]
        print_message(message)

    print("\n✅ --- EJECUCIÓN FINALIZADA ---")

if __name__ == "__main__":
    run()
