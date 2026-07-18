from app.prompts.system_prompt import SYSTEM_PROMPT
from app.services.llm_service import LLMService


class ResponseAgent:

    def generate(self, question: str, retrieval_data: dict):
        
        plan = retrieval_data.get("plan", {})
        result = retrieval_data.get("result")

        # 1. Handle Out of Domain Security
        if result == "OUT_OF_DOMAIN":
            return "I am a specialized Supermarket Analytics AI. I can only answer questions related to the Supermarket Sales dataset (e.g., Sales, Products, Customers, Branches, Payments). I cannot assist with that request."

        # 2. Determine formatting based on intent
        if plan.get("dashboard") is True:
            formatting_instruction = """
Generate a comprehensive business report.
Use the EXACT format below:

**Executive Summary**
[1 paragraph summary]

**Key Findings**
- [Bullet points]

**Recommendations**
- [Actionable bullet points]
"""
        else:
            formatting_instruction = """
Answer the user's question directly and concisely based strictly on the Analytics Result provided. 
Do not use the Executive Summary format. Keep it to 1-3 sentences. Do not hallucinate numbers.
"""

        prompt = f"""
Business Question:
{question}

Analytics Result (from exact dataset calculation):
{result}

{formatting_instruction}
"""

        return LLMService.ask(
            SYSTEM_PROMPT,
            prompt
        )