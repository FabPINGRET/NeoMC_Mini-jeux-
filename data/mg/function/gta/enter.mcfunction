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
title @s subtitle {"text":"Deviens le plus riche de Neo City","color":"gray"}
tellraw @s [{"text":"🚓 NEO GTA","color":"gold","bold":true},{"text":" : deviens le plus riche de la ville","color":"yellow"}]
tellraw @s [{"text":" 💵 Gagner : ","color":"green"},{"text":"accroupi + arme en main pour braquer passants, commerces, banque ; missions au 📱","color":"gray"}]
tellraw @s [{"text":" 🔫 Dépenser : ","color":"aqua"},{"text":"armurerie et concession au parc, tout ce qui est acheté est gratuit à la villa","color":"gray"}]
tellraw @s [{"text":" ★ Police : ","color":"red"},{"text":"chaque crime = étoile, une de moins toutes les 15 s","color":"gray"}]
tellraw @s [{"text":" 🚪 Sortir : ","color":"yellow"},{"text":"Échap → ≡ Menu","color":"gray"}]
execute at @s run playsound minecraft:block.portal.travel master @s ~ ~ ~ 0.3 1.6
