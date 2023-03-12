import random

R_EATING = "I don't like eating anything because I'm not a human like you!"
R_ADVICE = "If I were you, I would go to chat GPT and would've asked the same question!"
R_NAMING = "I would not like to be named but if your'e disappointed. I would prefer myself as a chatbot"


def unknown():
    response = ["Could you re-phrase that? ","I don't Know that",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
