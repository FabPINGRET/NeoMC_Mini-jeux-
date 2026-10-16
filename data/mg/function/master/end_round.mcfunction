# Fin du délai : échecs → tag mg.msk ; tout le monde a raté → tour annulé
tag @a[tag=mg.play] remove mg.msk
tag @a[tag=mg.play,tag=!mg.mso,scores={mg.mo=1..5,mg.mv=1}] add mg.msk
tag @a[tag=mg.play,tag=mg.msf,scores={mg.mo=6}] add mg.msk
tag @a[tag=mg.play,tag=mg.msf,scores={mg.mv=0}] add mg.msk
execute as @a[tag=mg.play,scores={mg.mo=7}] at @s unless block ~ ~-0.5 ~ minecraft:red_concrete run tag @s add mg.msk
execute as @a[tag=mg.play,scores={mg.mo=8}] at @s unless block ~ ~-0.5 ~ minecraft:blue_concrete run tag @s add mg.msk
execute as @a[tag=mg.play,scores={mg.mo=9}] at @s unless block ~ ~-0.5 ~ minecraft:lime_concrete run tag @s add mg.msk
execute as @a[tag=mg.play,scores={mg.mo=10}] at @s unless block ~ ~-0.5 ~ minecraft:yellow_concrete run tag @s add mg.msk
execute store result score $k mg.st if entity @a[tag=mg.msk]
execute store result score $a mg.st if entity @a[tag=mg.play]
scoreboard players set $msp mg.st 2
scoreboard players set $mst mg.st 30
execute if score $msx mg.st matches 1 run tellraw @a[tag=mg.play] {"text":"🔀 Ce tour-ci, chacun avait sa propre consigne !","color":"light_purple","bold":true}
execute if score $msx mg.st matches 0 if score $msv mg.st matches 0 if score $k mg.st matches 0 run title @a[tag=mg.play] actionbar {"text":"✔ Piège évité par tout le monde !","color":"green"}
execute if score $k mg.st matches 0 if score $msx mg.st matches 0 if score $msv mg.st matches 1 run title @a[tag=mg.play] actionbar {"text":"✔ Tout le monde a réussi","color":"green"}
execute if score $k mg.st matches 0 if score $msx mg.st matches 1 run title @a[tag=mg.play] actionbar {"text":"✔ Tout le monde a réussi","color":"green"}
execute if score $k mg.st matches 1.. if score $k mg.st = $a mg.st run return run function mg:master/void
execute if score $k mg.st matches 1.. as @a[tag=mg.msk] run function mg:master/ko
