# import necessary libraries
import random

# define some responses
greetings = ['hello', 'hi', 'hey', 'hola']
questions = ['how are you?', 'how are you doing?', 'what\'s up?']
responses = ['I\'m good.', 'I\'m doing well.', 'Not much.']
goodbyes = ['bye', 'goodbye', 'see you later', 'talk to you later']

# define a function to generate responses
def respond(message):
    if message in greetings:
        return random.choice(greetings)
    elif message in questions:
        return random.choice(responses)
    elif message in goodbyes:
        return random.choice(goodbyes)
    else:
        return "I didn't understand what you said."

# main loop
print("Hi, I'm a chatbot.")
while True:
    message = input().lower()
    if message == 'quit':
        break
    response = respond(message)
    print(response)
