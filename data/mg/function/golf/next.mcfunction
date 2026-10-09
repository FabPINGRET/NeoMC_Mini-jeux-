# @s : sa balle vient de s'arrêter (pas dans le trou)
execute unless score @s mg.gfs matches 1 run return 0
execute if score @s mg.gfc matches 8.. run return run function mg:golf/give_up
function mg:golf/stroke_start
function mg:golf/own
execute at @e[tag=mg.gfmy,limit=1] if block ~ ~-0.05 ~ #mg:golf_green run title @s actionbar {"text":"Sur le green : prends le Putter !","color":"green"}
tag @e[tag=mg.gfmy] remove mg.gfmy
