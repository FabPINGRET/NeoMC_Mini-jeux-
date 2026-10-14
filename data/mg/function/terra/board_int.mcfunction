# @s (tableau) : le colon qui a cliqué voit les missions
execute on target if entity @s[tag=mg.tvw] run function mg:terra/board
data remove entity @s interaction
