# Succès : Chasseur
scoreboard players operation $b mg.st = @s mg.trac
scoreboard players operation $b mg.st /= #p1 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.trac += #p1 mg.st
function mg:terra/rpg/xp {n:200}
tellraw @a[tag=mg.tvw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" obtient le titre ","color":"gray"},{"text":"« Chasseur »","color":"gold","bold":true},{"text":" (Abattre 50 monstres)","color":"dark_gray"}]
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.3
