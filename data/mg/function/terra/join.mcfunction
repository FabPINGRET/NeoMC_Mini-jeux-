# @s : réglages d'arrivée (les crédits sont gardés d'une visite à l'autre)
execute unless score @s mg.tvpid matches 1.. run scoreboard players add $tvpn mg.st 1
execute unless score @s mg.tvpid matches 1.. run scoreboard players operation @s mg.tvpid = $tvpn mg.st
execute unless score @s mg.tvc matches -2147483648.. run scoreboard players set @s mg.tvc 0
function mg:terra/mis_clear
scoreboard players set @s mg.tvh 0
scoreboard players set @s mg.tvcd 0
scoreboard players set @s mg.tvsc 0
scoreboard players set @s mg.tvhm 0
scoreboard players set @s mg.tval 0
scoreboard players set @s mg.deaths 0
scoreboard players set @s mg.tvkr 0
scoreboard players set @s mg.tvkc 0
scoreboard players set @s mg.tvkb 0
scoreboard players set @s mg.tvkg 0
scoreboard players set @s mg.tvdd 0
scoreboard players reset @s mg.tvq
scoreboard players enable @s mg.tvms
tag @s remove mg.tvoh
tag @s remove mg.tvout
team add mg_tv
team modify mg_tv friendlyFire false
team modify mg_tv color dark_green
team join mg_tv @s
function mg:terra/rpg/join
