# @s : dans l'arène, à un point au hasard (réapparition au même endroit)
execute unless score @s mg.pvid matches 1.. run scoreboard players add $pvidn mg.st 1
execute unless score @s mg.pvid matches 1.. run scoreboard players operation @s mg.pvid = $pvidn mg.st
tag @s add mg.pvpc
scoreboard players set @s mg.pks 0
scoreboard players set @s mg.phc 0
scoreboard players set @s mg.deaths 0
scoreboard players reset @s mg.pkc
execute unless score @s mg.pco matches 0.. run scoreboard players set @s mg.pco 0
scoreboard players enable @s mg.pshop
execute at @e[type=minecraft:marker,tag=mg.pvpsp,sort=random,limit=1] run tp @s ~ ~ ~ facing 13.5 44 12.5
execute at @s run spawnpoint @s ~ ~ ~
effect give @s minecraft:resistance 3 4 true
execute at @s run playsound minecraft:item.armor.equip_netherite master @s ~ ~ ~ 1 1
