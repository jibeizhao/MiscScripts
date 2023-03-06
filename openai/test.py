import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "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"

response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)

print(response)
