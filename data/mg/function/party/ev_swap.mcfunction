# Échange des pièces de @s avec un adversaire tiré au sort
execute as @a[tag=mg.mpp,tag=mg.play,tag=!mg.mpcur,sort=random,limit=1] run tag @s add mg.mpsw
execute unless entity @a[tag=mg.mpsw] run scoreboard players add @s mg.mpm 5
execute unless entity @a[tag=mg.mpsw] run return run tellraw @a[tag=mg.mpp] [{"text":"★ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" : ? échange, mais personne en face : ","color":"gray"},{"text":"+5 pièces","color":"gold"}]
scoreboard players operation $tmp mg.st = @s mg.mpm
scoreboard players operation @s mg.mpm = @a[tag=mg.mpsw,limit=1] mg.mpm
scoreboard players operation @a[tag=mg.mpsw] mg.mpm = $tmp mg.st
tellraw @a[tag=mg.mpp] [{"text":"★ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" : ? échange ses pièces avec ","color":"gray"},{"selector":"@a[tag=mg.mpsw]","color":"yellow"}]
tag @a remove mg.mpsw
