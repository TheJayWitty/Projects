import random
from colorama import Fore, Style

print("""
                                  ,'\ 
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
""")
print(Fore.CYAN + "="*71 + Style.RESET_ALL)

class Pokemon:
    def __init__(self, name, type, level, color):
        self.name = name
        self.type = type
        self.level = level
        self.health = level * 10
        self.max_health = level * 10
        self.color = color

    def attack(self, other):
        damage = random.randint(1, self.level * 2)
        print(f"{self.color}{self.name}{Style.RESET_ALL} attacks {other.color}{other.name}{Style.RESET_ALL} for {Fore.RED}{damage} damage{Style.RESET_ALL}!")
        other.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.color}{self.name}{Style.RESET_ALL} {Fore.RED}fainted!{Style.RESET_ALL}")
        else:
            self.display_health()

    def display_health(self):
        health_percentage = self.health / self.max_health
        bar_length = 20
        filled_length = int(bar_length * health_percentage)
        bar = Fore.GREEN + '[]' * filled_length + Fore.RED + '-' * (bar_length - filled_length)
        print(f"{self.color}{self.name}'s Health: {bar}{Style.RESET_ALL} {self.health}/{self.max_health} HP")

def choose_starter():
    print(f"{Fore.WHITE}Choose your starter Pokemon:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}1. Bulbasaur (Grass)")
    print(f"{Fore.RED}2. Charmander (Fire)")
    print(f"{Fore.BLUE}3. Squirtle (Water){Style.RESET_ALL}")
    choice = input("Enter 1, 2, or 3: ")
    if choice == '1':
        return Pokemon("Bulbasaur", "Grass", 5, Fore.GREEN)
    elif choice == '2':
        return Pokemon("Charmander", "Fire", 5, Fore.RED)
    elif choice == '3':
        return Pokemon("Squirtle", "Water", 5, Fore.BLUE)
    else:
        print("Invalid choice. Choosing Pikachu for you.")
        return Pokemon("Pikachu", "Electric", 5, Fore.YELLOW)

def battle(player, opponent):
    print(f"\n{Fore.YELLOW}A wild {opponent.color}{opponent.name}{Fore.YELLOW} appears!{Style.RESET_ALL}")
    while player.health > 0 and opponent.health > 0:
        print("\n" + Fore.CYAN + "="*71 + Style.RESET_ALL)
        player.display_health()
        opponent.display_health()
        print(Fore.CYAN + "="*71 + Style.RESET_ALL)
        action = input(f"Do you want to {Fore.GREEN}(1) Attack{Style.RESET_ALL} or {Fore.YELLOW}(2) Run{Style.RESET_ALL}? ")
        if action == '1':
            player.attack(opponent)
            if opponent.health > 0:
                opponent.attack(player)
        elif action == '2':
            print(f"{Fore.YELLOW}You ran away!{Style.RESET_ALL}")
            return
        else:
            print(f"{Fore.RED}Invalid choice. Skipping turn.{Style.RESET_ALL}")
    
    if player.health > 0:
        print(f"{Fore.GREEN}You won the battle!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}You lost the battle!{Style.RESET_ALL}")

def main():
    player = choose_starter()
    print(f"You chose {player.color}{player.name}{Style.RESET_ALL}!")
    
    while player.health > 0:
        input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
        opponent = random.choice([
            Pokemon("Pidgey", "Flying", 3, Fore.LIGHTWHITE_EX),
            Pokemon("Rattata", "Normal", 2, Fore.LIGHTBLACK_EX),
            Pokemon("Caterpie", "Bug", 1, Fore.GREEN)
        ])
        battle(player, opponent)
        if player.health <= 0:
            print(f"{Fore.RED}Game Over!{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    main()