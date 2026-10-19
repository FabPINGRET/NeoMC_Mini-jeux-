# @s ouvre le coffre caché n° 1 (w)
scoreboard players operation $b mg.st = @s mg.oltc
scoreboard players operation $b mg.st /= #p0 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run title @s actionbar {"text":"🗝 Déjà fouillé","color":"gray"}
scoreboard players operation @s mg.oltc += #p0 mg.st
scoreboard players add @s mg.olg 80
scoreboard players add @s mg.olm1 2
function mg:ombre/xp {n:60}
execute store result score $r mg.st run random value 1..3
execute if score $r mg.st matches 1 run scoreboard players add @s mg.olsp 1
title @s times 5 40 10
title @s title {"text":"🗝 COFFRE CACHÉ","color":"gold","bold":true}
title @s subtitle {"text":"+80 💰 et des matériaux","color":"yellow"}
execute if score $r mg.st matches 1 run tellraw @s {"text":"  💎 et une gemme de lune : +1 point de caractéristique !","color":"light_purple"}
execute at @s run playsound minecraft:block.chest.open player @s ~ ~ ~ 1 0.8
execute at @s run particle minecraft:happy_villager ~ ~1 ~ 0.6 0.6 0.6 0 20
