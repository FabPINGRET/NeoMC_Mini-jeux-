# @s (tag mg.frz), chaque tick : ramène au point de gel si le joueur s'en écarte (saut, poussée, glissade)
# en véhicule (kart, bateau, cheval…) : rien, un tp le ferait descendre
execute on vehicle run return 0
execute store result score $hx mg.st run data get entity @s Pos[0] 100
execute store result score $hz mg.st run data get entity @s Pos[2] 100
scoreboard players operation $hx mg.st -= @s mg.fx
scoreboard players operation $hz mg.st -= @s mg.fz
# plus de 3 blocs : téléporté par le jeu pendant le compte à rebours → nouveau point de gel
execute unless score $hx mg.st matches -300..300 run return run function mg:core/freeze_anchor
execute unless score $hz mg.st matches -300..300 run return run function mg:core/freeze_anchor
execute if score $hx mg.st matches -10..10 if score $hz mg.st matches -10..10 run return 0
execute store result storage mg:frz p.x double 0.01 run scoreboard players get @s mg.fx
execute store result storage mg:frz p.z double 0.01 run scoreboard players get @s mg.fz
function mg:core/freeze_tp with storage mg:frz p
