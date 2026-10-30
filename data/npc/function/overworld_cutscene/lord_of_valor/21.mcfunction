execute positioned 10029 95 -95 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute positioned 10029 95 -95 run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Stone","color":"gray"},{"text":"> Hero, we will need your help as well.","color":"white"},{"text":" Morbex ","color":"dark_aqua"},{"text":"is piloting his ","color":"white"},{"text":"machine","color":"dark_aqua"},{"text":" above the Dark Wilds. You should be able to ","color":"white"},{"text":"soar","color":"blue"},{"text":" and ","color":"white"},{"text":"glide ","color":"yellow"},{"text":"to it using powers you've obtained during your travels.","color":"white"},{"text":" ⇒","color":"light_purple"}]

execute as @n[tag=lord_of_valor,distance=0..] at @s facing 10029 95 -95 run tp @s ~ ~ ~ ~ 0

schedule function floaty:sched/npc/overworld_cutscene/lord_of_valor/22 13s replace
