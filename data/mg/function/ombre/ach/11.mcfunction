# Succès : Légende
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p11 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.olac += #p11 mg.st
function mg:ombre/xp {n:2000}
tellraw @a[tag=mg.olw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" obtient le titre ","color":"gray"},{"text":"« Légende »","color":"gold","bold":true},{"text":" (Atteindre le niveau 35)","color":"dark_gray"}]
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.3
