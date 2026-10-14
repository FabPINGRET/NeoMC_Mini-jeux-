# @s : mission « Chasse : 5 slashers »
scoreboard players set @s mg.tvm 3
scoreboard players set @s mg.tvmp 0
execute as @e[type=minecraft:marker,tag=mg.tvfar,sort=random,limit=1] run function mg:terra/mark_loc
function mg:terra/loc with storage mg:terra h
tellraw @s [{"text":"🦖 Mission : ","color":"green","bold":true},{"text":"abats 5 slashers dans la jungle (le 📡 indique une zone de chasse). ","color":"gray"},{"text":"+200 ₵","color":"green"}]
