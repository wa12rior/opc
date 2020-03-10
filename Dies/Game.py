from Die import Die


class Game:
    def __init__(self):
        print("Welcome to die game called 'oczko'!")

        self.__die = Die(6)
        self.__playerScore = 0
        self.__computerScore = 0
        self.__on = True

    def start(self):
        # Game loop
        print("Do you want to roll a die? (y/n)")
        play_more = input()

        while self.__on:
            if play_more == 'n' or self.__playerScore >= 21:
                self.__on = False
                print("\n------------ Summary -------------\n")
                self.__show_score()
                break

            print("Do you want to roll a die? (y/n)")
            play_more = input()

            self.__turn()
            self.__show_score()
        print(
            "You win." if self.__playerScore > self.__computerScore else
            "You've lost." if self.__playerScore < self.__computerScore else
            "It's draw."
        )

    def __turn(self):
        for throw in range(4):
            self.__die.roll()
            if throw <= 1:
                self.__computerScore += self.__die.get_value()
            else:
                self.__playerScore += self.__die.get_value()

    def __show_score(self):
        print(f"Your score is {self.__playerScore} points.")
        if not self.__on:
            print(f"Computer score is {self.__computerScore} points.")
