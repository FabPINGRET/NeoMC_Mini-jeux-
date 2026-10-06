# (@s = joueur visé, à sa position) : le boss apparaît dans son dos
scoreboard players set $tpd mg.st 0
execute at @e[tag=mg.boss,limit=1] run particle minecraft:large_smoke ~ ~1.5 ~ 0.5 1.2 0.5 0.05 30
tp @e[tag=mg.boss,limit=1] ^ ^ ^-2 facing entity @s eyes
execute at @e[tag=mg.boss,limit=1] run particle minecraft:large_smoke ~ ~1.5 ~ 0.5 1.2 0.5 0.05 30
playsound minecraft:entity.enderman.teleport master @a ~ ~ ~ 1 0.6
