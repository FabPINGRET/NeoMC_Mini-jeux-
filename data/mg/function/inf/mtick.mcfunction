# Toutes les 2 s : un zombie de plus tant qu'on est sous le plafond (6 + 3 par survivant, 30 max) ; plus rapide après 90 s
scoreboard players add $imc mg.st 1
execute store result score $imz mg.st if entity @e[type=minecraft:zombie,tag=mg.zz]
scoreboard players operation $imx mg.st = $ins mg.st
scoreboard players operation $imx mg.st *= #3 mg.st
scoreboard players add $imx mg.st 6
execute if score $imx mg.st matches 31.. run scoreboard players set $imx mg.st 30
execute if score $ift mg.st matches 1800.. if score $imc mg.st matches 20.. if score $imz mg.st < $imx mg.st run function mg:inf/mspawn
execute if score $imc mg.st matches 40.. if score $imz mg.st < $imx mg.st run function mg:inf/mspawn
execute if score $imc mg.st matches 40.. run scoreboard players set $imc mg.st 0
