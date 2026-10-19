# @s entre dans le portail d'Ombrelune (contexte : monde des mini-jeux)
execute unless data storage mg:ombre built run return run function mg:ombre/not_ready
execute if entity @s[tag=mg.mpp] run return run tellraw @s {"text":"⚠ Tu participes à la Mini Party : Ombrelune sera accessible après.","color":"red"}
function mg:lobkart/leave
function mg:parkour/quit
tag @s remove mg.inplot
tag @s remove mg.plabel
tag @s remove mg.visit
tag @s add mg.surv
tag @s add mg.olw
execute if score $state mg.st matches 0 run scoreboard players reset @s mg.vc
execute if score $state mg.st matches 0 run function mg:vote/refresh
team leave @s
effect clear @s
clear @s
gamemode adventure @s
function mg:core/attr_reset
attribute @s minecraft:fall_damage_multiplier base set 1
function mg:ombre/join
function mg:core/heal
execute in mg:ombrelune run spawnpoint @s 6 65 7
execute in mg:ombrelune run tp @s 0.5 65 9.5 180 0
function mg:ombre/kit
scoreboard players operation @s mg.olmp = @s mg.olmm
function mg:ombre/mana_bar
title @s times 10 60 20
title @s title {"text":"OMBRELUNE","color":"light_purple","bold":true}
title @s subtitle {"text":"Le royaume du crépuscule éternel","color":"gray"}
tellraw @s [{"text":"🌙 OMBRELUNE","color":"light_purple","bold":true},{"text":" : bienvenue à Havreclair, voyageur !","color":"yellow"}]
tellraw @s [{"text":" 📖 Journal (case 8) : ","color":"gold"},{"text":"quête, caractéristiques, bestiaire, voyage","color":"gray"}]
tellraw @s [{"text":" ✦ Mana : ","color":"aqua"},{"text":"la barre d'XP. Compétences en cases 3 à 6 (clic droit).","color":"gray"}]
tellraw @s [{"text":" 🌀 Pierres d'appel : ","color":"light_purple"},{"text":"voyage entre les régions. Sortir : pierre de la place ou Échap → ≡ Menu","color":"gray"}]
execute if score @s mg.olch matches 1.. run function mg:ombre/q/say
function mg:ombre/qloc
execute at @s run playsound minecraft:block.portal.travel master @s ~ ~ ~ 0.3 1.6
