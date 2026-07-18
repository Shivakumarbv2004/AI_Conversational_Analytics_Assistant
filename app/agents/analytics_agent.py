import json
import pandas as pd

class AnalyticsAgent:
    """
    Serializes Pandas data structures into JSON for the LLM.
    """
    def process(self, data: dict):
        
        result = data.get("result")
        
        # Prevent serialization errors for OUT_OF_DOMAIN or simple strings
        if isinstance(result, str):
            pass 
        elif isinstance(result, pd.DataFrame):
            result = result.to_dict(orient="records")
            result = json.dumps(result, indent=4, default=str)
        elif isinstance(result, pd.Series):
            result = result.to_dict()
            result = json.dumps(result, indent=4, default=str)
        else:
            try:
                result = json.dumps(result, indent=4, default=str)
            except:
                result = str(result)
        
        # Put serialized result back into the dictionary
        data["result"] = result
        return data