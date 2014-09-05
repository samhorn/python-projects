import random
import time

answers = ['Yes', 'No', 'Maybe',]

print('Welcome to the magic 8 ball')


while True:
    print('What is your question?')
    question = input('> ')
    if question.startswith('what is love'):
        print('Baby don\'t hurt me.')
        time.sleep(2)
        print('no more')
    elif 'love' in question:
        print('Dayum shawty, you lookin\' fo love, come dis way')
        


    answer = random.choice(answers)
    print(answer)
