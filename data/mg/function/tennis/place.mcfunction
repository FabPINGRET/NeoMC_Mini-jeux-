# Placement pour le point (court $tnk, $tnpar = parité des points) : en diagonale, derrière la ligne de fond
execute if score $tnk mg.st matches 1 if score $tnpar mg.st matches 0 as @e[tag=mg.tnk,scores={mg.tns=1}] run tp @s -58.0 65 35386.5 0 0
execute if score $tnk mg.st matches 1 if score $tnpar mg.st matches 0 as @e[tag=mg.tnk,scores={mg.tns=2}] run tp @s -61.0 65 35414.5 180 0
execute if score $tnk mg.st matches 1 if score $tnpar mg.st matches 1 as @e[tag=mg.tnk,scores={mg.tns=1}] run tp @s -61.0 65 35386.5 0 0
execute if score $tnk mg.st matches 1 if score $tnpar mg.st matches 1 as @e[tag=mg.tnk,scores={mg.tns=2}] run tp @s -58.0 65 35414.5 180 0
execute if score $tnk mg.st matches 2 if score $tnpar mg.st matches 0 as @e[tag=mg.tnk,scores={mg.tns=1}] run tp @s -18.0 65 35386.5 0 0
execute if score $tnk mg.st matches 2 if score $tnpar mg.st matches 0 as @e[tag=mg.tnk,scores={mg.tns=2}] run tp @s -21.0 65 35414.5 180 0
execute if score $tnk mg.st matches 2 if score $tnpar mg.st matches 1 as @e[tag=mg.tnk,scores={mg.tns=1}] run tp @s -21.0 65 35386.5 0 0
execute if score $tnk mg.st matches 2 if score $tnpar mg.st matches 1 as @e[tag=mg.tnk,scores={mg.tns=2}] run tp @s -18.0 65 35414.5 180 0
execute if score $tnk mg.st matches 3 if score $tnpar mg.st matches 0 as @e[tag=mg.tnk,scores={mg.tns=1}] run tp @s 22.0 65 35386.5 0 0
execute if score $tnk mg.st matches 3 if score $tnpar mg.st matches 0 as @e[tag=mg.tnk,scores={mg.tns=2}] run tp @s 19.0 65 35414.5 180 0
execute if score $tnk mg.st matches 3 if score $tnpar mg.st matches 1 as @e[tag=mg.tnk,scores={mg.tns=1}] run tp @s 19.0 65 35386.5 0 0
execute if score $tnk mg.st matches 3 if score $tnpar mg.st matches 1 as @e[tag=mg.tnk,scores={mg.tns=2}] run tp @s 22.0 65 35414.5 180 0
execute if score $tnk mg.st matches 4 if score $tnpar mg.st matches 0 as @e[tag=mg.tnk,scores={mg.tns=1}] run tp @s 62.0 65 35386.5 0 0
execute if score $tnk mg.st matches 4 if score $tnpar mg.st matches 0 as @e[tag=mg.tnk,scores={mg.tns=2}] run tp @s 59.0 65 35414.5 180 0
execute if score $tnk mg.st matches 4 if score $tnpar mg.st matches 1 as @e[tag=mg.tnk,scores={mg.tns=1}] run tp @s 59.0 65 35386.5 0 0
execute if score $tnk mg.st matches 4 if score $tnpar mg.st matches 1 as @e[tag=mg.tnk,scores={mg.tns=2}] run tp @s 62.0 65 35414.5 180 0
