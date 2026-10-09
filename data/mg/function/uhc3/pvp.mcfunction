# PvP activé, la zone commence à rétrécir
team leave @a[tag=mg.play]
title @a[tag=mg.play] title {"text":"⚔ PvP !","color":"red","bold":true}
title @a[tag=mg.play] subtitle {"text":"la zone rétrécit vers le centre","color":"gray"}
execute as @a[tag=mg.play] at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.6 1.2
