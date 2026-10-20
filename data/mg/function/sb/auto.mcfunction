# 📊 Tableau de droite hors mini-jeu : celui de l'endroit où sont le plus de joueurs (généré : tools/lobby/gen_sidebar.py)
execute unless score $state mg.st matches 0 run return run scoreboard players set $sbm mg.st -1
execute if score $sbo mg.st matches 1 unless score $sbm mg.st matches 9 run scoreboard objectives setdisplay sidebar
execute if score $sbo mg.st matches 1 run return run scoreboard players set $sbm mg.st 9
execute store result score $sbc0 mg.st if entity @a[tag=!mg.surv]
execute store result score $sbc1 mg.st if entity @a[tag=mg.gtw]
execute store result score $sbc2 mg.st if entity @a[tag=mg.tvw]
execute store result score $sbc3 mg.st if entity @a[tag=mg.surv,tag=!mg.gtw,tag=!mg.tvw,tag=!mg.olw]
scoreboard players set $sbn mg.st 0
scoreboard players operation $sbx mg.st = $sbc0 mg.st
execute if score $sbc1 mg.st > $sbx mg.st run scoreboard players set $sbn mg.st 1
execute if score $sbc1 mg.st > $sbx mg.st run scoreboard players operation $sbx mg.st = $sbc1 mg.st
execute if score $sbc2 mg.st > $sbx mg.st run scoreboard players set $sbn mg.st 2
execute if score $sbc2 mg.st > $sbx mg.st run scoreboard players operation $sbx mg.st = $sbc2 mg.st
execute if score $sbc3 mg.st > $sbx mg.st run scoreboard players set $sbn mg.st 3
execute if score $sbn mg.st matches 3 as @a[tag=mg.surv,tag=!mg.gtw,tag=!mg.tvw,tag=!mg.olw] store result score @s mg.svl run experience query @s levels
execute if score $sbn mg.st matches 0 unless score $sbm mg.st matches 0 run scoreboard players set $hrt mg.st 0
execute if score $sbn mg.st matches 1 run scoreboard objectives setdisplay sidebar mg.gta
execute if score $sbn mg.st matches 2 run scoreboard objectives setdisplay sidebar mg.tvc
execute if score $sbn mg.st matches 3 run scoreboard objectives setdisplay sidebar mg.svl
scoreboard players operation $sbm mg.st = $sbn mg.st
