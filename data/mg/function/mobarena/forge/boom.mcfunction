particle minecraft:explosion_emitter ~ ~ ~
particle minecraft:lava ~ ~1 ~ 1.5 0.5 1.5 0 25
playsound minecraft:entity.generic.explode master @a ~ ~ ~ 1 1.2
execute as @a[tag=mg.play,distance=..3.6] run damage @s 6 minecraft:explosion
setblock ~ ~ ~ minecraft:fire
