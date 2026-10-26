# @s : l'arme en main passe au Pack-a-Punch (dégâts ×3, chargeur ×2, voir guns.py)
item modify entity @s weapon.mainhand {function:"minecraft:set_custom_data",tag:{pap:1b}}
item modify entity @s weapon.mainhand {function:"minecraft:set_components",components:{"minecraft:enchantment_glint_override":true}}
execute if items entity @s weapon.mainhand *[custom_data~{gun:1}] run item modify entity @s weapon.mainhand {"function":"minecraft:set_name","entity":"this","target":"custom_name","name":{"text":"⚡ Pistolet M1911 (Pack-a-Punch)","color":"light_purple","bold":true,"italic":false}}
execute if items entity @s weapon.mainhand *[custom_data~{gun:1}] run scoreboard players set @s mg.g1 16
execute if items entity @s weapon.mainhand *[custom_data~{gun:2}] run item modify entity @s weapon.mainhand {"function":"minecraft:set_name","entity":"this","target":"custom_name","name":{"text":"⚡ Mitraillette MP5 (Pack-a-Punch)","color":"light_purple","bold":true,"italic":false}}
execute if items entity @s weapon.mainhand *[custom_data~{gun:2}] run scoreboard players set @s mg.g2 60
execute if items entity @s weapon.mainhand *[custom_data~{gun:3}] run item modify entity @s weapon.mainhand {"function":"minecraft:set_name","entity":"this","target":"custom_name","name":{"text":"⚡ Fusil à pompe (Pack-a-Punch)","color":"light_purple","bold":true,"italic":false}}
execute if items entity @s weapon.mainhand *[custom_data~{gun:3}] run scoreboard players set @s mg.g3 8
execute if items entity @s weapon.mainhand *[custom_data~{gun:4}] run item modify entity @s weapon.mainhand {"function":"minecraft:set_name","entity":"this","target":"custom_name","name":{"text":"⚡ Fusil M14 (Pack-a-Punch)","color":"light_purple","bold":true,"italic":false}}
execute if items entity @s weapon.mainhand *[custom_data~{gun:4}] run scoreboard players set @s mg.g4 20
execute if items entity @s weapon.mainhand *[custom_data~{gun:5}] run item modify entity @s weapon.mainhand {"function":"minecraft:set_name","entity":"this","target":"custom_name","name":{"text":"⚡ Sniper (Pack-a-Punch)","color":"light_purple","bold":true,"italic":false}}
execute if items entity @s weapon.mainhand *[custom_data~{gun:5}] run scoreboard players set @s mg.g5 10
execute if items entity @s weapon.mainhand *[custom_data~{gun:6}] run item modify entity @s weapon.mainhand {"function":"minecraft:set_name","entity":"this","target":"custom_name","name":{"text":"⚡ Ray Gun (Pack-a-Punch)","color":"light_purple","bold":true,"italic":false}}
execute if items entity @s weapon.mainhand *[custom_data~{gun:6}] run scoreboard players set @s mg.g6 40
execute if items entity @s weapon.mainhand *[custom_data~{gun:7}] run item modify entity @s weapon.mainhand {"function":"minecraft:set_name","entity":"this","target":"custom_name","name":{"text":"⚡ Mitrailleuse RPK (Pack-a-Punch)","color":"light_purple","bold":true,"italic":false}}
execute if items entity @s weapon.mainhand *[custom_data~{gun:7}] run scoreboard players set @s mg.g7 120
execute if items entity @s weapon.mainhand *[custom_data~{gun:8}] run item modify entity @s weapon.mainhand {"function":"minecraft:set_name","entity":"this","target":"custom_name","name":{"text":"⚡ Revolver Python (Pack-a-Punch)","color":"light_purple","bold":true,"italic":false}}
execute if items entity @s weapon.mainhand *[custom_data~{gun:8}] run scoreboard players set @s mg.g8 12
particle minecraft:witch ~ ~1.2 ~ 0.4 0.6 0.4 0.1 40
playsound minecraft:block.anvil.use player @a ~ ~ ~ 1 0.6
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 1 0.8
title @s actionbar {"text":"⚡ Pack-a-Punch : arme améliorée (dégâts ×3, chargeur ×2)","color":"light_purple","bold":true}
