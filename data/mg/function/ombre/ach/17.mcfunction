# Succès : Encyclopédiste
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p17 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.olac += #p17 mg.st
function mg:ombre/xp {n:1500}
tellraw @a[tag=mg.olw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" obtient le titre ","color":"gray"},{"text":"« Encyclopédiste »","color":"gold","bold":true},{"text":" (Compléter le bestiaire)","color":"dark_gray"}]
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.3
