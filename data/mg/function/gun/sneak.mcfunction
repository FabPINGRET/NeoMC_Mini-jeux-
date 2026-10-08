# Accroupi avec une arme en main : recharge
scoreboard players reset @s mg.gsn
execute if items entity @s weapon.mainhand *[custom_data~{gun:1}] run return run function mg:gun/reload_1
execute if items entity @s weapon.mainhand *[custom_data~{gun:2}] run return run function mg:gun/reload_2
execute if items entity @s weapon.mainhand *[custom_data~{gun:3}] run return run function mg:gun/reload_3
execute if items entity @s weapon.mainhand *[custom_data~{gun:4}] run return run function mg:gun/reload_4
execute if items entity @s weapon.mainhand *[custom_data~{gun:5}] run return run function mg:gun/reload_5
execute if items entity @s weapon.mainhand *[custom_data~{gun:6}] run return run function mg:gun/reload_6
