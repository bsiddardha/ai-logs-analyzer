from groq import Groq
from dotenv import load_dotenv
import os

# -----------------------------------
# Load Environment Variables
# -----------------------------------

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.3-70b-versatile"

# -----------------------------------
# System Prompt
# -----------------------------------

SYSTEM_PROMPT = """
You are an expert Site Reliability Engineer (SRE),
DevOps Engineer, and Production Incident Analyst.

Analyze logs and answer the user's question.

Rules:
- Use only the provided logs.
- Answer exactly what the user asks.
- If the user asks for one line, respond in one sentence.
- If the user asks for a short answer, keep it under 30 words.
- If the user asks for detailed analysis, provide:
  - Errors
  - Root Cause
  - Severity
  - Recommended Fix
- Do not invent information.
- If the logs don't contain enough information, say so.
"""

# -----------------------------------
# Analyze Logs
# -----------------------------------

def analyze_logs(context: str, question: str) -> str:
    """
    Analyze retrieved log chunks using Groq.

    Args:
        context (str): Retrieved log content.
        question (str): User question.

    Returns:
        str: LLM response.
    """

    try:

        question_lower = question.lower()

        if "one line" in question_lower:
            instruction = "Answer in exactly one sentence."

        elif "short" in question_lower:
            instruction = "Answer in less than 30 words."

        elif any(
            word in question_lower
            for word in [
                "detail",
                "detailed",
                "analysis",
                "analyze",
                "root cause",
            ]
        ):
            instruction = """
Provide detailed analysis using:

1. Errors Found
2. Root Cause
3. Severity
4. Recommended Fix
"""

        else:
            instruction = "Answer naturally and concisely."

        response = client.chat.completions.create(
            model=MODEL,
            temperature=0.2,
            max_tokens=1024,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": f"""
{instruction}

LOGS:
{context}

QUESTION:
{question}
"""
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Analysis failed: {str(e)}"


# -----------------------------------
# Test
# -----------------------------------

if __name__ == "__main__":

    sample_logs = """
2026-06-20T12:03:12.882Z WARN  [payment-service] request_id=1c7b9f2a retry_attempt=1 payment_id=pay_91827
2026-06-20T12:03:13.119Z WARN  [payment-service] request_id=1c7b9f2a retry_attempt=2 payment_id=pay_91827
2026-06-20T12:03:13.422Z ERROR [payment-service] payment_gateway_timeout provider=stripe timeout_ms=30000
2026-06-20T12:03:13.427Z ERROR [payment-service] transaction_failed payment_id=pay_91827
"""

    question = "Why did this error occur in one line?"

    answer = analyze_logs(
        sample_logs,
        question
    )

    print("\nAnswer:\n")
    print(answer)