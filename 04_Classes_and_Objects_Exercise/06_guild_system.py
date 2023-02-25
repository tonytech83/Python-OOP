# Exam: 06. Guild System
# From: Classes and Objects - Exercise
# URL: https://judge.softuni.org/Contests/Compete/Index/1937#5

from project.player import Player
from project.guild import Guild

# Test code
player = Player("George", 50, 100)
player_1 = Player("Ivan", 50, 100)

print(player.add_skill("Shield Break", 20))
print(player.add_skill("Attack", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.assign_player(player_1))
print(guild.kick_player('George'))
print(guild.guild_info())
