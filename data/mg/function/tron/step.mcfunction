# @s = joueur : porteur (lui-même ou sa moto), collision, traînée, immobilité
tag @s add mg.tme
scoreboard players operation $tid mg.st = @s mg.trc
execute if score $trm mg.st matches 0 run tag @s add mg.tcar
execute if score $trm mg.st matches 1 on vehicle run tag @s add mg.tcar
execute if score $trm mg.st matches 1 unless entity @e[tag=mg.tcar] run function mg:tron/remount
execute if score $trm mg.st matches 1 on vehicle run tag @s add mg.tcar
execute if score $trm mg.st matches 1 unless entity @e[tag=mg.tcar] run return run function mg:tron/out_dismount
execute as @e[tag=mg.trm] if score @s mg.trc = $tid mg.st run tag @s add mg.tcm
execute as @e[tag=mg.trp] if score @s mg.trc = $tid mg.st run tag @s add mg.tpm
scoreboard players set $tdead mg.st 0
execute if score $trt mg.st matches 20.. as @e[tag=mg.tcar,limit=1] at @s run function mg:tron/probe
scoreboard players add @s mg.trs 1
execute as @e[tag=mg.tcm,limit=1] at @s align xyz unless entity @e[tag=mg.tcar,dx=0,dy=0,dz=0] run function mg:tron/lay
tag @e remove mg.tcar
tag @e remove mg.tcm
tag @e remove mg.tpm
tag @s remove mg.tme
execute if score $tdead mg.st matches 1 run return run function mg:tron/out_wall
execute if score @s mg.trs matches 50.. run return run function mg:tron/out_still
execute if score @s mg.trs matches 25 run title @s actionbar {"text":"⚠ Avance ! (immobile = éliminé)","color":"red"}
