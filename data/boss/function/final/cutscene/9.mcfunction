tp @n[tag=wv_lord,tag=valor,distance=0..] -12364 123 355
tp @n[tag=wv_lord,tag=flame,distance=0..] -12364 123 354
tp @n[tag=wv_lord,tag=forest,distance=0..] -12364 123 356
tp @n[tag=wv_lord,tag=spores,distance=0..] -12364 123 353
tp @n[tag=wv_lord,tag=stone,distance=0..] -12364 121.6 357
tp @n[tag=wv_lord,tag=ice,distance=0..] -12364 123 352
tp @n[tag=wv_lord,tag=water,distance=0..] -12364 123 358

playsound minecraft:entity.shulker.teleport master @a[tag=mg.flw] -12364 123 355 2 1

execute as @e[tag=wv_lord,distance=0..] at @s facing -12359 122 355 run tp @s ~ ~ ~ ~ ~

schedule function floaty:sched/boss/final/cutscene/10 3s replace

#","color":"white"},{"text":"
