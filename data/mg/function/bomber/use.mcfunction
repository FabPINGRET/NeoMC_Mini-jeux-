# Clic droit (@s, à sa position) : la bombe en main
execute if items entity @s weapon.mainhand *[custom_data~{bomb:1}] if score @s mg.bc1 matches ..0 run return run function mg:bomber/drop {t:1,cd:"bc1",cdv:12,sp:0.0009}
execute if items entity @s weapon.mainhand *[custom_data~{bomb:2}] if score @s mg.bc2 matches ..0 run return run function mg:bomber/drop {t:2,cd:"bc2",cdv:140,sp:0.0006}
execute if items entity @s weapon.mainhand *[custom_data~{bomb:3}] if score @s mg.bc3 matches ..0 run return run function mg:bomber/drop {t:3,cd:"bc3",cdv:100,sp:0.0009}
execute if items entity @s weapon.mainhand *[custom_data~{bomb:4}] run return run function mg:bomber/drop_nuke
playsound minecraft:block.dispenser.fail player @s ~ ~ ~ 0.4 1.6
