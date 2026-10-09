# Trou suivant
scoreboard players add $gfh mg.st 1
scoreboard players set $gft mg.st 0
kill @e[type=minecraft:item_display,tag=mg.gfb]
execute if score $gfh mg.st matches 1 run function mg:golf/h1
execute if score $gfh mg.st matches 2 run function mg:golf/h2
execute if score $gfh mg.st matches 3 run function mg:golf/h3
execute if score $gfh mg.st matches 4 run function mg:golf/h4
execute if score $gfh mg.st matches 5 run function mg:golf/h5
execute if score $gfh mg.st matches 6 run function mg:golf/h6
