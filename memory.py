#creates an empty list for saved conversations.
conversation_history =[]

#Adds new information or message and response to the list.
def add_user_message (user, content):
    message = {
        "role" : "user",
        "content":content 
    }
    conversation_history.append(message)

def add_ai_response ( assistant , content):
    response = {
        "role": "assistant" ,
        "content" : content
    }

    conversation_history.append(response)
#clears the current memory do as not to interfer with new session 
def clear_history():
    conversation_history.clear()


def get_history():

    return conversation_history


# Replace the current memory with a previously saved conversation.
def set_history(history):

    # Clear the existing conversation.
    conversation_history.clear()

    # Add all messages from the loaded conversation.
    conversation_history.extend(history)