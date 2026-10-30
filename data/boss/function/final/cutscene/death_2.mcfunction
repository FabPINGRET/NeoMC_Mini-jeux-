tp @n[tag=wv_lord,tag=valor,distance=0..] -12384 123 360
tp @n[tag=wv_lord,tag=flame,distance=0..] -12388 123 358
tp @n[tag=wv_lord,tag=forest,distance=0..] -12380 123 358
tp @n[tag=wv_lord,tag=spores,distance=0..] -12389 123 354
tp @n[tag=wv_lord,tag=stone,distance=0..] -12379 121.6 354
tp @n[tag=wv_lord,tag=ice,distance=0..] -12387 123 350
tp @n[tag=wv_lord,tag=water,distance=0..] -12381 123 350

playsound minecraft:entity.shulker.teleport master @a[tag=mg.flw] -12384 123 355 2 1

execute as @e[tag=wv_lord,distance=0..] at @s facing -12384 123 355 run tp @s ~ ~ ~ ~ ~

schedule function floaty:sched/boss/final/cutscene/death_3 3s replace

#","color":"white"},{"text":"
