# Exam: 08. Pokemon Battle
# From: First Steps in OOP - Exercise
# URL: https://judge.softuni.org/Contests/Compete/Index/1935#7

from project.pokemon import Pokemon
from project.trainer import Trainer

# Test code
pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
