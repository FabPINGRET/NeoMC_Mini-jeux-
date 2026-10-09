# @s : chasseur
clear @s
effect clear @s minecraft:invisibility
attribute @s minecraft:scale base set 1
item replace entity @s hotbar.0 with minecraft:warped_fungus_on_a_stick[custom_data={chm:10},item_model="mg:gun_raygun",custom_name={"text":"🔫 Lance-peinture","color":"red","bold":true,"italic":false},lore=[{"text":"Clic droit : tire (40 blocs). Touche un caméléon pour le trouver !","color":"gray","italic":false}],unbreakable={}]
item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=16711680,unbreakable={}]
item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=16711680,unbreakable={}]
effect give @s minecraft:saturation infinite 0 true
effect give @s minecraft:speed infinite 0 true
scoreboard players set @s mg.cmgc 0
scoreboard players set @s mg.cmq 0
