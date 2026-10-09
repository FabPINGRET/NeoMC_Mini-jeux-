# Coffres vidés : 1 500 à 2 500 $, banque fermée 7 min
scoreboard players set @s mg.grob 0
execute store result score $gcv mg.st run random value 1500..2500
function mg:gta/cash_gain
scoreboard players set @e[type=minecraft:marker,tag=mg.gbank] mg.gpc 8400
execute as @e[type=minecraft:text_display,tag=mg.gbkl] run data merge entity @s {text:{"text":"🔒 Coffres vides","color":"red","bold":true}}
function mg:gta/wanted_up
title @s title {"text":"💰 JACKPOT","color":"gold","bold":true}
tellraw @a[tag=mg.gtw] [{"text":"💰 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a vidé les coffres de la banque : ","color":"gold"},{"score":{"name":"$gcv","objective":"mg.st"},"color":"green","bold":true},{"text":" $ !","color":"gold"}]
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1
