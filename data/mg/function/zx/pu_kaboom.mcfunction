execute as @e[tag=mg.zz] at @s run particle minecraft:explosion ~ ~1 ~ 0.3 0.3 0.3 0 2 force
kill @e[tag=mg.zz]
scoreboard players add @a[tag=mg.play] mg.zpt 400
effect give @a[tag=mg.play] minecraft:blindness 1 0 true
execute as @a[tag=mg.play] at @s run playsound minecraft:entity.generic.explode master @s ~ ~ ~ 1 0.6
