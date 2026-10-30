# Chaque tick (monde des mini-jeux) : session de la carte, boucle de la carte
execute unless score $setup mg.st matches 1 run return 0
execute unless score $flw mg.st matches 1 if entity @a[tag=mg.flw] run function mg:floaty/session_start
execute if score $flw mg.st matches 1 unless entity @a[tag=mg.flw] run function mg:floaty/session_end
execute if score $flw mg.st matches 1.. in mg:floaty positioned 1274 209 181 run function floaty:map/tick
