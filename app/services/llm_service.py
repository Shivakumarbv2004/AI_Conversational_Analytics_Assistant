from groq import Groq

from app.config import GROQ_API_KEY
from app.config import MODEL

client = Groq(api_key=GROQ_API_KEY)


class LLMService:

    @staticmethod
    def ask(system_prompt, user_prompt):

        response = client.chat.completions.create(

            model=MODEL,

            messages=[

                {
                    "role": "system",
                    "content": system_prompt
                },

                {
                    "role": "user",
                    "content": user_prompt
                }

            ],

            temperature=0.2

        )

        return response.choices[0].message.content