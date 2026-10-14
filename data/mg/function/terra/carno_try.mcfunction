# Une chance sur 90 par seconde : un carnotaure sauvage apparaît loin des colons
execute store result score $tvr mg.st run random value 0..89
execute unless score $tvr mg.st matches 0 run return 0
scoreboard players set $tvf mg.st 0
execute as @e[type=minecraft:marker,tag=mg.tvsp,sort=random] at @s if score $tvf mg.st matches 0 if entity @a[tag=mg.tvout,gamemode=adventure,distance=36..80] unless entity @a[tag=mg.tvw,distance=..30] run function mg:terra/carno_at
