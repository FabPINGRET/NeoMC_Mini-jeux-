# @s (tag mg.frz), chaque tick : ramène au point de gel si le joueur s'en écarte (saut, poussée, glissade)
# en véhicule (kart, bateau, cheval…) : rien, un tp le ferait descendre
execute on vehicle run return 0
# gelé avant cette version (pas de hauteur notée) : point de gel = ici
execute unless score @s mg.fy matches -2147483648.. run return run function mg:core/freeze_anchor
# posé au sol : la hauteur du point de gel suit (chute verticale normale si le joueur est apparu en l'air)
execute if entity @s[nbt={OnGround:1b}] store result score @s mg.fy run data get entity @s Pos[1] 100
execute store result score $hx mg.st run data get entity @s Pos[0] 100
execute store result score $hz mg.st run data get entity @s Pos[2] 100
scoreboard players operation $hx mg.st -= @s mg.fx
scoreboard players operation $hz mg.st -= @s mg.fz
# plus de 3 blocs : téléporté par le jeu pendant le compte à rebours → nouveau point de gel
execute unless score $hx mg.st matches -300..300 run return run function mg:core/freeze_anchor
execute unless score $hz mg.st matches -300..300 run return run function mg:core/freeze_anchor
execute if score $hx mg.st matches -10..10 if score $hz mg.st matches -10..10 run return 0
# écarté : retour au point de gel, hauteur comprise (sinon un pas dans le vide fait descendre d'un cran à chaque retour)
execute store result storage mg:frz p.x double 0.01 run scoreboard players get @s mg.fx
execute store result storage mg:frz p.y double 0.01 run scoreboard players get @s mg.fy
execute store result storage mg:frz p.z double 0.01 run scoreboard players get @s mg.fz
function mg:core/freeze_tp with storage mg:frz p
