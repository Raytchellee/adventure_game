import time
import random
import enum


class Colors(enum.Enum):
    yellow = '\033[93m'
    red = '\033[91m'
    white = '\033[97m'
    blue = '\033[94m'
    magenta = '\033[95m'
    grey = '\033[90m'
    purple = '\033[95m'

    @classmethod
    def choose_colors(colr):
        return random.choice([color.value for color in colr])


defense_list = ["gauntlet", "godstone", "flamethrower", "mine", "sword"]
evil_guys_list = ["Injustice leagues", "Cobra commands", "Thunderbolts",
                  "Hydras", "Assassins"]


def print_pause(message, delay=0):
    print(Colors.choose_colors() + message)
    time.sleep(delay)


def intro():
    print_pause("Entering the classroom early in the morning, "
                "you find your classmates crying.", 3)
    print_pause("You ask them what is wrong and you are told that "
                "your bestfriend has been kidnapped by "
                f"{evil_guys}.", 3)
    print_pause("You enquire which way they went and "
                "they direct you towards the old Factory.", 3)
    print_pause("You take off in search of your bestfriend before "
                "anybody could say another word.", 3)
    print_pause("An hour later, you are in front of "
                "the factory gate.", 3)
    print_pause("There is another entrance to the factory "
                "through the back gate.", 3)
    print_pause("The front gate is highly secured with "
                "armed men.", 3)
    print_pause("You are not sure how secure the back "
                "gate is.", 3)
    print_pause("To take the front gate, enter 1.", 3)
    print_pause("To take the back gate, enter 2.", 3)


def check_correct_input(message, options):
    while True:
        option = input(message).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is '
                    'invalid. Try again!')


def attack(defense_box,):
    print_pause(f"You combat with the {evil_guys}.", 1)
    if defense in defense_box:
        print_pause(f"The {evil_guys} rush to attack "
                    f"you, you pull out your {defense} "
                    "in defense and combat courageously.", 1)
        print_pause("You take them out with the "
                    f"{defense}.", 1)
        print_pause("You're victorious!", 1)
        print_pause("You free your bestfriend and take him "
                    "home feeling tired and happy.", 1)
    else:
        print_pause("But you did not think it through and you "
                    "are clueless on what to do.", 1)
        print_pause(f"The {evil_guys} seem very powerful and they possess "
                    "very advanced ammunitions.", 1)
        print_pause("You have nothing to fight with and "
                    "your enemy is armed to the teeth.", 1)
        print_pause("You've been defeated!", 1)
    print_pause("Would you like to play again?")
    start_again()


def run(defense_box):
    print_pause("You retrace your steps and run "
                "for your dear life.", 1)
    print_pause("You are back to the front "
                "gate", 1)
    print_pause(f"You turn back and the {evil_guys} "
                "are not after you.", 1)
    gate_choice(defense_box)


def front_gate():
    print_pause("You break the lock and enter the front gate.", 1)
    print_pause("As soon as you entered, "
                f"the {evil_guys} move to ambush you.", 1)
    print_pause("Would you like to attack or flee to safety?", 1)


def back_gate(defense_box):
    print_pause("You move round the wall and "
                "maneuver to the back gate.", 1)
    if defense in defense_box:
        print_pause("The gate is wide open and you meet "
                    "a security house with nobody "
                    "inside. You have collected all that was there.", 1)
        print_pause("You run back to the front gate", 1)
    else:
        print_pause("You get there and discover a "
                    f"new {defense}", 1)
        print_pause(f"You pick up the {defense} and "
                    "run back towards the front gate.", 1)
        defense_box.append(defense)
    gate_choice(defense_box)


def start_again():
    play_again = check_correct_input("Enter y for yes and "
                                     "n for no.\n", ["y", "n"])
    if play_again == "y":
        print_pause("Good choice! Restarting the "
                    "game...", 2)
        main_game()
    else:
        print_pause("Thanks for playing! Hope "
                    "you revisit the game soon.")
        exit(0)


def gate_choice(defense_box):
    choose_road = check_correct_input("Which gate will you like "
                                      "to enter?\n"
                                      "Please enter 1 or 2\n", ["1", "2"])
    if choose_road == "1":
        front_gate()
        fight_or_run = check_correct_input("Enter 1 to attack and 2 to "
                                           "flee to safety.\n", ["1", "2"])
        if fight_or_run == "1":
            attack(defense_box)
        else:
            run(defense_box)
    else:
        back_gate(defense_box)


def main_game():
    global defense
    global evil_guys
    defense = random.choice(defense_list)
    evil_guys = random.choice(evil_guys_list)
    defense_box = []
    intro()
    gate_choice(defense_box)


main_game()
