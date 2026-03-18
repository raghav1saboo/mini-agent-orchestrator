# Mini Agent Orchestrator
This project is a lightweight, event-driven agentic workflow built with Python and FastAPI. It demonstrates an order processing agent that can parse natural language requests, plan a sequence of actions, and execute them asynchronously using mock tools.

## Architectural Choices
# 1. State Handling and Guardrails
The system uses a custom Orchestrator to manage the execution state of the generated plan.
Sequential Execution: The Orchestrator processes tasks in the order provided by the Planner.
Error Propagation: A critical guardrail is implemented where the send_email tool is only executed if the cancel_order tool succeeds.
Failure Simulation: The cancel_order tool is designed with a random 20% failure rate to test the system's ability to handle and report a clear failure state to the user.

# 2. Asynchronous Tasks
To ensure high performance and non-blocking operations, the entire workflow is built on Python's asyncio.
Mock Tools: Both cancel_order and send_email are implemented as asynchronous functions.
Simulated Latency: The send_email tool includes an async sleep for 1 second to simulate a real-world network call without blocking the server.
FastAPI Integration: Using FastAPI allows the single API endpoint to handle multiple concurrent user requests efficiently.

# 3. LLM Planning and Unreliability
The Planner serves as the translation layer between natural language and actionable code.
Structured Output: To address the inherent unreliability of LLMs, the system prompts for a structured JSON list of tasks, which includes specific tool names and arguments.
Decoupled Logic: By separating the Planner from the Orchestrator, the core logic remains framework-agnostic. This project intentionally avoids heavy frameworks like LangChain to maintain direct control over the agentic logic.
Mock Fallback: A local mock planner using regex is provided as an alternative to the OpenAI API, ensuring the system remains functional even without external API access.

# Tech Stack
Language: Python8
Framework: FastAPI1
LLM: OpenAI API (with local mock fallback)

# Project Structure
main.py: Entry point containing the FastAPI application and the single /process-request endpoint.1
planner.py: Responsible for converting natural language into a task list (the Plan).4
orchestrator.py: Executes the plan and manages tool dependencies and guardrails.9
tools.py: Contains the mock asynchronous functions for cancel_order and send_email.5
How to Run
Install dependencies: pip install fastapi uvicorn openai
Start the server: uvicorn main:app --reload
Navigate to /docs in your browser to use the interactive API documentation to send a POST request.
