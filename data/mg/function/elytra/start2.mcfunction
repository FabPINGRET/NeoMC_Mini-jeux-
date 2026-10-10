# Départ du grand parcours d'élytra (@s = joueur sur le socle)
execute if entity @s[tag=mg.elyf] run function mg:elytra/free_stop
# Pas de baguette feu d'artifice ni de charges de vent pendant la course (rendue à la fin)
execute store result score @s mg.ehw run clear @s minecraft:blaze_rod
clear @s minecraft:wind_charge
tag @s add mg.ely
scoreboard players set @s mg.ecr 2
scoreboard players set @s mg.est 0
scoreboard players set @s mg.ec 0
scoreboard players set @s mg.et 0
scoreboard players set @s mg.eg 0
scoreboard players set #20 mg.st 20
scoreboard players set #5 mg.st 5
item replace entity @s armor.chest with minecraft:elytra[minecraft:custom_data={mg_ely:1b},minecraft:unbreakable={},minecraft:enchantments={"minecraft:binding_curse":1},minecraft:custom_name={"text":"Élytres du parcours","color":"aqua","italic":false}]
give @s minecraft:firework_rocket[minecraft:custom_data={mg_ely:1b},minecraft:fireworks={flight_duration:1},minecraft:custom_name={"text":"Fusée du parcours","color":"gold","italic":false}] 6
effect give @s minecraft:resistance 600 4 true
function mg:core/heal
tp @s -52.5 300 -47.5 facing -29.5 292 -47.5
playsound minecraft:entity.ender_dragon.flap master @s ~ ~ ~ 0.8 1.2
tellraw @s [{"text":"🪽 Grand parcours d'élytra : ","color":"aqua","bold":true},{"text":"saute, plane à travers les 15 anneaux dans l'ordre (une traînée lumineuse indique le suivant). Le chrono part à l'ouverture des élytres. 6 fusées.","color":"gray"}]
