# Import the conversation memory functions.
from memory import (
    add_user_message,
    add_ai_response,
    get_history,
    clear_history
)

# Import the session functions.
from session import save_session, load_session


# Start with an empty conversation.
clear_history()

# Add a sample patient question.
add_user_message("Patient", "What services do you offer?")

# Add a sample assistant response.
add_ai_response(
    "AI",
    "We offer outpatient, laboratory, immunization and maternity services."
)

# Save the conversation.
filename = save_session(get_history())


# Clear memory to simulate starting a fresh session.
clear_history()

print("\nMemory after clearing:")
print(get_history())


# Load the previously saved conversation.
load_session(filename)


# Display the restored memory.
print("\nMemory after loading:")

for message in get_history():
    print(message["role"] + ": " + message["content"])