# Baguette feu d'artifice (@s = joueur, position = joueur)
scoreboard players reset @s mg.fw
# l'objet est consommé par le clic : on le redonne
execute store result score $apc mg.st run clear @s minecraft:blaze_rod 0
execute if score $apc mg.st matches 0 run function mg:lobby/give_wand
# recharge de 5 s (100 ticks)
execute if score @s mg.wd matches 1.. run return run function mg:lobby/wand_wait
scoreboard players set @s mg.wd 100
playsound minecraft:entity.firework_rocket.launch master @a ~ ~ ~ 1.5 1
particle minecraft:firework ~ ~1 ~ 0.2 0.3 0.2 0.3 25
execute positioned ~ ~16 ~ run function mg:lobby/boom
