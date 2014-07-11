print("welcome")

name = input("What is your name?").strip().title() 
print("Well hello there " + name)

other_name = input ("What is the other persons name?").strip().title()

print("Please tell {} hello for me.".format(other_name))

first_age = input("what is your age{}?".format(name)).strip()
other_age = input("And what is your age {}?".format(other_name)).strip()

first_age = int(first_age)
other_age = int(other_age) 

years_apart = first_age - other_age
years_apart = abs(years_apart) 

print("You are {} years apart.".format(years_apart)) 
