# @s : 📍 localisateur (boussole) vers $(x) $(y) $(z), en case 9
clear @s minecraft:compass[minecraft:custom_data~{olloc:1b}]
$item replace entity @s hotbar.8 with minecraft:compass[custom_data={olloc:1b},lodestone_tracker={target:{pos:[I;$(x),$(y),$(z)],dimension:"mg:ombrelune"},tracked:false},custom_name={"text":"📍 Localisateur","color":"light_purple","italic":false,"bold":true},lore=[{"text":"Indique ton objectif (faisceau violet)","color":"gray","italic":false}]]
$scoreboard players set @s mg.olox $(x)
$scoreboard players set @s mg.oloy $(y)
$scoreboard players set @s mg.oloz $(z)
scoreboard players set @s mg.olon 1
