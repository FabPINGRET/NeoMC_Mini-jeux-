# Fin de l'étourdissement (@s) : élytres rendues
tag @s remove mg.skstun
scoreboard players set @s mg.skst 0
execute unless entity @s[tag=mg.play] run return 0
item replace entity @s armor.chest with minecraft:elytra[minecraft:custom_data={mg_sky:1b},minecraft:unbreakable={},minecraft:enchantments={"minecraft:binding_curse":1},minecraft:custom_name={"text":"Élytres du ciel","color":"aqua","italic":false}]
scoreboard players set @s mg.skg -30
title @s subtitle [{"text":"Élytres rendues : appuie sur Espace !","color":"yellow","bold":true}]
title @s title [{"text":" "}]
playsound minecraft:item.armor.equip_elytra master @s ~ ~ ~ 1 1.2
