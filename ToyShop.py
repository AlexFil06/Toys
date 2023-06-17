import random


class ToyShop:
    def __init__(self):
        self.toys = []

    def add_toy(self, toy):
        self.toys.append(toy)

    def play(self):
        prizes = []
        for toy in self.toys:
            for i in range(toy.quantity):
                prizes.append(toy)


        while True:
            choice = input("Нажмите Enter, чтобы получить призовую игрушку или Q для выхода: ")
            if choice.lower() == "q":
                break

            if not prizes:
                print("Призы закончились!")
                break


            prize = self.get_prize_toy(prizes)
            with open("prizes.txt", "a", encoding='UTF-8') as file:
                file.write(f"{prize.name}\n")
            print(f"Вы получили призовую игрушку: {prize.name}")

    def get_prize_toy(self, prizes):
        prize = random.choice(prizes)
        prize.remove_quantity(1)
        prizes.remove(prize)
        return prize

    def __str__(self):
        result = "Список игрушек:\n"
        for toy in self.toys:
            result += str(toy) + "\n"
        return result