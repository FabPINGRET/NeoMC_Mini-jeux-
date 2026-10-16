# @s : 📡 localisateur (boussole) vers $(x) $(y) $(z) (macro), en case 9 de la barre
clear @s minecraft:compass[minecraft:custom_data~{tvloc:1b}]
$item replace entity @s hotbar.8 with minecraft:compass[custom_data={tvloc:1b},lodestone_tracker={target:{pos:[I;$(x),$(y),$(z)],dimension:"mg:terranova"},tracked:false},custom_name={"text":"📡 Localisateur","color":"aqua","italic":false,"bold":true},lore=[{"text":"Indique la colonie ou l’objectif de ta mission","color":"gray","italic":false}]]
$scoreboard players set @s mg.trox $(x)
$scoreboard players set @s mg.troy $(y)
$scoreboard players set @s mg.troz $(z)
scoreboard players set @s mg.tron 1
