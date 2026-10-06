# Onde de choc (@s = boss, à sa position) : joueurs à moins de 13 blocs repoussés de 4,5 blocs + dégâts
particle minecraft:explosion_emitter ~ ~1 ~
particle minecraft:lava ~ ~1 ~ 5 0.5 5 0 60
playsound minecraft:entity.generic.explode master @a ~ ~ ~ 1.5 0.6
execute as @a[tag=mg.play,distance=..13] at @s facing entity @e[tag=mg.boss,limit=1] feet rotated ~ 0 run tp @s ^ ^0.4 ^-4.5
execute as @a[tag=mg.play,distance=..13] run damage @s 5 minecraft:explosion
