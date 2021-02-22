from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.roll()
        self.reset()
    
    def roll(self):
        self.dice = Die.create_dice(5)

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value ## fix no.1
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        runner = cls() ## fix no.2
        while True:
            runner.roll() ## fix no.3
            print("Round {}\n".format(runner.round))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)
            

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.round += 1

            if runner.wins == 6: ## fix no.4
                print("YOU WON... Hurray !!!")
                break

            if runner.loses == 6:
                print("YOU LOST...  Please try again....")
                break


            prompt = input("Would you like to play again?[if yes type Y, else press any key to exit]:")

            if prompt.upper() == 'Y' : 
                continue
            else:
                break
