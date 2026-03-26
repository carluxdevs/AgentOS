📄 Product Requirements Document (PRD): AgentOS (POM Framework)

1. Meta Información

Producto: AgentOS (Product Operating Model Multi-Agent System)

Estado: Fase 1 Completada (Visual UI) / Fase 2 en Planificación (Orchestrator)

Document Owner: Chief Product Officer (CPO)

Target Release: Q3 2026

2. Resumen Ejecutivo (Product Vision)

AgentOS es un sistema operativo empresarial basado en Inteligencia Artificial. Mapea la topología de una empresa tecnológica moderna (7 verticales, 33 roles) y la sustituye/aumenta mediante Agentes de IA autónomos.

El objetivo no es crear un "chatbot", sino un bucle de ejecución autónoma donde agentes especializados (CEO, Tech Lead, Product Discovery, etc.) debaten, toman decisiones estratégicas usando "Chain of Thought", ejecutan código y analizan datos sin intervención humana constante.

3. Problema a Resolver (Problem Statement)

Las empresas tecnológicas sufren de cuellos de botella humanos al escalar:

Silos de información: Producto, Ingeniería y Ventas no comparten el mismo contexto.

Costes de coordinación: El 40% del tiempo se pierde en reuniones de alineamiento ("Deadlocks").

Lentitud de ejecución: Escribir código, testearlo y lanzarlo requiere sincronizar múltiples humanos con capacidades limitadas.

4. Usuarios Objetivo (Target Audience)

Startups y Founders: Que buscan escalar un producto digital con un equipo humano mínimo ("Zero-employee unicorn").

AI Engineers & DevOps: Que necesitan una arquitectura base sólida (prompts, tools y flujos) para conectar a orquestadores como LangGraph, CrewAI o Autogen.

Product Leaders: Que buscan estandarizar las operaciones de producto (Product Ops) automatizando el registro de decisiones y el análisis de datos.

5. Alcance del Producto (Scope & Phases)

✅ Fase 1: El Mapa de Conocimiento (Completada)

Interfaz Visual: Una aplicación React/Tailwind inspirada en Obsidian.

Grafo Interactivo: Visualización de la topología organizacional y las relaciones inter-departamentales (Nodos y Aristas).

Directorio de Agentes: Repositorio en Markdown de los 33 agentes, incluyendo su Role, Context, Guardrails y flujos de pensamiento (<thinking>).

🚀 Fase 2: El Motor de Ejecución (Next Milestone)

Orquestación Backend: Infraestructura en Python/Node.js para instanciar los agentes.

Tool Calling Real: Conectar los esquemas XML (ej. calculate_basal_cost) a funciones reales que consulten repositorios de GitHub, bases de datos o APIs financieras.

Shared State (Memoria Global): Implementar un objeto de estado (Decision Log, OKRs, Presupuesto) que todos los agentes puedan leer/escribir.

6. Requisitos Técnicos y Arquitectura (Non-Functional Requirements)

Estándar Anthropic (Pattern 1): Obligatorio el uso de Flat Schemas (esquemas planos sin anidación profunda) para todas las herramientas XML para evitar alucinaciones.

Chain of Thought: Todo agente con capacidad de alterar presupuesto, base de datos o código DEBE imprimir su razonamiento en una etiqueta <thinking> antes de ejecutar una acción.

Aislamiento de Dominio: Un agente de "Diseño" no puede ejecutar herramientas de "Finanzas". Los permisos están estrictamente mapeados por vertical.

7. Métricas de Éxito (Success Metrics / KPIs)

Task Completion Rate: Porcentaje de tareas complejas (ej. "Lanza una feature de referidos") completadas por los agentes sin intervención humana (Target: >70%).

Cycle Time: Tiempo medio desde que el CEO Agent aprueba una iniciativa hasta que el QA Agent aprueba el código (Target: < 2 horas).

Tool Error Rate: Tasa de alucinación en los parámetros de entrada de las funciones XML (Target: < 1%).