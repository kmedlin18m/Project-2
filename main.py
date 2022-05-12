# Original Idea: https://codereview.stackexchange.com/questions/261247/terminal-typing-game
# Features added: Customer object, rules
def main():
    from time import time, sleep
    import random

    stat = True
    strike = 0
    score = 0
    wordBank = ''

    class Customer:
        """ A class representing details for the customer object
        """
        instances = []

        def __init__(self, person, wealth):
            """ Constructor to create initial state of the customer object.
            :param person: The customers' status
            :param wealth: The dollar amount that can be awarded to the player
            """
            self.person = person
            self.wealth = wealth
            __class__.instances.append(self)

    student = Customer("Student", 1)
    businessman = Customer("Businessman", 2)
    critic = Customer("Critic", 3)

    def start():
        """ Function to let the player know that the game is starting
        """
        print('Ready?')
        sleep(.5)
        print('Set?')
        sleep(.5)
        print('Go!')
        sleep(.5)

    start_input = input(f"Welcome to Restaurant Typing Game!\nYou are the owner of a new restaurant in town and your "
                        f"goal is to serve your customers.\nThere are three types of customers with different levels of "
                        f"difficulty and wealth. Students are EASY, Businessmen are MEDIUM, and critics are "
                        f"HARD.\nStudents will give you $1, Businessmen will give you $2 and Critics will give you "
                        f"$3.\nTo serve the customer, simply type what they order.\nIf you successfully type their "
                        f"order without typos in under three seconds the console will display the money you earned "
                        f"for that order!\nIf not, you get a strike.\nGet three strikes and the game is over. Once the "
                        f"game is over, your total earnings will be displayed.\nGOOD LUCK! press 's' to start: "
                        f"").strip().lower()
    while start_input != 's':
        start_input = input('Invalid input. Enter "s" to start: ')
    start()

    def game_check(wordBank):
        """
        Checks if the user input matches the chosen word.
        lst[0] = added points (dollars), lst[1] = added strikes
        :return lst
        """
        lst = [0, 0]
        wordChoice = random.choice(wordBank)
        print(f'A {randCustomer.person} has walked in!')
        sleep(1)
        start = time()
        wordType = input(f'They order {wordChoice}  : ')
        if wordType == wordChoice and time() - start < 3:
            if randCustomer == student:
                lst[0] += student.wealth
                print(f'+ ${student.wealth}!')
                sleep(.5)
            elif randCustomer == businessman:
                lst[0] += businessman.wealth
                print(f'+ ${businessman.wealth}!')
                sleep(.5)
            elif randCustomer == critic:
                lst[0] += critic.wealth
                print(f'+ ${critic.wealth}!')
                sleep(.5)
        elif time() - start >= 3:
            lst[1] += 1
            print('TOO SLOW')
            sleep(.5)
        else:
            lst[1] += 1
            print('WRONG SPELLING')
            sleep(1)
        return lst

    #This loop is what keeps the game running while the user has less than 3 strikes
    while stat:
        randIndex = random.randrange(len(Customer.instances))
        randCustomer = Customer.instances[randIndex]
        if randCustomer == student:
            openStudent = open('student.txt')
            readStudent = openStudent.read()
            wordBank = readStudent.split()
        elif randCustomer == businessman:
            openBusinessman = open('businessmen.txt')
            readBusinessman = openBusinessman.read()
            wordBank = readBusinessman.split()
        elif randCustomer == critic:
            openCritic = open('critic.txt')
            readCritic = openCritic.read()
            wordBank = readCritic.split()
        lst = game_check(wordBank)

        score += lst[0]
        strike += lst[1]
        print(f'STRIKES: {strike}')
        sleep(1)
        print(f'EARNINGS: ${score}')
        sleep(1)
        if strike == 3:
            print('Game Over! The game has ended...\n')
            sleep(1)
            print(f'Your total earnings: ${score}')
            sleep(1)
            break


if __name__ == '__main__':
    main()
