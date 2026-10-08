# Mob Arena — plus de monstres au-delà de 4 joueurs (+25 % par joueur), appelé juste après la vague de base
execute store result score $mnp mg.st if entity @a[tag=mg.play]
scoreboard players operation $mex mg.st = $mnp mg.st
scoreboard players remove $mex mg.st 4
execute if score $mex mg.st matches ..0 run return 0
execute store result score $mb0 mg.st if entity @e[tag=mg.mob]
scoreboard players set $wdup mg.st 1
function mg:mobarena/scale_pass
execute if score $mex mg.st matches 1..3 run function mg:mobarena/scale_part
scoreboard players set $wdup mg.st 0
tag @e remove mg.mb0
execute store result score $mb1 mg.st if entity @e[tag=mg.mob]
tellraw @a [{"text":"  ➜ ","color":"gray"},{"score":{"name":"$mnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs : ","color":"gray"},{"score":{"name":"$mb1","objective":"mg.st"},"color":"red"},{"text":" monstres au lieu de ","color":"gray"},{"score":{"name":"$mb0","objective":"mg.st"},"color":"yellow"}]
