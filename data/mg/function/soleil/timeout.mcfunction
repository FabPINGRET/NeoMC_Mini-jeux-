# Temps écoulé : ceux qui ne sont pas arrivés sont éliminés
tellraw @a[tag=mg.play] {"text":"⏰ Temps écoulé !","color":"red","bold":true}
function mg:soleil/turn {yaw:180}
execute if score $n0 mg.st matches 2.. as @a[tag=mg.play,tag=!mg.sqf] run function mg:soleil/shot
function mg:soleil/end
