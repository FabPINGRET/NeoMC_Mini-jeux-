# Temps écoulé : le plus proche de la sortie gagne
tellraw @a {"text":"⏱ Temps écoulé ! Le plus proche de la sortie l'emporte.","color":"gold"}
execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw
execute positioned 51 65 41100 as @a[tag=mg.play,gamemode=adventure,sort=nearest,limit=1] run return run function mg:core/win_player
function mg:core/draw
