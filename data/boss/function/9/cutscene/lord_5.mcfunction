playsound minecraft:entity.drowned.ambient_water neutral @s -11223 -18 -109 5 2
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Water","color":"blue"},{"text":"> Is that so? I retreated here because we thought it would be safe, but the","color":"white"},{"text":" Virus","color":"dark_aqua"},{"text":" somehow knew where to find me.","color":"white"},{"text":" ⇒","color":"light_purple"}]

data modify entity @n[tag=lord_of_water,distance=0..] Pose.Head set value [0f,0f,0f]
setblock -11239 -34 -132 minecraft:redstone_block

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/9/cutscene/lord_6 9s
