# Succès : Légende vivante
scoreboard players operation $b mg.st = @s mg.trac
scoreboard players operation $b mg.st /= #p10 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.trac += #p10 mg.st
function mg:terra/rpg/xp {n:1000}
tellraw @a[tag=mg.tvw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" obtient le titre ","color":"gray"},{"text":"« Légende vivante »","color":"gold","bold":true},{"text":" (Atteindre le niveau 20)","color":"dark_gray"}]
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.3
