
# Import Python's JSON library.
import json


# Validate whether Gemini's response has the correct JSON fields.
def validate_answer(response_text):

    try:
        # Change JSON text into a Python dictionary.
        data = json.loads(response_text)

        # Define the required fields.
        required_fields = ["answer", "category", "found"]

        # Check if any required field is missing.
        for field in required_fields:
            if field not in data:
                return None

        # Check whether answer is a string.
        if not isinstance(data["answer"], str):
            return None

        # Check whether category is a string.
        if not isinstance(data["category"], str):
            return None

        # Check whether found is a Boolean.
        if not isinstance(data["found"], bool):
            return None

        # Check that answer is not empty.
        if not data["answer"].strip():
            return None

        # Check that category is not empty.
        if not data["category"].strip():
            return None

        # Return the response if all checks pass.
        return data

    except (json.JSONDecodeError, TypeError):
        # Return None if the response is invalid JSON.
        return None

