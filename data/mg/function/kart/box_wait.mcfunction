scoreboard players remove @s mg.t 1
execute if score @s mg.t matches 1.. run return 0
tag @s remove mg.kboff
item replace entity @s contents with minecraft:yellow_stained_glass
execute at @s as @e[type=minecraft:text_display,tag=mg.kboxq,distance=..1.5] run data merge entity @s {text:[{"text":"?","color":"gold","bold":true}]}
