import random
import time
import naoqi

from naomotions import *


def greeting(robot, do_stand_and_wave = False):

    # do the stand and wave if we want to
    if (do_stand_and_wave):
        robot.posture.goToPosture("Stand", 0.3)
        id = robot.genSpeech("Hello, my friend!")
        robot.wave()
        robot.speechDevice.wait(id, 0)

    # initialize at crouch position
    robot.posture.goToPosture("Crouch", 0.3)

    # introduce the game of rock-paper-scissors
    id = robot.genSpeech("Let's play a game of rock paper scissors together! \\pau=500\\ I'll show you how we can play. We'll go")
    robot.speechDevice.wait(id, 0)
    rock_paper_scissors_shoot(robot, "rock")

    id = robot.genSpeech("This is how I do rock")
    robot.speechDevice.wait(id, 0)
    robot.swing()
    robot.paper()
    id = robot.genSpeech("This is how I do paper")
    robot.speechDevice.wait(id, 0)
    robot.motion.closeHand('RHand')
    robot.swing()
    robot.scissors()
    id = robot.genSpeech("And this is how I do scissors")
    robot.speechDevice.wait(id, 0)
    robot.motion.closeHand('RHand')
    robot.rock()

    time.sleep(0.5)
    robot.genSpeech("Are you ready? Let's play.")


def rock_paper_scissors_shoot(robot, choice):

    robot.rock()
    robot.swing()
    robot.rock()
    robot.genSpeech("rock")
    robot.swing()
    robot.rock()
    robot.genSpeech("paper")
    robot.swing()
    robot.rock()
    robot.genSpeech("scissors")
    robot.swing()

    if (choice == "scissors"):
        robot.scissors()
    elif (choice == "paper"):
        robot.paper()
    else:
        robot.rock()

    robot.genSpeech("shoot")

    time.sleep(1.0)


def play(robot):

    num_user_wins = 0

    while True:

        robot_choices = ["rock", "paper", "scissors"]
        robot_choice = robot_choices[random.randint(0,2)]
        print("\nRobot chooses: " + robot_choice + "\n")
        rock_paper_scissors_shoot(robot, robot_choice)

        wizard_input = raw_input("\nEnter either Rock[R], Paper[P], Scissors[S], Greeting[G], or End[E]:\n")

        possible_outcomes = [
            "user wins",
            "robot wins",
            "tie"
        ]
        outcome = ""

        if (wizard_input == "G" or wizard_input == "g"):
            greeting(robot, False)
            # robot_choice = robot_choices[random.randint(0,2)]
            # print("\nRobot chooses: " + robot_choice + "\n")
            # rock_paper_scissors_shoot(robot, robot_choice)
            num_user_wins = 0

        elif (wizard_input == "E" or wizard_input == "e"):
            robot.posture.goToPosture("Crouch", 0.3)
            robot.release_nao()
            break

        elif (wizard_input == "R" or wizard_input == "r"):
            if (robot_choice == "rock"):
                # rock ties with rock
                outcome = possible_outcomes[2]
            elif (robot_choice == "paper"):
                # user's rock loses to robot's paper
                outcome = possible_outcomes[1]
            else:
                # user's rock wins over robot's scissors
                outcome = possible_outcomes[0]

        elif (wizard_input == "P" or wizard_input == "p"):
            if (robot_choice == "rock"):
                # user's paper beats robot's rock
                outcome = possible_outcomes[0]
            elif (robot_choice == "paper"):
                # paper ties with paper
                outcome = possible_outcomes[2]
            else:
                # user's paper loses to robot's scissors
                outcome = possible_outcomes[1]

        elif (wizard_input == "S" or wizard_input == "s"):
            if (robot_choice == "rock"):
                # user's scissors loses to robot's rock
                outcome = possible_outcomes[1]
            elif (robot_choice == "paper"):
                # user's scissors beat's robot's paper
                outcome = possible_outcomes[0]
            else:
                # scissors ties with scissors
                outcome = possible_outcomes[2]

        else:
            print("Unknown user input")

        # robot announces the outcome
        if (outcome == "user wins"):
            # robot cheat
            # if (num_user_wins % 2 == 1):
            print("\nUser is winning and robot decides to cheat.\n")
            if (robot_choice == "rock"):
                robot.scissors()
            elif (robot_choice == "paper"):
                robot.rock()
                robot.motion.closeHand('RHand')
            else:
                robot.paper()
            robot.genSpeech("I win!")
            # else:
            #     robot.genSpeech("You win! Good job.")
            time.sleep(1)
            robot.genSpeech("Let's play again.")

            # increment number of user wins (disregarding robot cheating)
            num_user_wins += 1
        elif (outcome == "robot wins"):
            robot.genSpeech("I win!")
            time.sleep(1)
            robot.genSpeech("Let's play again.")
        elif (outcome == "tie"):
            robot.genSpeech("It's a tie!")
            time.sleep(1)
            robot.genSpeech("Let's play again.")

        robot.posture.goToPosture("Crouch", 0.3)

    robot.posture.goToPosture("Crouch", 0.3)

def testing(robot):

    robot.rock()
    robot.swing()
    robot.rock()
    robot.genSpeech("rock")

    angles = robot.motion.getAngles("RWristYaw", False)
    print(angles)

    # robot.posture.goToPosture("Crouch", 0.3)
    # robot.release_nao()


if __name__ == "__main__":

    # ip_address = raw_input("Robot IP Address:\n")
    ip_address = "192.168.1.139"
    robot = NaoRobot(ip_address, 9559)

    time.sleep(1.0)

    do_greeting = raw_input("\nRobot greeting? [Y/N]:\n")
    if (do_greeting == "Y" or do_greeting == "y"):
        do_standing_greeting = raw_input("\nStanding robot greeting? [Y/N]:\n")
        if (do_standing_greeting == "Y" or do_standing_greeting == "y"):
            greeting(robot, True)
        else:
            greeting(robot, False)

    play(robot)
    # testing(robot)

    robot.posture.goToPosture("Crouch", 0.3)
    # robot.release_nao()
