# One in the Chamber — tick de jeu

# Nouvelles flèches : dégâts énormes (one-shot) et non ramassables ; les flèches plantées disparaissent
execute as @e[distance=0..,type=minecraft:arrow,tag=!mg.ar] run function mg:oitc/arrow_new
# Flèches enchantées : traînée, explosion
execute as @e[type=minecraft:arrow,tag=mg.sp] at @s run function mg:oitc/sp_tick

# Une flèche enchantée toutes les 30 s pour un joueur au hasard
scoreboard players add $os mg.st 1
execute if score $os mg.st matches 600.. run function mg:oitc/special_timer

execute as @e[distance=0..,type=minecraft:arrow,nbt={inGround:1b}] run kill @s

# Recharge auto : 1 flèche après 5 s sans flèche
execute as @a[tag=mg.play] run function mg:oitc/ammo

# KILL → une flèche de plus
execute as @a[tag=mg.play,scores={mg.pk=1..}] run function mg:oitc/kill_reward

# Chute dans le vide → compte comme une mort
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,scores={mg.t=..70}] run function mg:oitc/death

# Mort → une vie en moins
execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:oitc/death

# Victoire : premier à 10 kills
execute if score $state mg.st matches 2 as @a[tag=mg.play,scores={mg.ok=10..},limit=1] run function mg:core/win_player
execute store result score $alive mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $alive mg.st matches 1 as @a[tag=mg.play,limit=1] run function mg:core/win_player
execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw
