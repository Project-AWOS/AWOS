from app.ai.gemini import GeminiClient

client = GeminiClient()

response = client.generate(
    "Say hello from AWOS in one sentence."
)

print(response)