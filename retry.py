import time
# Import the JSON validator function.
from validator import validate_answer

# Import the system prompt.
from prompts import SYSTEM_PROMPT

# Import functions for managing conversation memory.
from memory import add_user_message, add_ai_response, get_history



# Send a question and conversation history to Gemini.
def get_gemini_response(client, question, clinic_info):

    # Retrieve all previous messages.
    history = get_history()

    # Convert the conversation history into readable text.
    conversation = ""

    for message in history:
        conversation += message["role"] + ": "
        conversation += message["content"] + "\n"

    # Prepare the complete prompt for Gemini.
    full_prompt = (
        SYSTEM_PROMPT
        + "\nClinic information: "
        + str(clinic_info)
        + "\nPrevious conversation:\n"
        + conversation
        + "\nPatient's latest question: "
        + question
    )

    # Start measuring Gemini's response time.
    start_time = time.time()

    try:
        # Send the complete prompt to Gemini.
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=full_prompt
        )

        # Return Gemini's response as text.
        return response.text

    finally:
        print("Timing section reached!")

        # Calculate the time taken.
        end_time = time.time()

        # Display the request duration.
        print(f"Gemini request time: {end_time - start_time:.2f} seconds")



# Check Gemini's response and retry once if invalid.
def get_valid_response(client, question, clinic_info):

    # Get the first response from Gemini.
    response_text = get_gemini_response(client, question, clinic_info)

    # Validate the first response.
    validated_data = validate_answer(response_text)

    # If the first response is valid, save it.
    if validated_data is not None:

        # Store the patient's question.
        add_user_message("Patient", question)

        # Store the assistant's answer.
        add_ai_response("AI", validated_data["answer"])

        return validated_data

    # If invalid, try again once.
    print("Invalid response. Retrying...")

    # Get the second response from Gemini.
    response_text = get_gemini_response(client, question, clinic_info)

    # Validate the second response.
    validated_data = validate_answer(response_text)

    # If the second response is valid, save it.
    if validated_data is not None:

        # Store the patient's question.
        add_user_message("Patient", question)

        # Store the assistant's answer.
        add_ai_response("AI", validated_data["answer"])

        return validated_data

    # If both attempts fail, return an error message.
    return {
        "answer": "Sorry, I cannot process your question right now. Please try again later.",
        "category": "error",
        "found": False
    }

