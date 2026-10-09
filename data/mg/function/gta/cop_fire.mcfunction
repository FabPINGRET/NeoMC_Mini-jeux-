# @s (policier) : tire sur le joueur recherché le plus proche s'il le voit (une chance sur trois toutes les 0,5 s)
execute store result score $gr mg.st run random value 0..3
execute if score $gr mg.st matches 1.. run return 0
tag @s add mg.gcsh
scoreboard players set $gcd2 mg.st 2
execute if entity @s[tag=mg.gswat] run scoreboard players set $gcd2 mg.st 3
execute store result storage mg:gta s.a int 1 run random value -6..6
execute store result storage mg:gta s.b int 1 run random value -4..4
execute if entity @s[tag=mg.gswat] store result storage mg:gta s.a int 1 run random value -4..4
scoreboard players set $gcr mg.st 56
function mg:gta/cop_shot with storage mg:gta s
tag @s remove mg.gcsh
playsound minecraft:entity.firework_rocket.blast hostile @a ~ ~ ~ 1.6 1.7
execute anchored eyes positioned ^-0.3 ^-0.2 ^0.8 run particle minecraft:small_flame ~ ~ ~ 0.02 0.02 0.02 0 3
