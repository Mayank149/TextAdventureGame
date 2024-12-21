import time

print("Welcome to Crystal Diary!")
time.sleep(2)
print("This is a Text-based Adventure Game\nMade by Mayank Bansal")
time.sleep(2)
print("Adventurer, are you ready to dive in and have fun?")
time.sleep(2)
gamestate = "title"
substate = "start"

class Player:
    def __init__(self, name="Unknown", age="18", health=100, smell="good", liked="yes"):
        self.name = name
        self.age = age
        self.health = health
        self.smell = smell
        self.liked = liked
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} has no health left!")
            gameover()
        else:
            print(f"{self.name}'s health is now {self.health}.")

player = Player()

def gameover():
    time.sleep(2)
    print("Game Over")
    print("Rebooting World!")
    time.sleep(5)
    global gamestate, substate
    gamestate = "title"
    substate = "start"

while gamestate == "title":
    choice = input("Y/N: ").lower()
    if choice == "y":
        print("Very well then, Let's Start!")
        gamestate = "character_building"
    elif choice == "n":
        print("Too bad...... You have to play anyways!")
        player.name = "Monkey"
        player.age = "10"
        player.smell = "bad"
        player.liked = "no"
        gamestate = "playing"
    else:
        print("Enter a valid input!")

while gamestate == "character_building":
    player.name = input("Enter your name adventurer!\n")
    player.smell = "good"
    player.liked = "yes"
    gamestate = "playing"

while gamestate == "playing":

    while substate == "start":
        print("Loading.....")
        time.sleep(2)
        print("Wait... Where am I?")
        time.sleep(2)
        choice = input("What do I want to do?\n1.Look around\n2.Wait\n3.Make noise\n4.Go back to sleep\n")
        if choice == "1":
            print("You notice a swarm of vicious monkeys outside!")
            time.sleep(2)
            print("Looking around was the smart choice.")
            time.sleep(2)
            print("You found your passport with your details.")
            time.sleep(2)
            print("Your Name is:", player.name)
            print("You are", player.age, "years old.")
            substate = "stage1"
        elif choice == "2":
            print("You waited only to die from hunger!")
            gameover()
        elif choice == "3":
            print("*You start jumping up and down like a monkey!*")
            time.sleep(2)
            choice = input("A monkey approaches! What will you do?\n1.Befriend\n2.Run Away\n")
            if choice == "1":
                print("The monkey ate you...sadly, it wasn't a good friend choice.")
                gameover()
            elif choice == "2":
                print("You ran into a swarm of monkeys and were left half-eaten.")
                gameover()
            else:
                print("Invalid choice. The monkey ate you!")
                gameover()
        elif choice == "4":
            print("Why go back to sleep in such danger? Game Over!")
            gameover()
        else:
            print("Invalid choice, try entering a number!")

    while substate == "stage1":
        print("A strange buzzing noise catches your attention.")
        choice = input("What do you want to do?\n1.Check it out\n2.Ignore it\n3.Hide\n")
        if choice == "1":
            print("fmzzz.....bzzzzz")
            time.sleep(2)
            print("fmzzz.....bzzzzz...click")
            time.sleep(2)
            print("hmmmzzz.....mmmz")
            time.sleep(2)
            print("You approach a strange noise, but a monkey catches your scent!")
            time.sleep(2)
            print("The monkeys catch you off gaurd and rip you apart!")
            player.take_damage(40)
            if player.health>0:
                substate = "waterfall"
            
        elif choice == "2":
            print("Ignoring the noise was a mistake! The monkeys smelled you and attacked.")
            player.take_damage(50)
            if player.health > 0:
                substate = "waterfall"
        elif choice == "3":
            if player.smell == "bad":
                print("Your smell gave you away! The monkeys found you!")
                player.take_damage(20)
                if player.health>0:
                    substate = "waterfall"
            else:
                print("You successfully hid from the monkeys!")
                if player.health > 0:
                    substate = "waterfall"

    while substate == "waterfall":
        print("You stumble upon a beautiful waterfall.")
        choice = input("Do you want to wash off the smell?\n1.Yes\n2.No\n")
        if choice == "1":
            print("You start bathing, but notice crocodiles in the water!")
            choice = input("Do you:\n1. Swim faster\n2. Try to distract them\n")
            if choice == "1":
                player.take_damage(20)
                print("You escaped but were slightly injured.")
            elif choice == "2":
                print("You distracted the crocodiles successfully.")
            else:
                print("Invalid choice, you got caught by a crocodile!")
                gameover()
            player.smell = "good"
            print("You smell better, but the monkeys stole your clothes!")
            substate = "tribal"
        elif choice == "2":
            print("You remain smelly and attract monkeys along your journey!")
            player.take_damage(10)
            if player.health > 0:
                substate = "tribal"

    while substate == "tribal":
        print("You enter a tribal village.")
        if player.smell == "bad":
            print("The tribespeople notice your foul smell and get angry!")
            player.take_damage(20)
            if player.liked == "no":
                print("They disliked you even more due to your behavior!")
                player.take_damage(10)
        else:
            print("The tribespeople greet you, intrigued by a visitor.")

        choice = input("Do you:\n1.Try to communicate\n2.Run away\n")
        if choice == "1":
            if player.smell == "good":
                print("They invite you to a feast and offer directions to a safe path.")
                player.health += 30
                time.sleep(2)
                print("You got health back!")
                substate = "shelter"
            else:
                print("The tribes get irritated and chase you out!")
                player.take_damage(10)
                substate = "shelter"
        elif choice == "2":
            print("You quickly leave the village.")
            time.sleep(2)
            print("They throw some spears at you and you take damage!")
            player.take_damage(30)
            substate = "shelter"

    while substate == "shelter":
        print("You find an abandoned shelter with some old clothes.")
        if player.smell == "bad":
            print("The clothes don't help much with your smell.")
            player.take_damage(10)
        else:
            print("The clothes provide some cover.")
        substate = "temple"

    while substate == "temple":
        print("Ahead, you see a massive temple. Will you enter?")
        choice = input("1. Yes\n2. No\n")
        if choice == "1":
            print("The temple is full of traps but also promises treasure.")
            player.take_damage(20)
            print(f"After dodging traps, you find the Crystal Artifact!")
            gamestate = "end"
            break
        elif choice == "2":
            print("You decide not to risk it and find a safe path home.")
            gamestate = "end"
            break

print("Thanks for playing Crystal Diary!")
