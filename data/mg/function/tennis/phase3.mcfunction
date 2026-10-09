# @s : marqueur — pause après un point
scoreboard players remove @s mg.tnt 1
execute if score @s mg.tnt matches 1.. run return 0
execute if entity @s[tag=mg.tndone] run return run function mg:tennis/court_end
function mg:tennis/point_setup
