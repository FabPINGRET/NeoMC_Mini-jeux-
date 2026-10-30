fill -12389 123 350 -12379 134 360 light[level=15] replace copper_ore
fill -12389 123 350 -12379 134 360 light[level=15] replace deepslate_copper_ore
fill -12389 123 350 -12379 134 360 light[level=15] replace cyan_stained_glass

execute as @n[tag=wv_center,distance=0..] at @s run particle block{block_state:"cyan_stained_glass"} ~ ~ ~ 2 2 2 0 200

execute as @n[tag=wv_lord,tag=valor,distance=0..] at @s run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2 1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Valor","color":"yellow"},{"text":"> Yes! Just one more shot, straight to his core!","color":"white"}]

scoreboard players set wv_one_left bool 1

function boss:final/arena/reset_light

bossbar set boss:final color red
