from app.agents.orchestrator import AnalyticsAssistant

assistant = AnalyticsAssistant()

questions = [
    "What are the total sales?",
    "Show top products",
    "Compare branch sales",
    "Show payment distribution",
    "Give me dashboard summary"
]

for q in questions:
    print("=" * 80)
    print("Question:", q)
    print()
    print(assistant.ask(q))
    print()