# @s entre dans le portail de Neo City
execute unless data storage mg:gta built run return run function mg:gta/not_ready
execute if entity @s[tag=mg.mpp] run return run tellraw @s {"text":"⚠ Tu participes à la Mini Party : Neo GTA sera accessible après.","color":"red"}
function mg:lobkart/leave
function mg:parkour/quit
tag @s remove mg.inplot
tag @s remove mg.plabel
tag @s remove mg.visit
tag @s add mg.surv
tag @s add mg.gtw
execute if score $state mg.st matches 0 run scoreboard players reset @s mg.vc
execute if score $state mg.st matches 0 run function mg:vote/refresh
team leave @s
effect clear @s
clear @s
gamemode adventure @s
function mg:core/attr_reset
attribute @s minecraft:fall_damage_multiplier base set 1
function mg:gta/join
execute in mg:gta run spawnpoint @s 20 71 32297
execute in mg:gta run tp @s 20.5 71 32297.5 180 0
function mg:gta/kit
title @s times 10 50 20
title @s title {"text":"NEO GTA","color":"gold","bold":true}
title @s subtitle {"text":"Bienvenue en ville. Fais-toi un nom.","color":"gray"}
tellraw @s [{"text":"🚓 NEO GTA ","color":"gold","bold":true},{"text":"Armes sur les trottoirs, voitures et hélicos (clic droit pour monter), lunette du sniper en s'accroupissant. Passants et flics tués = ★ : la police débarque, de plus en plus nombreuse. Tes dollars sont gardés. ","color":"gray"},{"text":"Retour au lobby : panneau 🚪 près du carrefour de départ, ou menu (Échap → ≡ Menu).","color":"yellow"}]
execute at @s run playsound minecraft:block.portal.travel master @s ~ ~ ~ 0.3 1.6
