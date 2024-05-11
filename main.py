import sys
import numpy as np
import time

def imprimir_lento(s):
    for letra in s:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.05)

class Pokemon:
    def __init__(self, name, types, moves, EVs, health_bar='==============='):
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health_bar = health_bar
        self.hearts = 20

    def battle(self, pokemon2):
        print('-----POKEMON BATTLE-----')
        print(f'\n{self.name}')
        print('TYPE/', self.types)
        print('ATTACK/', self.attack)
        print('DEFENSE/', self.defense)
        print('LVL./', 4 * (np.mean([self.attack, self.defense])))
        print('----------VS----------')
        print(f'\n{pokemon2.name}')
        print('TYPE/', pokemon2.types)
        print('ATTACK/', pokemon2.attack)
        print('DEFENSE/', pokemon2.defense)
        print('LVL/', 4 * (np.mean([pokemon2.attack, pokemon2.defense])))

        time.sleep(2)

        # Check if there is an advantage!
        types = ['Fire', 'Water', 'Grass']
        for i, ele in enumerate(types):
            if self.types == ele:
                # Both are the same type
                if pokemon2.types == ele:
                    attack_1 = 'Its not very effective...'
                    attack_2 = 'Its not very effective...'
                # Second pokemon has an advantage
                if pokemon2.types == types[(i + 1) % 3]:
                    pokemon2.attack *= 2
                    pokemon2.defense *= 2
                    self.attack /= 1.5
                    self.defense /= 1.5
                    attack_1 = 'Its not very effective...'
                    attack_2 = 'Its super effective!'
                # First pokemon has an advantage
                if pokemon2.types == types[(i + 2) % 3]:
                    self.attack *= 2
                    self.defense *= 2
                    pokemon2.attack /= 1.5
                    pokemon2.defense /= 1.5
                    attack_1 = 'Its super effective!'
                    attack_2 = 'Its not very effective...'

        while( self.hearts > 0 and pokemon2.hearts > 0 ):
            print(f'{self.name}\t\t HEALTH\t{self.health_bar}')
            print(f'{pokemon2.name}\t\t HEALTH\t{pokemon2.health_bar}\n')

            print(f'GO {self.name}!')
            for i, ele in enumerate(self.moves):
                print(f'{i + 1})', ele)
            index = int(input('Pick a move: '))
            imprimir_lento(f'{self.name} used {self.moves[index-1]}!\n')
            time.sleep(1)
            imprimir_lento(attack_1)

            pokemon2.hearts -= self.attack
            pokemon2.health_bar = ""

            for j in range(int(pokemon2.hearts+.1*pokemon2.defense)):
                pokemon2.health_bar += "="

            time.sleep(1)
            print(f'\n{self.name}\t\t HEALTH\t{self.health_bar}')
            print(f'{pokemon2.name}\t\t HEALTH\t{pokemon2.health_bar}\n')
            time.sleep(0.5)

            if pokemon2.hearts <=0:
                imprimir_lento('\n...' + pokemon2.name + ' fainted !\n')
                break

            print(f'GO {pokemon2.name}!')
            for i, ele in enumerate(pokemon2.moves):
                print(f'{i + 1})', ele)
            index = int(input('Pick a move: '))
            imprimir_lento(f'{pokemon2.name} used {pokemon2.moves[index - 1]}!\n')
            time.sleep(1)
            imprimir_lento(attack_2)

            self.hearts -= pokemon2.attack
            self.health_bar = ""

            for j in range(int(self.hearts + .1 * self.defense)):
                self.health_bar += "="

            time.sleep(1)
            print(f'\n{pokemon2.name}\t\t HEALTH\t{pokemon2.health_bar}')
            print(f'{self.name}\t\t HEALTH\t{self.health_bar}\n')
            time.sleep(0.5)

            if self.hearts <= 0:
                imprimir_lento('\n...' + self.name + ' fainted !\n')
                break

        money = np.random.choice(5000)
        imprimir_lento(f'Opponent paid you ${money}.')

if __name__ == "__main__":
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fire Blast', 'Solar Beam', 'Dragon Pulse'], {'ATTACK': 14, 'DEFENSE': 8})
    Blastoise = Pokemon('Blastoise', 'Water', ['Water Pulse', 'Rapid Spin', 'Aqua Tail', 'Hydro Pump'], {'ATTACK': 12, 'DEFENSE': 10})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Petl Blizazrd', 'Sluge Bomb', 'Solar Beam', 'Razor Leaf'], {'ATTACK': 10, 'DEFENSE': 12})

    Charizard.battle(Blastoise)


