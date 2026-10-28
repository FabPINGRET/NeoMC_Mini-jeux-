execute unless score $fnw mg.st matches 1 run return 0
execute unless loaded -22 99 45978 run return run schedule function mg:filon/session_ready 20t
execute unless loaded 38 99 46038 run return run schedule function mg:filon/session_ready 20t
execute unless data storage mg:filon {built:1} run function mg:filon/build
execute unless entity @e[type=minecraft:text_display,tag=mg.fnboard,x=-60,y=0,z=45930,dx=136,dy=200,dz=136] run function mg:filon/ents
scoreboard players set $fnok mg.st 1
function mg:filon/board
execute if score $fnpend mg.st matches 1 run function mg:filon/regen
