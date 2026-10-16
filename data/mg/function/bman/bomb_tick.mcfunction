# @s : bombe (mg.yt = ticks avant l'explosion) ; devient un bloc solide dès que sa case est libre
scoreboard players remove @s mg.yt 1
execute if entity @s[tag=!mg.ys] positioned ~-0.5 ~ ~-0.5 unless entity @a[gamemode=!spectator,dx=0,dy=1,dz=0] positioned ~0.5 ~ ~0.5 run function mg:bman/solid
execute if score @s mg.yt matches ..0 run return run function mg:bman/boom
scoreboard players operation $yq2 mg.st = @s mg.yt
scoreboard players set #5 mg.st 5
scoreboard players operation $yq2 mg.st %= #5 mg.st
execute if score $yq2 mg.st matches 0 run particle minecraft:smoke ~ ~1.1 ~ 0.05 0.05 0.05 0.01 2
