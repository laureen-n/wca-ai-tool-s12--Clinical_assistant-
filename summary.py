# Import Gemini's client library.
from google import genai

# Import the summary instructions.
from prompts import SUMMARY_PROMPT


# Generate a summary of the conversation.
def generate_summary(client, history):

    # Convert the conversation history into readable text.
    conversation = ""

    for message in history:
        conversation += message["role"] + ": "
        conversation += message["content"] + "\n"

    # Combine the summary instructions with the conversation.
    full_prompt = (
        SUMMARY_PROMPT
        + "\n\nConversation:\n"
        + conversation
    )

    # Ask Gemini to generate the conversation summary.
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=full_prompt
    )

    # Return the generated summary.
    return response.text