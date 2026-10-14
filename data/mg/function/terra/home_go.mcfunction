# @s : de retour sur la place de la colonie
tp @s 0.5 65 4.5
execute at @s run playsound minecraft:entity.enderman.teleport player @a ~ ~ ~ 0.6 1.2
execute at @s run particle minecraft:reverse_portal ~ ~1 ~ 0.4 0.8 0.4 0.05 40
