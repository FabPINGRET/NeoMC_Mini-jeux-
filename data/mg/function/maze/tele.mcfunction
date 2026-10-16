# @s sur un téléporteur (marqueur le plus proche) : vers sa jumelle (0↔1, 2↔3, 4↔5)
scoreboard players operation $jx mg.st = @e[type=minecraft:marker,tag=mg.jtp,sort=nearest,limit=1] mg.jp
scoreboard players set #2 mg.st 2
scoreboard players operation $jy mg.st = $jx mg.st
scoreboard players operation $jy mg.st %= #2 mg.st
execute if score $jy mg.st matches 0 run scoreboard players add $jx mg.st 1
execute if score $jy mg.st matches 1 run scoreboard players remove $jx mg.st 1
execute as @e[type=minecraft:marker,tag=mg.jtp] if score @s mg.jp = $jx mg.st run tag @s add mg.jsel
tp @s @e[type=minecraft:marker,tag=mg.jsel,limit=1]
tag @e[tag=mg.jsel] remove mg.jsel
scoreboard players set @s mg.jc 60
execute at @s run particle minecraft:portal ~ ~1 ~ 0.4 0.8 0.4 0.5 60
execute at @s run playsound minecraft:entity.enderman.teleport master @a ~ ~ ~ 1 1.2
title @s actionbar {"text":"🌀 Téléporté !","color":"light_purple"}
