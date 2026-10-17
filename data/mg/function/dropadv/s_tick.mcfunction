# Dropper : Essais — chaque tick
scoreboard players add $dat mg.st 1
scoreboard players remove @a[tag=mg.play,scores={mg.cd=1..}] mg.cd 1
execute as @a[tag=mg.play,tag=!mg.ddone] at @s if block ~ ~ ~ minecraft:water run function mg:dropadv/s_success
execute as @a[tag=mg.play,tag=!mg.ddone] at @s if block ~ ~ ~ minecraft:lava run function mg:dropadv/s_fail
execute as @a[tag=mg.play,tag=!mg.ddone] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,tag=!mg.ddone,scores={mg.cd=0,mg.t=..298}] at @s if data entity @s {OnGround:1b} unless block ~ ~ ~ minecraft:water run function mg:dropadv/s_fail
execute as @a[tag=mg.play,tag=!mg.ddone,scores={mg.t=..36}] run function mg:dropadv/s_fail
scoreboard players operation $dam mg.st = $dat mg.st
scoreboard players operation $dam mg.st %= #k10 mg.st
execute if score $dam mg.st matches 0 as @a[tag=mg.play,tag=!mg.ddone] run function mg:dropadv/s_hud
function mg:dropadv/k_tick
execute if score $dat mg.st matches 36000.. run return run function mg:dropadv/s_end
execute unless entity @a[tag=mg.play] run return run function mg:core/draw
execute unless entity @a[tag=mg.play,tag=!mg.ddone] run function mg:dropadv/s_end
