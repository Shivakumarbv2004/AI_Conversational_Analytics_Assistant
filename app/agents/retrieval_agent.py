from app.analytics.analytics_engine import AnalyticsEngine


class RetrievalAgent:

    def __init__(self):
        self.engine = AnalyticsEngine()

    def retrieve(self, plan: dict):
        result = self.engine.execute(plan)

        return {
            "plan": plan,
            "result": result
        }