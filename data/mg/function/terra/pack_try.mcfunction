# Une meute sur un point d'apparition entre 24 et 64 blocs d'un colon (aucun à moins de 22)
scoreboard players set $tvpk mg.st 8
scoreboard players set $tvf mg.st 0
execute as @e[type=minecraft:marker,tag=mg.tvsp,sort=random] at @s if score $tvf mg.st matches 0 if entity @a[tag=mg.tvout,gamemode=adventure,distance=24..64] unless entity @a[tag=mg.tvw,distance=..22] run function mg:terra/pack_at
