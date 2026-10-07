# Fusées illimitées : jamais moins de 3 (toutes les 2 s), protection renouvelée
execute store result score $efn mg.st run clear @s minecraft:firework_rocket[minecraft:custom_data~{mg_elyf:1b}] 0
execute if score $efn mg.st matches ..2 run give @s minecraft:firework_rocket[minecraft:custom_data={mg_elyf:1b},minecraft:fireworks={flight_duration:1},minecraft:custom_name={"text":"Fusée du spawn","color":"gold","italic":false}] 1
effect give @s minecraft:resistance 600 4 true
