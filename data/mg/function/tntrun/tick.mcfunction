# TNT Run — tick de jeu

# Marquage du bloc sous chaque joueur (au sol uniquement)
execute as @a[tag=mg.play] at @s if block ~ ~-1 ~ minecraft:white_wool run setblock ~ ~-1 ~ minecraft:red_wool

# Décroissance : les blocs marqués disparaissent régulièrement
scoreboard players remove $dk mg.st 1
execute if score $dk mg.st matches ..0 run function mg:tntrun/decay

# Chute finale → éliminé
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute if score $ar mg.st matches 0 as @a[tag=mg.play,scores={mg.t=..58}] run function mg:core/eliminate
execute if score $ar mg.st matches 1.. as @a[tag=mg.play] if score @s mg.t <= $ky mg.st run function mg:core/eliminate

# Mort accidentelle → éliminé
execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:core/eliminate

# Victoire
execute store result score $alive mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $alive mg.st matches 1 as @a[tag=mg.play,limit=1] run function mg:core/win_player
execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw
