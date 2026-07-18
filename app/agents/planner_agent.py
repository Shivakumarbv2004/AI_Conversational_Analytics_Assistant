import json
from typing import Dict
from app.services.llm_service import LLMService

class PlannerAgent:
    """
    Determines how to query the Supermarket dataset dynamically using Pandas.
    Enforces strict domain restrictions.
    """

    def __init__(self):
        self.system_prompt = """
You are an advanced Data Architect for a Supermarket Sales dataset.
Your job is to read the user's natural language question and translate it into a structured JSON query plan.

DATASET SCHEMA:
- Invoice ID (string)
- Branch (string: A, B, C)
- City (string: Yangon, Naypyitaw, Mandalay)
- Customer type (string: Member, Normal)
- Gender (string: Female, Male)
- Product line (string: Health and beauty, Electronic accessories, Home and lifestyle, Sports and travel, Food and beverages, Fashion accessories)
- Unit price (float)
- Quantity (int)
- Tax 5% (float)
- Sales (float) - Total revenue including tax
- Date (string)
- Time (string)
- Payment (string: Ewallet, Cash, Credit card)
- cogs (float)
- gross margin percentage (float)
- gross income (float)
- Rating (float: 1 to 10)

CRITICAL RULE:
If the user asks ANY question that cannot be answered using ONLY the schema above (e.g., asking about politicians, general knowledge, or data not in the supermarket schema), you MUST respond exactly with:
{"error": "out_of_domain"}

JSON QUERY PLAN FORMAT (Respond ONLY with valid JSON):
{
  "filters": [
    {"column": "City", "operator": "==", "value": "Yangon"},
    {"column": "Product line", "operator": "==", "value": "Health and beauty"}
  ] or [],
  "group_by": ["list", "of", "columns"] or null,
  "agg_column": "target_column" or null (e.g. "Sales", "Quantity"),
  "agg_method": "method" or null (e.g. "sum", "mean", "count", "max")
}

If the user asks for a general dashboard or summary, return:
{"dashboard": true}

Return ONLY the raw JSON object, without markdown formatting or code blocks.
"""

    def plan(self, question: str) -> Dict:
        try:
            # Use LLM to generate the JSON query plan
            raw_response = LLMService.ask(self.system_prompt, question).strip()
            
            # Clean up potential markdown blocks if the LLM hallucinated them
            if raw_response.startswith("```json"):
                raw_response = raw_response[7:-3].strip()
            elif raw_response.startswith("```"):
                raw_response = raw_response[3:-3].strip()

            plan = json.loads(raw_response)
            plan["question"] = question
            return plan
            
        except Exception as e:
            # Fallback to dashboard in case of LLM failure or JSON parsing error
            return {
                "dashboard": True,
                "question": question,
                "error_details": str(e)
            }