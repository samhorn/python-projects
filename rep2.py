def ask(question):
    answer = input(question)
    answer = answer.strip().lower()
    return answer

def ask_color():
    return ask("What is your favorite color?")

def live():
    print("Correct, you may pass")

def die():
    print("Thou art cast into the Gorge of Eternal Peril.")
    print("You are dead.")



#####################################################


name = ask("what is your name")

quest = ask("what is your quest")

if name == 'lancelot':
    color = ask_color()
elif name == 'robin':
    capital = ask("What is the capital of Assyria?")
elif name == 'galahad':
    color = ask_color()
elif name == 'arthur':
    answer = ask("What is the air speed velocity of an unlaiden swallow")
else:
    color = ask_color()





