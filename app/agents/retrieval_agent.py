from app.analytics.analytics_engine import AnalyticsEngine


class RetrievalAgent:

    def __init__(self):

        self.engine = AnalyticsEngine()

    def retrieve(self, plan):

        tool = plan["tool"]

        result = self.engine.execute(tool)

        return {

            "tool": tool,

            "result": result

        }