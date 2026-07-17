from app.prompts.system_prompt import SYSTEM_PROMPT
from app.services.llm_service import LLMService


class ResponseAgent:

    def generate(

        self,

        question,

        analytics_result

    ):

        prompt = f"""

Business Question

{question}

Analytics Result

{analytics_result}

Generate a business report.

Use the format

Executive Summary

Key Findings

Recommendations

"""

        return LLMService.ask(

            SYSTEM_PROMPT,

            prompt

        )