# --- Define your functions below! ---


# --- Put your main program below! ---
def print_name():
    print("my name is KG")
    name = input("what's your name: ")
    print("hi " + name)
def main():
  print_name()
  while True:
      your_age()
      your_color()
      subject()
      print_number()
      free_time()
      print_preference()
      sock_color()
      hair_color()
      great = input("What is your favorite fruit?")
      fruit_good(great)
      cat_dog()
      good_bye()

      break

def subject():
    answer = input("what's your favorite subject?:")
    if answer.upper() == "SCIENCE":
        print("I like science too")
    elif answer.upper() == "MATH":
        print("That is cool, I'm in calculus")
        ans = input("what math are you taking? ")
        if ans.upper() == "PRECALCULUS" or ans.upper() == "AP CALCULUS":
            print("that is awesome!")
        else:
            print("Oh that's cool keep up the good work")
    elif answer.upper() == "ENGLISH" :
        print("I'm not good at english but that's cool")
    elif answer.upper() == "HISTORY":
        print("nice!, history is so interesting")
    else:
        print("I don't know what that is")
        answ = input("would you care to explain")
        print("oh cool")

def your_age():
    age = input("what is your age?: ")
    age = int(age)
    mine = 16
    if (mine > age):
        print("you're younger than me")
    elif (mine < age):
        print("You're older than me, cool")
    else:
        print("we have the same age yay")


def your_color():
    color = input("My favorite color is Yellow and yours?: ")
    print( color + "! that color is pretty")

def print_number():
    number = input("what is your favorite number?: ")
    if (number == 5):
        print("mine too")
    else:
        print( "mine is 5 " + "I like " + number +" too")

def print_preference():
    preference = input("Do you preffer to go to the mountains or the beach?: ")
    if preference.lower() == "beach":
        prefer = input("why do you like going to the beach?")
        print("I love going to the beach as well because I like building sand castles")
        print("I also like your reason")
    elif preference.lower()== "both":
        print("I can't choose too!")
    else:
        pre = input("why do you like mountains? ")
        print("I love going to the mountains as well because I like the wilderness")
        print("I also like your reason")

def free_time():
    time = input("what do you like doing on your free time?: ")
    print( "I like walking my dogs and spending time with my family")
    print("But I also like " + time)

def sock_color():
    color = input("what color are your socks?: ")
    if color.lower() == "black" or color.lower() == "white" or color.lower() == "gray" or color.lower() == "grey":
        print("your socks are average, boooo!!!!")
    elif color.lower() == "no socks" or color.lower() == "i'm not wearing socks" or color.lower() == "none":
        print("at least you're not average waering white, black, or gray socks")
    else:
        print("uh, that's cute! very colorful")


def hair_color():
    hair = input("what is your hair color?")
    if hair.lower()== "black":
        print("I like black hair")
    elif hair.lower()== "blonde":
        print("Uh, I like it, mine is Blonde too")
    elif hair.lower()== "brown":
        print("cool, My sister's hair is brown")
    else:
        print("that is very interesting, I like it alot")


def cat_dog():
    dog = input("do you like cats or dogs?: ")
    if dog.lower() == "cats":
        print("I like dogs better")
    elif dog.lower()== "dogs":
        print("yes!, they are so cuteeeeeeeeeeee")
    else:
        print("well that is sad")


def good_bye():
    bye= input("do you think you know me better?: ")
    if bye.lower()== "yes":
        print("me too, I very much like you! ")
    if bye.lower()== "no":
        print("well I don't care, I don't know you and I don't like you")

def fruit_good(great):
    if great.lower() == "watermelon":
        print("I love watermelon, they are juicy")
    else:
        print("I really like" + great + " too")




# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
