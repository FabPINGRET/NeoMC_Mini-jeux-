# Socle « élytres libres » (@s, une fois par passage) : prendre ou rendre
tag @s add mg.efp
execute if entity @s[tag=mg.elyf] run return run function mg:elytra/free_off
tag @s add mg.elyf
item replace entity @s armor.chest with minecraft:elytra[minecraft:custom_data={mg_elyf:1b},minecraft:unbreakable={},minecraft:enchantments={"minecraft:binding_curse":1},minecraft:custom_name={"text":"Élytres du spawn","color":"white","italic":false}]
give @s minecraft:firework_rocket[minecraft:custom_data={mg_elyf:1b},minecraft:fireworks={flight_duration:1},minecraft:custom_name={"text":"Fusée du spawn","color":"gold","italic":false}] 3
effect give @s minecraft:resistance 600 4 true
effect give @s minecraft:levitation 2 14 true
playsound minecraft:entity.ender_dragon.flap master @s ~ ~ ~ 0.8 1.4
title @s actionbar [{"text":"🪽 Ouvre tes élytres en l'air (Espace) — fusées illimitées. Remonte sur le socle pour les rendre.","color":"white"}]
