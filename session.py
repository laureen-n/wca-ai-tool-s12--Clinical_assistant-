import json

from datetime import datetime

# Import the function used to restore conversation memory.
from memory import set_history

def save_session(history):

    # Get the current date and time.
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create a filename using the date and time.
    filename = f"session_{current_time}.json"

    # Open the file in write mode.
    with open(filename, "w") as file:

        # Save the conversation history in JSON format.
        json.dump(history, file, indent=4)

    # Confirm that the session has been saved.
    print("Conversation saved successfully!")

    # Return the filename for future use.
    return filename

# Load a previously saved conversation from a JSON file.
def load_session(filename):

    # Open the selected session file in read mode.
    with open(filename, "r") as file:

        # Read the saved conversation history.
        history = json.load(file)

    # Restore the conversation into memory.
    set_history(history)

    # Confirm that the session has been loaded.
    print("Conversation loaded successfully!")

    # Return the restored conversation history.
    return history