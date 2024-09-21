def chatbot():
    print("Hello! I'm a simple chatbot. Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I assist you today?")
        elif user_input in ["how are you?", "how are you", "what's up?"]:
            print("Chatbot: I'm just a program, but thanks for asking!")
        elif user_input in ["what is your name?", "who are you?"]:
            print("Chatbot: I'm a simple chatbot created to assist you.")
        elif user_input in ["help", "can you help me?"]:
            print("Chatbot: Sure! What do you need help with?")
        else:
            print("Chatbot: I'm sorry, I don't understand that.")


if __name__ == "__main__":
    chatbot()
