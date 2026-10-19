# Construction d'Ombrelune (ou reconstruction complète, ~3 min)
scoreboard players set $olb mg.st 0
scoreboard players set $olrl mg.st 0
scoreboard players set $olrr mg.st 0
data remove storage mg:ombre q
execute in mg:ombrelune run forceload remove all
schedule function mg:ombre/wb_step 20t
tellraw @a[tag=mg.admin] {"text":"🌙 Construction de la carte d'Ombrelune lancée (~3 min).","color":"light_purple"}
