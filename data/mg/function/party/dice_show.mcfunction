# Affiche $dv sur le grand dé du plateau
execute if score $dv mg.st matches 1 run data modify entity @e[type=minecraft:text_display,tag=mg.mpdice,limit=1] text set value [{"text":"1","color":"white","bold":true}]
execute if score $dv mg.st matches 2 run data modify entity @e[type=minecraft:text_display,tag=mg.mpdice,limit=1] text set value [{"text":"2","color":"white","bold":true}]
execute if score $dv mg.st matches 3 run data modify entity @e[type=minecraft:text_display,tag=mg.mpdice,limit=1] text set value [{"text":"3","color":"white","bold":true}]
execute if score $dv mg.st matches 4 run data modify entity @e[type=minecraft:text_display,tag=mg.mpdice,limit=1] text set value [{"text":"4","color":"white","bold":true}]
execute if score $dv mg.st matches 5 run data modify entity @e[type=minecraft:text_display,tag=mg.mpdice,limit=1] text set value [{"text":"5","color":"white","bold":true}]
execute if score $dv mg.st matches 6 run data modify entity @e[type=minecraft:text_display,tag=mg.mpdice,limit=1] text set value [{"text":"6","color":"white","bold":true}]
