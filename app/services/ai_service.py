import json
from groq import AsyncGroq
from app.core.config import settings
from app.core.logger import logger

client = AsyncGroq(api_key=settings.GROQ_API_KEY)


async def generate_attack_simulation(company_type: str, attack_type: str):

    try:

        prompt = f"""
        Simulate a realistic {attack_type} attack on a {company_type} company.

        Return ONLY raw valid JSON.

        Format:

        {{
          "summary": "short summary",
          "risk_level": "Low/Medium/High",
          "attack_chain": [
            "step 1",
            "step 2"
          ],
          "recommendations": [
            "recommendation 1"
          ]
        }}
        """
        logger.info("Generating AI attack simulation")

        response = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        logger.info("AI response generated successfully")

        content = response.choices[0].message.content

        content = content.replace("```json", "")
        content = content.replace("```", "")

        return json.loads(content)

    except Exception as e:
        logger.error(f"Error: {str(e)}")

        return {
            "error": str(e)
        }