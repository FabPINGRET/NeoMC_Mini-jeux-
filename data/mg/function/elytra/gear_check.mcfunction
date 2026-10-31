# @s (gear_keep vrai, toutes les 2 s) : élytres sur le dos, fusées (au moins 3), ⚡ Vitesse et 🐇 Super saut
execute unless entity @s[tag=mg.lgear] run title @s actionbar [{"text":"🪽 Élytres + fusées","color":"white"},{"text":"  ⚡ Vitesse","color":"yellow"},{"text":"  🐇 Super saut","color":"green"},{"text":" : tiens l'objet en main","color":"gray"}]
tag @s add mg.lgear
execute unless items entity @s armor.chest * run item replace entity @s armor.chest with minecraft:elytra[minecraft:custom_data={mg_elyf:1b},minecraft:unbreakable={},minecraft:enchantments={"minecraft:binding_curse":1},minecraft:attribute_modifiers=[{type:"minecraft:fall_damage_multiplier",id:"mg:lobby_fall",amount:-1,operation:"add_multiplied_total",slot:"chest"}],minecraft:custom_name={"text":"Élytres du spawn","color":"white","italic":false}]
execute store result score $efn mg.st run clear @s minecraft:firework_rocket[minecraft:custom_data~{mg_elyf:1b}] 0
execute if score $efn mg.st matches 0 run function mg:elytra/gear_rockets
execute if score $efn mg.st matches 1..2 run give @s minecraft:firework_rocket[minecraft:custom_data={mg_elyf:1b},minecraft:fireworks={flight_duration:1},minecraft:custom_name={"text":"Fusée du spawn","color":"gold","italic":false}] 1
execute unless items entity @s container.* *[minecraft:custom_data~{mg_spd:1b}] unless items entity @s player.cursor *[minecraft:custom_data~{mg_spd:1b}] run function mg:elytra/gear_speed
execute unless items entity @s container.* *[minecraft:custom_data~{mg_jmp:1b}] unless items entity @s player.cursor *[minecraft:custom_data~{mg_jmp:1b}] run function mg:elytra/gear_jump
