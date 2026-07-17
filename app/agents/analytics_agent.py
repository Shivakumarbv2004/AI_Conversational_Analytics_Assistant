import json

import pandas as pd


class AnalyticsAgent:

    def process(self, data):

        result = data["result"]

        if isinstance(result, pd.DataFrame):

            result = result.to_dict(orient="records")

        elif isinstance(result, pd.Series):

            result = result.to_dict()

        return json.dumps(

            result,

            indent=4,

            default=str

        )