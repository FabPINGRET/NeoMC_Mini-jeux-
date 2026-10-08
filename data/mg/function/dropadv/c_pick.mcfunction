# Nouveau niveau au hasard (jamais deux fois de suite le même)
scoreboard players operation $dcp mg.st = $dcl mg.st
execute store result score $dcl mg.st run random value 1..10
execute if score $dcl mg.st = $dcp mg.st run scoreboard players add $dcl mg.st 1
execute if score $dcl mg.st matches 11.. run scoreboard players set $dcl mg.st 1
scoreboard players add $dcr mg.st 1
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 303
scoreboard players set $pz mg.st 23989
