from typing import Dict
from app.services.llm_service import LLMService

class PlannerAgent:
    """
    Determines which analytics tool should be executed
    based on the user's natural language question using an LLM.
    """

    def __init__(self):
        self.available_tools = [
            "total_sales", "average_sale", "transactions", "quantity",
            "top_products", "least_products", "sales_by_product", "quantity_by_product",
            "customer_distribution", "gender_distribution", "sales_by_gender", "member_vs_normal",
            "payment_distribution", "sales_by_payment",
            "sales_by_branch", "sales_by_city",
            "monthly_trend", "weekday_trend", "hourly_trend",
            "dashboard"
        ]
        
        self.system_prompt = f"""
You are an intelligent intent classifier for a Supermarket Sales Analytics System.
Your job is to read the user's question and determine the single most appropriate tool to run.
The user wants to analyze a dataset containing Sales, Products, Branches, Cities, Customer Types, Gender, Payments, and Trends.

Available tools:
{", ".join(self.available_tools)}

Rules:
1. ONLY reply with the exact name of the tool from the list above. Do not include any other text, punctuation, or explanation.
2. If the user asks for a general summary, overview, or you are unsure, reply with "dashboard".
3. Map logical intents (e.g., "how are people paying?" -> "payment_distribution", "who buys more men or women?" -> "sales_by_gender").
"""

    def plan(self, question: str) -> Dict:
        try:
            # Use LLM to classify intent
            tool = LLMService.ask(self.system_prompt, question).strip().lower()
            
            # Validate output, fallback to dashboard if LLM hallucinates
            if tool not in self.available_tools:
                tool = "dashboard"
                
        except Exception as e:
            # Fallback to dashboard in case of LLM failure
            tool = "dashboard"

        return {
            "tool": tool,
            "question": question
        }