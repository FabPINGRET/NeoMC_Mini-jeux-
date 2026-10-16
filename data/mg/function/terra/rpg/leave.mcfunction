# @s quitte Terra Nova : bonus de vie retiré, monture renvoyée
attribute @s minecraft:max_health modifier remove mg:trlv
function mg:terra/rpg/mount_gone
scoreboard players set @s mg.trrg 0
function mg:terra/rpg/cl/remove
function mg:terra/rpg/cs/stop
function mg:terra/rpg/st/remove
