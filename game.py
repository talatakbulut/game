import random

def write_health(name, name2, health, health2):
    if health<0:
        health=0
    elif health2<0:
        health2=0
    print("%s                                                                                             %s" %(name, name2))    # Function writes heros' healths with number and bar.
    print("\n")
    print("HP[%d]=%s                                        HP[%d]=%s" %(health, int(health/2)*"|", health2, int(health2/2)*"|"))

def attack(health, health2, first, second):
    hit = 0

    while(hit<1 or hit>50):
        hit = float(input("Choose your hit damage between 1 and 50: ")) # Person chooses hit damage between 1 and 50.             
        if hit<1 or hit>50:
            print("You should choose your hit damage between 1 and 50.")
    chance = 100-hit

    if random.randint(1, 100) < chance:
        print("%s given %d damage." %(first, hit)) # With chance, it selects a number between 1 and 100 and changes hero's health.
        health2 = health2-hit 
        write_health(first, second, health, health2)
        return health2
            
    else:
        print("%s missed it." %(first)) # If misses, does nothing.
        return health2

def game(hero, hero2):

    characters = [hero, hero2]
    first = random.choice(characters) # Selects firts and second heros.
    if first == characters[0]:
        second = characters[1]

    else:
        second = characters[0]

    print("Result of heads or tails: %s's going to start first." %first)

    health= 100
    health2 = 100

    write_health(first, second, health, health2)

    while(True):
        print("%s's going to attack." %first)
    
        health2 = attack(health, health2, first, second)

        if health2<1:
            print("%s won." %(first)) # With a loop, it plays and controls until someone's health is zero.
            question()
            break

        print("%s's going to attack." %second) 
    
        health = attack(health2, health, second, first)

        if health<1:
            print("%s won." %(second))
            question()
            break

def question():
    reply = 0
    while reply != "YES" and reply != "yes" and reply != "NO" and reply!= "no": # It asks person for playing the game again.
            reply = input("Do you want to play again? (yes or no): ") 
            if reply == "yes" or reply == "YES":
                game(hero, hero2)
            elif reply == "no" or reply== "NO":
                print("Thank you for playing.")
                
print("First Character")
hero = input("Please enter your character's name: ").strip() # It assigns names to variables.
print("Second Character")
hero2 = input("Please enter your character's name: ").strip()

if hero == hero2:
    while(hero == hero2):
        print("It's already taken, please enter different name.") # It controls names and if it's same with other name, asks again.
        print("Second Character")
        hero2 = input("Please enter your character's name: ").strip()

game(hero, hero2)



            
            
            




