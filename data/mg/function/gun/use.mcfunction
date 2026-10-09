# Clic droit avec une arme (@s, à sa position)
scoreboard players reset @s mg.qs
execute if score @s mg.gcd matches 1.. run return 0
execute if score @s mg.grl matches 1.. run return run playsound minecraft:block.dispenser.fail player @s ~ ~ ~ 0.4 1.8
execute if items entity @s weapon.mainhand *[custom_data~{gun:1}] run return run function mg:gun/fire_1
execute if items entity @s weapon.mainhand *[custom_data~{gun:2}] run return run function mg:gun/fire_2
execute if items entity @s weapon.mainhand *[custom_data~{gun:3}] run return run function mg:gun/fire_3
execute if items entity @s weapon.mainhand *[custom_data~{gun:4}] run return run function mg:gun/fire_4
execute if items entity @s weapon.mainhand *[custom_data~{gun:5}] run return run function mg:gun/fire_5
execute if items entity @s weapon.mainhand *[custom_data~{gun:6}] run return run function mg:gun/fire_6
