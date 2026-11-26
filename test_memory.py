# Import the functions from memory.py.
# Import the memory functions.
from memory import add_user_message, add_ai_response, get_history, clear_history
from memory import set_history


# Clear previous conversation history.
clear_history()


# TURN 1
add_user_message("Patient", "What time does the clinic open?")
add_ai_response("AI", "We open at 8:00 AM.")


# TURN 2
add_user_message("Patient", "What about Saturdays?")
add_ai_response("AI", "We open from 8:00 AM to 8:00 PM.")


# TURN 3
add_user_message("Patient", "Which services do you offer?")
add_ai_response("AI", "We offer outpatient, laboratory, immunization and maternity services.")


# TURN 4
add_user_message("Patient", "Where are you located?")
add_ai_response("AI", "We are located in Kasarani, next to Naivas Supermarket.")


# Display the complete conversation history.
print("\nComplete Conversation History:\n")

for message in get_history():
    print(message["role"] + ": " + message["content"])


# Display the total number of stored messages.
print("\nTotal messages:", len(get_history()))


# Clear the conversation history.
clear_history()

# Display the history after clearing.
print("\nHistory after clearing:")
print(get_history())

# Display the number of remaining messages.
print("Messages remaining:", len(get_history()))

# Create a sample previously saved conversation.
old_history = [
    {"role": "user", "content": "Where are you located?"},
    {"role": "assistant", "content": "We are located in Kasarani."}
]

# Restore the previous conversation into memory.
set_history(old_history)

# Display the restored conversation.
print("\nRestored Memory:")

for message in get_history():
    print(message["role"] + ": " + message["content"])