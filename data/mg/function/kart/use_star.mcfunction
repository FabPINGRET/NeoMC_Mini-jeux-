scoreboard players set @s mg.kst 160
effect give @s minecraft:glowing 8 0 true
execute at @s run playsound minecraft:entity.player.levelup master @a[tag=mg.play,distance=..24] ~ ~ ~ 1 1.6
title @s actionbar [{"text":"⭐ Invincible !","color":"yellow","bold":true}]
