# Succès : Porteur de l'Aube
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p10 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.olac += #p10 mg.st
function mg:ombre/xp {n:2000}
tellraw @a[tag=mg.olw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" obtient le titre ","color":"gray"},{"text":"« Porteur de l'Aube »","color":"gold","bold":true},{"text":" (Terminer la campagne)","color":"dark_gray"}]
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.3
