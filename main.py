import random

def main():
    print("Welcome to the Strange and Fun Adventure Game!")
    name = input("What is your name, adventurer? ")
    print(f"Greetings, {name}! Prepare to discover your unique destiny.")
    
    # Discover your class
    player_class = discover_class()
    print(f"You are now a {player_class['name']}! {player_class['description']}")

    # Start the adventure
    adventure(player_class)

def discover_class():
    classes = [
        {
            "name": "Bubble Mage",
            "description": "A master of soap-based sorcery. Your enemies will slip and slide to their doom!",
            "power": "Blow bubbles that explode into sticky traps."
        },
        {
            "name": "Pun Paladin",
            "description": "A knight who defends justice with the power of terrible jokes. Your enemies cringe in agony!",
            "power": "Deliver puns so awful they deal psychic damage."
        },
        {
            "name": "Toaster Tamer",
            "description": "You command sentient toasters, wielding the power of perfectly browned bread!",
            "power": "Summon an army of toast to overwhelm your foes."
        },
        {
            "name": "Meme Monk",
            "description": "Harness the wisdom of ancient memes to confound your enemies and inspire your allies.",
            "power": "Invoke timeless internet humor to distract and demoralize opponents."
        },
        {
            "name": "Duck Whisperer",
            "description": "A communicator with ducks, your quacky companions aid you in unexpected ways.",
            "power": "Summon a flock of ducks for chaotic assistance."
        }
    ]

    return random.choice(classes)

def adventure(player_class):
    print("\nYour adventure begins...")
    print("You stand at the entrance of a dark and mysterious forest. A path lies before you.")

    while True:
        print("\nWhat will you do?")
        print("1. Enter the forest.")
        print("2. Inspect your surroundings.[NOT YET FULLY IMPLEMENTED]")
        print("3. Use your unique power.[NOT YET FULLY IMPLEMENTED]")
        print("4. Quit the game.")
        
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("\nYou venture deeper into the forest. Strange sounds echo around you. Suddenly, a wild challenge appears!")
            challenge(player_class)
        elif choice == "2":
            print("\nYou look around and see ancient trees, glowing mushrooms, and perhaps... a lurking shadow.")
        elif choice == "3":
            print(f"\nYou use your power: {player_class['power']}")
            print("It's super effective (or maybe just confusing)! You feel accomplished.")
        elif choice == "4":
            print("\nThank you for playing! May your strange class bring joy to all your adventures.")
            break
        else:
            print("\nInvalid choice. Try again.")

def challenge(player_class):
    enemies = [
        "a grumpy gnome",
        "a mischievous pixie",
        "a towering ogre with a big appetite",
        "a sentient pile of leaves",
        "a ghostly librarian who demands silence"
    ]

    enemy = random.choice(enemies)
    print(f"You encounter {enemy}!")

    action = input("Do you want to (1) fight, (2) talk, or (3) run away? ")

    if action == "1":
        print(f"\nYou engage in battle using your {player_class['power']}.")
        if random.random() > 0.3:
            print(f"You defeated {enemy} with style! Your adventure continues.")
        else:
            print(f"Oh no! {enemy} proved too strong this time. You narrowly escape.")
    elif action == "2":
        print(f"\nYou attempt to reason with {enemy}.")
        if random.random() > 0.5:
            print(f"Your clever words convince {enemy} to let you pass. Well done!")
        else:
            print(f"{enemy} doesn't seem interested in talking. It attacks!")
            print("You barely manage to get away.")
    elif action == "3":
        print(f"\nYou decide to run away from {enemy}. Sometimes discretion is the better part of valor.")
    else:
        print("\nInvalid choice. You hesitate, and {enemy} gets the upper hand! You escape, but only just.")

if __name__ == "__main__":
    main()
