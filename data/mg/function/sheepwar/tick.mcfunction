# Sheep War — tick de jeu
# (le lancement des moutons passe par l'advancement mg:sheep_launch → launch_adv)

# Délai entre deux lancers (1 s)
scoreboard players remove @a[scores={mg.cd=1..}] mg.cd 1

# Vie des moutons (mèche + explosion)
execute as @e[tag=mg.sheep] at @s run function mg:sheepwar/sheep_tick

# Flammes temporaires des moutons de feu
execute as @e[type=minecraft:marker,tag=mg.fx] at @s run function mg:sheepwar/fire_tick

# Soin lent (remplace la régénération naturelle) : 2 cœurs toutes les 12 s
scoreboard players remove $sh mg.st 1
execute if score $sh mg.st matches ..0 run function mg:sheepwar/slow_heal

# Recharge de munitions
scoreboard players remove $sr mg.st 1
execute if score $sr mg.st matches ..0 run function mg:sheepwar/refill

# Tombé dans le vide → éliminé
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,scores={mg.t=..60}] run function mg:core/eliminate

# Mort (explosion) → éliminé
execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:core/eliminate

# Victoire d'équipe
execute store result score $nr mg.st if entity @a[team=mg_red,tag=mg.play]
execute store result score $nb mg.st if entity @a[team=mg_blue,tag=mg.play]
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $nr mg.st matches 0 if score $nb mg.st matches 1.. run function mg:core/win_blue
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $nb mg.st matches 0 if score $nr mg.st matches 1.. run function mg:core/win_red
execute if score $state mg.st matches 2 if score $nr mg.st matches 0 if score $nb mg.st matches 0 run function mg:core/draw
