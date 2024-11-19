import re

responses = {
    "hello": "Hi there! How can I assist you today?",
    "how are you": "I'm doing well, thank you for asking!",
    "bye": "Goodbye! Have a great day!",
    "your name": "I am a simple rule-based chatbot.",
    "what is your purpose": "My purpose is to assist you with simple queries and help you with information!",
    "what can you do": "I can answer basic questions, give greetings, and provide help with predefined tasks.",
    "tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
    "how old are you": "I don't age, but I am constantly learning new things!",
    "what is the temperature in delhi": "It's 18 degrees out there, the day is getting colder.",
    "Akshat": "Hello Akshat! How are you?",
    "Good": "Sounds good! So what's on your mind?",
    "Bad": "Anything you would like to share?",
    "default": "Hello! How do you do? /n What is your name?"
}

def get_response(user_input):
    user_input = user_input.lower()  # Make input lowercase for better matching
    
    # Check for each predefined response
    for key in responses:
        if re.search(r'\b' + re.escape(key) + r'\b', user_input):
            return responses[key]
    
    return responses["default"]

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

chatbot()
