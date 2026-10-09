# @s (zone cliquable d'une voiture) : le joueur qui a cliqué monte au volant
scoreboard players operation $gv mg.st = @s mg.gvid
execute on target run function mg:gta/car_mount
data remove entity @s interaction
data remove entity @s attack
