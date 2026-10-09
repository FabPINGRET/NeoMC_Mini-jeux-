# @s réussit sa mission : récompense
scoreboard players set $gcv mg.st 0
execute if score @s mg.gmt matches 1 run scoreboard players set $gcv mg.st 300
execute if score @s mg.gmt matches 2 run scoreboard players set $gcv mg.st 500
execute if score @s mg.gmt matches 3 run scoreboard players set $gcv mg.st 400
scoreboard players operation @s mg.gta += $gcv mg.st
function mg:gta/mis_clean
title @s times 5 50 15
title @s title {"text":"MISSION RÉUSSIE","color":"gold","bold":true}
title @s subtitle [{"text":"+","color":"green"},{"score":{"name":"$gcv","objective":"mg.st"},"color":"green","bold":true},{"text":" $","color":"green"}]
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1
scoreboard players set @s mg.gtl 60
