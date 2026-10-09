# @s : réglages d'arrivée (les dollars sont gardés d'une visite à l'autre)
tag @s add mg.gtg
execute unless score @s mg.gta matches -2147483648.. run scoreboard players set @s mg.gta 0
scoreboard players set @s mg.gwl 0
scoreboard players set @s mg.gwt 0
scoreboard players set @s mg.grk 0
scoreboard players add $bidn mg.st 1
scoreboard players operation @s mg.bid = $bidn mg.st
scoreboard players reset @s mg.gkp
scoreboard players reset @s mg.gkv
scoreboard players reset @s mg.gks
scoreboard players reset @s mg.gkw
scoreboard players reset @s mg.gqs
scoreboard players set @s mg.deaths 0
function mg:gun/reset
scoreboard players set @s mg.gtl 0
scoreboard players set @s mg.gal 0
tag @s remove mg.gdrv
team join mg_gciv @s
