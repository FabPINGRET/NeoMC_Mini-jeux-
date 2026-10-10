advancement revoke @s only mg:pvpc_home
item replace entity @s hotbar.8 with minecraft:recovery_compass[custom_data={pvpc_home:1b},consumable={consume_seconds:0.05f,animation:"none",sound:"minecraft:ui.button.click",has_consume_particles:false},custom_name=[{"text":"🏠 Retour au spawn","color":"yellow","bold":true,"italic":false}],lore=[[{"text":"Clic droit : 5 s sans prendre de coup","color":"gray","italic":false}]]]
execute unless entity @s[tag=mg.pvpc] run return 0
execute if score @s mg.phc matches 1.. run return 0
scoreboard players set @s mg.phc 100
scoreboard players set @s mg.pdt 0
tellraw @s {"text":"🏠 Retour au spawn dans 5 s… ne prends pas de coup !","color":"yellow"}
