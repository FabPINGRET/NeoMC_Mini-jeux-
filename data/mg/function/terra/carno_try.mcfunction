# Une chance sur 90 par seconde : un carnotaure sauvage apparaît loin des colons
execute store result score $tvr mg.st run random value 0..89
execute unless score $tvr mg.st matches 0 run return 0
tag @e[tag=mg.trok] remove mg.trok
execute as @e[type=minecraft:marker,tag=mg.tvsp] at @s if entity @a[tag=mg.tvout,gamemode=adventure,distance=36..80] unless entity @a[tag=mg.tvw,distance=..30] run tag @s add mg.trok
execute as @e[tag=mg.trok,sort=random,limit=1] at @s run function mg:terra/carno_at
tag @e[tag=mg.trok] remove mg.trok
