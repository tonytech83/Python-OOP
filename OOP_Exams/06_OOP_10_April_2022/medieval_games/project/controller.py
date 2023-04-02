from typing import List

from project.player import Player
from project.supply.supply import Supply


class Controller:

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *args: Player):
        added_players = []

        for player in args:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)

        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *args: Supply):
        self.supplies.extend(args)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player_by_name(player_name)

        if not player:
            return

        if sustenance_type not in ["Food", "Drink"]:
            return

        if player.stamina == 100:
            return f"{player.name} have enough stamina."

        supply = self.__take_last_supply(sustenance_type)
        if supply:

            if player.stamina + supply.energy > 100:
                player.stamina = 100
            else:
                player.stamina += supply.energy

            return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)

        result = self.__check_players_condition_before_duel(first_player, second_player)
        if result:
            return result

        sort_players_by_stamina = sorted([first_player, second_player], key=lambda x: x.stamina)
        first_attacker = sort_players_by_stamina[0]
        second_attacker = sort_players_by_stamina[1]

        second_attacker.stamina -= first_attacker.stamina / 2
        if first_attacker.stamina - (second_attacker.stamina / 2) < 0:
            first_attacker.stamina = 0
        else:
            first_attacker.stamina -= second_attacker.stamina / 2

        if first_attacker.stamina < second_attacker.stamina:
            return f"Winner: {second_attacker.name}"
        else:
            return f"Winner: {first_attacker.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= (player.age * 2)

            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        data = []
        for player in self.players:
            data.append(f"Player: {player.name}, {player.age}, {player.stamina}, {player.need_sustenance}")
        for supply in self.supplies:
            data.append(f'{supply.supply_type}: {supply.name}, {supply.energy}')

        return '\n'.join(data)

    @staticmethod
    def __check_players_condition_before_duel(*players):
        result_str = []
        for player in players:
            if player.stamina == 0:
                result_str.append(f"Player {player.name} does not have enough stamina.")

        if result_str:
            return '\n'.join(result_str)

    def __find_player_by_name(self, player_name):
        return next((p for p in self.players if p.name == player_name), False)

    def __take_last_supply(self, supply_type):
        for i in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[i]).__name__ == supply_type:
                return self.supplies.pop(i)

        raise Exception(f"There are no {supply_type.lower()} supplies left!")
