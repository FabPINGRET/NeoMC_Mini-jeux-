# Fin du délai : échecs → tag mg.msk ; tout le monde a raté → tour annulé
tag @a[tag=mg.play] remove mg.msk
execute if score $msv mg.st matches 1 if score $mso mg.st matches 1..5 as @a[tag=mg.play,tag=!mg.mso] run tag @s add mg.msk
execute if score $mso mg.st matches 6 as @a[tag=mg.play,tag=mg.msf] run tag @s add mg.msk
execute if score $msv mg.st matches 0 as @a[tag=mg.play,tag=mg.msf] run tag @s add mg.msk
execute if score $mso mg.st matches 7 as @a[tag=mg.play] at @s unless block ~ ~-0.5 ~ minecraft:red_concrete run tag @s add mg.msk
execute if score $mso mg.st matches 8 as @a[tag=mg.play] at @s unless block ~ ~-0.5 ~ minecraft:blue_concrete run tag @s add mg.msk
execute if score $mso mg.st matches 9 as @a[tag=mg.play] at @s unless block ~ ~-0.5 ~ minecraft:lime_concrete run tag @s add mg.msk
execute if score $mso mg.st matches 10 as @a[tag=mg.play] at @s unless block ~ ~-0.5 ~ minecraft:yellow_concrete run tag @s add mg.msk
execute store result score $k mg.st if entity @a[tag=mg.msk]
execute store result score $a mg.st if entity @a[tag=mg.play]
scoreboard players set $msp mg.st 2
scoreboard players set $mst mg.st 30
execute if score $msv mg.st matches 0 if score $k mg.st matches 0 run title @a[tag=mg.play] actionbar {"text":"✔ Piège évité par tout le monde !","color":"green"}
execute if score $k mg.st matches 0 if score $msv mg.st matches 1 run title @a[tag=mg.play] actionbar {"text":"✔ Tout le monde a réussi","color":"green"}
execute if score $k mg.st matches 1.. if score $k mg.st = $a mg.st run return run function mg:master/void
execute if score $k mg.st matches 1.. as @a[tag=mg.msk] run function mg:master/ko
