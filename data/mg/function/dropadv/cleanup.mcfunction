kill @e[type=minecraft:text_display,tag=mg.dat]
execute as @e[type=minecraft:item,x=-20,y=0,z=23980,dx=520,dy=308,dz=40] if items entity @s contents *[custom_data~{mg_dskip:1b}] run kill @s
function mg:dropadv/fl_remove
scoreboard objectives setdisplay sidebar
tag @a remove mg.ddone
