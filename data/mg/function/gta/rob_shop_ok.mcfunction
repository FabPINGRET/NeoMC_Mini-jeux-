# Caisse vidée : 200 à 450 $, deux étoiles, commerce fermé 3 min
scoreboard players set @s mg.grob 0
execute store result score $gcv mg.st run random value 200..450
function mg:gta/cash_gain
execute as @e[type=minecraft:marker,tag=mg.gshop,distance=..2.6,limit=1,sort=nearest] run function mg:gta/shop_close
function mg:gta/wanted_up
function mg:gta/wanted_up
title @s title {"text":" ","color":"gold"}
title @s subtitle {"text":"💰 Caisse vidée !","color":"gold","bold":true}
