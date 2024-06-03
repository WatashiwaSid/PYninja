def chatbot():
    print("Hello! I'm Jarvis. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()
        
        if "hello" in user_input or "hi" in user_input:
            print("Jarvis: Hello! How can I assist you?")
        elif "how are you" in user_input:
            print("Jarvis: I'm just a bunch of code, but I'm here to help you!")
        elif "what is your name" in user_input:
            print("Jarvis: I am Jarvis. Siddhant created me in Iron Man 1.")
        elif "bye" in user_input or "exit" in user_input:
            print("Jarvis: Goodbye! Have a great day!")
            break
        else:
            print("Jarvis: I'm sorry, I don't understand that. Can you please rephrase?")

chatbot()