# Manche perdue (@s = victime ; le tireur porte mg.dlsh) : +1 manche au tireur, match fini à 3
scoreboard players operation $dli mg.st = @s mg.dli
tag @a[tag=mg.dlsh,limit=1] add mg.dlwn
scoreboard players add @a[tag=mg.dlsh,limit=1] mg.dlr 1
execute as @a[tag=mg.dl] if score @s mg.dli = $dli mg.st run tag @s add mg.dlsp
execute if entity @a[tag=mg.dlwn,scores={mg.dlr=3..}] run return run function mg:duel/win
execute at @s run particle minecraft:firework ~ ~1 ~ 0.3 0.5 0.3 0.15 40
tellraw @a[tag=mg.dlsp] [{"text":"⚔ Manche pour ","color":"gold"},{"selector":"@a[tag=mg.dlwn,limit=1]","color":"yellow"},{"text":" : ","color":"gray"},{"score":{"name":"@a[tag=mg.dlwn,limit=1]","objective":"mg.dlr"},"color":"gold"},{"text":" - ","color":"gray"},{"score":{"name":"@s","objective":"mg.dlr"},"color":"red"}]
tag @a remove mg.dlwn
function mg:duel/next
