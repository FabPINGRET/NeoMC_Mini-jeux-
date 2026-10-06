# @s = joueur touché par une boule de neige du lobby : 1 cœur de dégâts (jamais mortel)
scoreboard players set $snh mg.st 1
execute at @s run particle minecraft:snowflake ~ ~1 ~ 0.3 0.4 0.3 0.05 20
execute at @s run playsound minecraft:entity.player.hurt_freeze master @a ~ ~ ~ 1 1.2
execute if score @s mg.hp matches 3.. run damage @s 2 minecraft:thrown
