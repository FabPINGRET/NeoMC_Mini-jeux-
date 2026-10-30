particle minecraft:explosion ~ ~1.5 ~
playsound minecraft:block.vine.break master @a[tag=mg.flw] ~ ~ ~ 1 1
playsound minecraft:block.grass.break master @a[tag=mg.flw] ~ ~ ~ 1 1
execute as @a[gamemode=!spectator,distance=..1,tag=mg.flw] run damage @s 14 minecraft:cactus
execute positioned ~ ~1 ~ as @a[gamemode=!spectator,distance=..1,tag=mg.flw] run damage @s 14 minecraft:cactus
execute positioned ~ ~-1 ~ as @a[gamemode=!spectator,distance=..1,tag=mg.flw] run damage @s 14 minecraft:cactus

kill @s
