from app.agents.planner_agent import PlannerAgent
from app.agents.retrieval_agent import RetrievalAgent
from app.agents.analytics_agent import AnalyticsAgent
from app.agents.response_agent import ResponseAgent


class AnalyticsAssistant:

    def __init__(self):

        self.planner = PlannerAgent()

        self.retriever = RetrievalAgent()

        self.analytics = AnalyticsAgent()

        self.response = ResponseAgent()

    def ask(self, question):

        plan = self.planner.plan(question)

        retrieved_data = self.retriever.retrieve(plan)

        analytics_result = self.analytics.process(

            retrieved_data

        )

        answer = self.response.generate(

            question,

            analytics_result

        )

        return answer