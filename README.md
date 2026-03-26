# 🚀 AgentOS: The Autonomous Product Operating Model

AgentOS is an open-source framework that maps the topology of a modern tech company into an executable Multi-Agent System. It defines 33 specialized AI roles across 7 verticals, replacing human bottlenecks with autonomous execution loops.

This is not a chatbot. This is a complete Product Operating Model (POM) designed to debate, take strategic decisions, execute code, and analyze data autonomously.

## 🎯 Core Philosophy: Anthropic Pattern 1

All agents and tools in this repository are strictly designed following the best practices for agentic workflows (specifically Claude's Pattern 1):

- **Flat Schemas**: Tools avoid deeply nested objects to prevent LLM hallucinations during function calling.
- **Strict Guardrails**: Hardcoded limits per agent to prevent domain overlapping (e.g., Design agents cannot execute Finance tools).
- **Mandatory Chain of Thought**: Every strategic agent is forced to use a `<thinking>` tag before invoking a tool or taking a capital-intensive decision.

## 🧠 The 33 Agents Ecosystem

The system is divided into 7 core verticals. Each vertical contains specialized agents with unique System Prompts and Tools.xml schemas:

- 👑 **Leadership**: CEO Agent (Strategy, OKRs, Capital Allocation).
- 📦 **Product & Discovery**: CPO, Discovery, Product Ops, Product Analytics, User Research.
- 🎨 **Design**: Lead UX/UI, Design System, UX Writer.
- ⚙️ **Engineering**: Tech Lead, Software Engineer, QA/SDET, DevOps/SRE, SecOps, Delivery Manager.
- 📊 **Data**: CDO, Data Engineer, Data Scientist, BI Analyst, Data Governance.
- 📈 **Growth & GTM**: Product Growth, User Acquisition, Lifecycle CRM, Community, PMM, B2B Sales.
- 💰 **Business & Ops**: Finance, Legal & Compliance, BizDev, Customer Success, Mass Support, HR.

## 🏗️ Architecture

AgentOS consists of two main layers:

- **The Knowledge Graph (Visual UI)**: A React/Tailwind application (included in this repo) that visualizes the company's topology, agent dependencies, and workflows.
- **The Orchestrator (Backend)**: The execution engine designed to be run via LangGraph, CrewAI, or Autoresearch frameworks. It manages the Global State (Decision Log, OKRs, Budget) and executes the actual Python tool functions.

## 🚀 Getting Started (Visual UI)

To run the interactive Knowledge Graph locally:

```bash
# Clone the repository
git clone https://github.com/your-username/agentos.git

# Navigate to the directory
cd agentos

# Install dependencies (requires Node.js)
npm install

# Run the development server
npm run dev
```

## 🛠️ Getting Started (Execution Engine - Python)

To run the execution loops (LangGraph) locally:

```bash
# Create Virtual Environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the local POC loop (CPO <-> Discovery)
python run_poc.py
```

### Vercel Deployment
The orchestration engine can be deployed out-of-the-box as a serverless endpoint on Vercel (`api/index.py`):
```bash
vercel
```

## 🤝 Contributing

We are building the future of the "Zero-Employee Unicorn". Contributions are welcome!
Whether it's adding a new tool schema for the Data Engineer Agent, refining the `<thinking>` prompt of the CPO Agent, or scaling the LangGraph execution loops, please submit a PR.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
