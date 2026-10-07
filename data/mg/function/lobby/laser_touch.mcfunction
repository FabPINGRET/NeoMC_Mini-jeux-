# Joueur touché par le railgun (@s = joueur touché) : 1 cœur de dégâts, jamais mortel
effect give @s minecraft:glowing 2 0 true
execute at @s run particle minecraft:electric_spark ~ ~1 ~ 0.3 0.5 0.3 0.45 30
execute at @s run particle minecraft:dust{color:[1.0,0.15,0.15],scale:1.6} ~ ~1 ~ 0.3 0.5 0.3 0 20
execute at @s run particle minecraft:explosion ~ ~1 ~ 0 0 0 0 1
execute if score @s mg.hp matches 3.. run damage @s 2 minecraft:generic
execute unless score @s mg.hp matches 3.. at @s run playsound minecraft:entity.player.hurt master @a ~ ~ ~ 1 1.2
execute at @s run playsound minecraft:block.respawn_anchor.deplete master @a ~ ~ ~ 0.8 1.8
execute as @a[tag=mg.lsr] at @s run playsound minecraft:entity.arrow.hit_player master @s ~ ~ ~ 1 1.2
title @a[tag=mg.lsr] actionbar [{"text":"✔ Touché !","color":"green","bold":true}]
title @s actionbar [{"text":"⚡ Touché par un railgun ! (-1 ❤)","color":"red"}]
