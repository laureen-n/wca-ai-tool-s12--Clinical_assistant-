# Import modules for working with files and saved sessions.
import os
import glob

# Import libraries for connecting to Gemini.
from dotenv import load_dotenv
from google import genai

# Import clinic information and prompts.
from clinic_info import clinic_info
from prompts import SYSTEM_PROMPT, SUMMARY_PROMPT

# Import the function that gets and validates Gemini responses.
from retry import get_valid_response

# Import conversation memory functions.
from memory import get_history, clear_history

# Import session saving and loading functions.
from session import save_session, load_session

# Import the conversation summary function.
from summary import generate_summary

# Display the main menu and get the user's choice.
def display_menu():
    print("\n================================")
    print("      HEALTHCARE FAQ ASSISTANT")
    print("================================")

    print("\nWelcome to Healthcare Clinic!")
    print("\nPlease choose an option:")

    print("1. Start a new session")
    print("2. Continue from previous session")
    print("3. Exit")

    # Ask the user to enter their choice.
    choice = input("\nEnter your choice: ")

    # Return the selected option.
    return choice


# Save the conversation and generate its summary.
def finish_session(client):

    # Get the complete conversation history.
    history = get_history()

    # Check whether there are messages to save.
    if not history:
        print("No conversation to save.")
        return

    # Save the conversation and get its filename.
    filename = save_session(history)

    # Generate a summary of the conversation.
    try:
        summary = generate_summary(client, history)

        # Create a summary filename using the session filename.
        summary_filename = filename.replace(".json", "_summary.txt")

        # Save the summary into a text file.
        with open(summary_filename, "w", encoding="utf-8") as file:
            file.write(summary)

        print("\nConversation summary:")
        print(summary)
        print("\nSummary saved successfully!")

    except Exception as error:
        print("\nConversation was saved, but summary generation failed.")
        print("Error:", error)


# Start a new conversation.
def start_new_session(client):

    # Clear any previous conversation from memory.
    clear_history()

    # Welcome the patient.
    print("\nWelcome! You can now ask questions about our clinic.")

    # Continue accepting questions until the patient exits.
    while True:

        # Get a question from the patient.
        question = input("\nYou: ")

        # Allow the patient to end the conversation.
        if question.lower() == "exit":
            break

        # Get a response from Gemini and validate it.
        result = get_valid_response(client, question, clinic_info)

        # Display the assistant's answer.
        print("\nClinic Assistant:", result["answer"])

    # Save the conversation and generate its summary.
    finish_session(client)


# Continue a previously saved conversation.
def continue_previous_session(client):

    # Find all saved session files.
    session_files = glob.glob("session_*.json")

    # Check whether any saved conversations exist.
    if not session_files:
        print("\nNo previous sessions found.")
        return

    # Display the available saved conversations.
    print("\nAvailable Previous Sessions:")

    for index, filename in enumerate(session_files, start=1):
        print(f"{index}. {filename}")

    # Ask the user to select a conversation.
    choice = input("\nEnter the session number: ")

    # Check whether the selection is a valid number.
    if not choice.isdigit():
        print("Invalid selection. Please enter a number.")
        return

    # Convert the selection into an index.
    selected_index = int(choice) - 1

    # Check whether the selected number exists.
    if selected_index < 0 or selected_index >= len(session_files):
        print("Invalid session number.")
        return

    # Get the selected filename.
    filename = session_files[selected_index]

    # Load the selected conversation into memory.
    load_session(filename)

    # Allow the user to continue asking questions.
    print("\nYou can now continue your previous conversation.")

    while True:

        # Get the next question.
        question = input("\nYou: ")

        # End the conversation when the user types exit.
        if question.lower() == "exit":
            break

        # Get and validate Gemini's response.
        result = get_valid_response(client, question, clinic_info)

        # Display the assistant's answer.
        print("\nClinic Assistant:", result["answer"])

    # Save the updated conversation and generate its summary.
    finish_session(client)


# Run the main Clinic FAQ Assistant program.
def main():

    

    # Load environment variables from the .env file.
    load_dotenv()

    # Get the Gemini API key.
    api_key = os.getenv("GEMINI_API_KEY")

    # Check whether the API key was loaded.
    if not api_key:
        print("API key not found. Please check your .env file.")
        return

    # Initialize the Gemini client.
    client = genai.Client(api_key=api_key)

    print("\nGemini client initialized successfully!")

    # Keep displaying the menu until the user exits.
    while True:

        # Display the menu and get the user's choice.
        choice = display_menu()

        

        # Start a fresh conversation.
        if choice == "1":
            start_new_session(client)

        # Continue a previously saved conversation.
        elif choice == "2":
            continue_previous_session(client)

        # Exit the program.
        elif choice == "3":
            print("\nThank you for using Healthcare FAQ Assistant!")
            break

        # Handle invalid menu selections.
        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")    


# Run the main program when this file is executed directly.
if __name__ == "__main__":
    main()