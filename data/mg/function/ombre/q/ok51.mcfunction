# Étape 51 validée (isolde)
scoreboard players add @s mg.olg 3000
tellraw @s {"text":"  +3000 💰","color":"gold"}
function mg:ombre/xp {n:3000}
scoreboard players set @s mg.olat 9
function mg:ombre/kit
tellraw @a[tag=mg.olw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow","bold":true},{"text":" a sauvé Ombrelune !","color":"gold"}]
tellraw @s {"text":"🛡 Armure de l'Aube reçue (palier 9).","color":"gold"}
function mg:ombre/q/adv
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1
