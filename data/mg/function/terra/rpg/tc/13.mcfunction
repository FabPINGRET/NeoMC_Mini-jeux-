# @s ouvre le trésor caché n° 14 (s)
scoreboard players operation $b mg.st = @s mg.trtc
scoreboard players operation $b mg.st /= #p13 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run title @s actionbar {"text":"🗝 Déjà fouillé","color":"gray"}
scoreboard players operation @s mg.trtc += #p13 mg.st
scoreboard players add @s mg.tvc 450
scoreboard players add @s mg.trgr 6
function mg:terra/rpg/xp {n:360}
execute store result score $r mg.st run random value 1..3
execute if score $r mg.st matches 1 run scoreboard players add @s mg.trsp 1
title @s times 5 40 10
title @s title {"text":"🗝 TRÉSOR CACHÉ","color":"gold","bold":true}
title @s subtitle {"text":"+450 ₵, +6 griffes","color":"yellow"}
execute if score $r mg.st matches 1 run tellraw @s {"text":"  💎 et une gemme d'ambre : +1 point de caractéristique !","color":"light_purple"}
execute at @s run playsound minecraft:block.chest.open player @s ~ ~ ~ 1 0.8
execute at @s run particle minecraft:happy_villager ~ ~1 ~ 0.6 0.6 0.6 0 20
