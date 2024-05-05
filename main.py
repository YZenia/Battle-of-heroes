import random
class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        """Выполняет атаку на другого героя, уменьшая его здоровье на значение attack_power."""
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        """Проверяет, жив ли герой."""
        return self.health > 0

    def __str__(self):
        """Возвращает строковое представление героя."""
        return f"{self.name} (Здоровье: {self.health})"
class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        """Запускает игру и управляет чередованием ходов до определения победителя."""
        turn = 0  # 0 - ход игрока, 1 - ход компьютера
        while self.player.is_alive() and self.computer.is_alive():
            if turn == 0:
                print("\nТвой ход.")
                self.player.attack(self.computer)
                turn = 1
            else:
                print("\nХод компьютера.")
                self.computer.attack(self.player)
                turn = 0

            print(self)
            # Добавим небольшую задержку для лучшей читаемости ходов
            import time
            time.sleep(2)

        self.declare_winner()

    def __str__(self):
        """Возвращает текущее состояние здоровья героев."""
        return f"{self.player}\n{self.computer}"

    def declare_winner(self):
        """Определяет и объявляет победителя игры."""
        if self.player.is_alive():
            print(f"\nПобедил {self.player.name}!")
        else:
            print(f"\nПобедил {self.computer.name}!")

def main():
    print("Добро пожаловать в игру 'Битва героев'!")
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()

if __name__ == "__main__":
    main()
