# @s est mort (contexte : dimension mg:gta) : WASTED, ou BUSTED s'il était recherché ; -25 % lâchés en liasse
scoreboard players set @s mg.deaths 0
scoreboard players set @s mg.gtl 60
scoreboard players operation $gl mg.st = @s mg.gta
scoreboard players set #4 mg.st 4
scoreboard players operation $gl mg.st /= #4 mg.st
scoreboard players operation @s mg.gta -= $gl mg.st
title @s times 5 45 15
execute if score @s mg.gwl matches 1.. run title @s title {"text":"BUSTED","color":"#4A7BD8","bold":true}
execute if score @s mg.gwl matches 1.. run title @s subtitle [{"text":"-","color":"#4A7BD8"},{"score":{"name":"$gl","objective":"mg.st"},"color":"#4A7BD8"},{"text":" $ (caution)","color":"gray"}]
execute unless score @s mg.gwl matches 1.. run title @s title {"text":"WASTED","color":"#C8102E","bold":true}
execute unless score @s mg.gwl matches 1.. run title @s subtitle [{"text":"-","color":"#C8102E"},{"score":{"name":"$gl","objective":"mg.st"},"color":"#C8102E"},{"text":" $ (frais d'hôpital)","color":"gray"}]
scoreboard players set @s mg.gwl 0
scoreboard players set @s mg.gwt 0
team join mg_gciv @s
execute if score $gl mg.st matches 1.. run function mg:gta/drop_cash
function mg:gta/radio_off
function mg:gta/unscope
function mg:gta/place
function mg:gta/kit
execute at @s run playsound minecraft:entity.wither.death player @s ~ ~ ~ 0.4 1.6
execute at @s run playsound minecraft:block.bell.resonate player @s ~ ~ ~ 0.8 0.5
