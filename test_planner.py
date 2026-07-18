import sys
from app.agents.planner_agent import PlannerAgent

agent = PlannerAgent()
question = "which industry has highest average MRR"
plan = agent.plan(question)
print("PLANNER OUTPUT:")
print(plan)
