# Flèche qui vient d'être tirée (@s = la flèche) : one-shot, non ramassable
tag @s add mg.ar
data modify entity @s damage set value 1000.0d
data modify entity @s pickup set value 0b

# Flèches enchantées : type lu dans les données de l'objet tiré (1 explosive, 2 perforante, 3 révélatrice)
scoreboard players set @s mg.ak 0
execute store result score @s mg.ak run data get entity @s item.components."minecraft:custom_data".mg_ar
execute if score @s mg.ak matches 1..3 run tag @s add mg.sp
execute if score @s mg.ak matches 1 run tag @s add mg.ex
execute if score @s mg.ak matches 2 run data modify entity @s PierceLevel set value 3b
execute if score @s mg.ak matches 3 run function mg:oitc/sp_reveal
