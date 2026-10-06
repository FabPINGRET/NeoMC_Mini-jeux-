# Mob Arena — combat : la vague est-elle terminée ?
execute store result score $mob mg.st if entity @e[tag=mg.mob]
# Progression : annonce quand il reste 3 monstres ou moins
execute if score $mob mg.st matches 1..3 unless score $mob mg.st = $ml mg.st run tellraw @a [{"text":"[Mob Arena] ","color":"dark_green","bold":true},{"text":"Plus que ","color":"gray"},{"score":{"name":"$mob","objective":"mg.st"},"color":"yellow","bold":true},{"text":" monstre(s) !","color":"gray"}]
execute if score $mob mg.st matches 1..3 run scoreboard players operation $ml mg.st = $mob mg.st
execute if score $mob mg.st matches 1.. run return 0

# Vague nettoyée !
execute if score $wv mg.st >= $wmax mg.st run return run function mg:mobarena/victory
function mg:mobarena/reward
