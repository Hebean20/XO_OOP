import random

class Tabla:
    victory_pos = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9},
                   {1, 4, 7}, {2, 5, 8}, {3, 6, 9},
                   {1, 5, 9}, {3, 5, 7}
                   ]

    def __init__(self):
        self.player = None
        self.user_sign = None
        self.pc_sign = None
        self.win = False
        self.pc_choices = set()
        self.user_choices = set()
        self.list_pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.harta2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.set_user_sign()

    def is_win(self, player):
        player_pos = self.user_choices if player == 'User' else self.pc_choices
        for item in self.victory_pos:
            if item.issubset(player_pos):
                print(f'Win for the {player}')
                return True
        return False

    def set_user_sign(self):
        choice = input("Your sign is: ")
        if choice in ['X', 'x']:
            self.user_sign = 'X'
            self.pc_sign = 'O'
        elif choice in ['O', 'o', '0']:
            self.user_sign = 'O'
            self.pc_sign = 'X'
        else:
            print("Choose again")
            self.set_user_sign()
    def set_pos_user(self):
        try:
            pos = int(input("Choose your position: "))
            if pos not in self.list_pos:
                print("Choose a valid position")
            elif pos not in self.user_choices and pos not in self.pc_choices:
                self.harta2[pos - 1] = self.user_sign
                self.list_pos.remove(pos)
                self.user_choices.add(pos)
            else:
                print("Position already taken. Choose again.")
                self.set_pos_user()
        except ValueError:
            print("Invalid input. Try again.")

    def set_pos_pc(self):
        pc_choice = random.choice(self.list_pos)
        self.harta2[pc_choice - 1] = self.pc_sign
        self.list_pos.remove(pc_choice)
        self.pc_choices.add(pc_choice)

    def __str__(self):
        result = "List of remaining positions: " + str(self.list_pos) + "\n"
        for i in range(0, len(self.harta2), 3):
            result += ' '.join(self.harta2[i:i+3]) + "\n"
        result += "Computer positions: " + str(self.pc_choices) + "\n"
        result += "User positions: " + str(self.user_choices)
        return result

game = Tabla()
if game.pc_sign == 'X':
    game.set_pos_pc()

while len(game.list_pos):
    game.set_pos_user()
    if game.is_win('User'):
        game.win = True
        print(game)
        break
    if len(game.list_pos):
        game.set_pos_pc()
        if game.is_win('PC'):
            game.win = True
            print(game)
            break
    print(game)

if not game.win and len(game.list_pos) == 0:
    print('Draw')