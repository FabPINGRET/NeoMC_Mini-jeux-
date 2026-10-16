# @s (carnotaure) : rugit et charge
scoreboard players set @s mg.tvat 12
tag @s add mg.tvroar
effect give @s minecraft:speed 3 2 true
playsound minecraft:entity.ravager.roar hostile @a ~ ~ ~ 2 0.7
damage @s 0.01 minecraft:generic by @p[tag=mg.tvw,gamemode=adventure,distance=..20]
