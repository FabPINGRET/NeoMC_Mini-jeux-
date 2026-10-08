# Toutes les 15 s : 3 charges de vent
scoreboard players set $skwt mg.st 0
clear @a[tag=mg.play] minecraft:wind_charge[minecraft:custom_data~{mg_sky:1b}]
give @a[tag=mg.play] minecraft:wind_charge[minecraft:custom_data={mg_sky:1b},minecraft:custom_name={"text":"Charge de vent","color":"aqua","italic":false}] 3
execute as @a[tag=mg.play] at @s run playsound minecraft:item.armor.equip_elytra master @s ~ ~ ~ 0.6 1.6
