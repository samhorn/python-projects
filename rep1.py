print("hello world")

name = input("What is your name?").strip().title()
print("Hi there {}".format(name))

age_in_years = input("What is your age")
age_in_years = int(age_in_years)
print("Haha nerd, you're only {} years old".format(age_in_years))
print("ok, all joking aside, not that bad")

print(''' You awake dazed and confused. You have to go and try to redeem your
friend named Shawshank. It appears that he was taken away from you and dragged
into the wild.''')

action =input('''You see two doors. The Red Door says STOP, DON'T ENTER!!!
The Blue one says hello friend, if you would like to save your friend, come this way.''')

def welcome():
    print("Welcome")

#---------------------------------

def hello(name=''):
    print("hello {}".format(name))

#---------------------------------
def ask_name():
    name = input("What is your name? ").strip().title()
    
    return name


##################################

welcome()




