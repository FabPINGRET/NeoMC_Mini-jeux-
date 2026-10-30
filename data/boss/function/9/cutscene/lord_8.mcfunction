execute as @n[tag=lord_of_water,distance=0..] at @s run particle minecraft:splash ~ ~1 ~ 0.4 0.8 0.4 0 150
execute as @n[tag=lord_of_water,distance=0..] at @s run particle minecraft:bubble_pop ~ ~1 ~ 0.4 0.8 0.4 0 150
execute as @n[tag=lord_of_water,distance=0..] at @s run playsound minecraft:ambient.underwater.enter master @a[tag=mg.flw] -11223 -20 -109 5 0.1

kill @n[tag=lord_of_water,distance=0..]
setblock -11239 -34 -132 air
setblock -11237 -34 -132 air

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/9/cutscene/lord_9 1.2s
