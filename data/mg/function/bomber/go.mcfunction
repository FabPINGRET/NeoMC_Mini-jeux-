# Départ
scoreboard players set $btt mg.st 0
execute unless score $bbs mg.st matches 120.. run function mg:bomber/build_rest
execute as @a[tag=mg.play] run function mg:bomber/kit
scoreboard players reset @a mg.qs
scoreboard objectives setdisplay sidebar mg.bmb
tellraw @a[tag=mg.play] [{"text":"💣 BOMBARDIER : ","color":"red","bold":true},{"text":"vise un immeuble et clic droit pour larguer. Chaque bloc détruit = 1 point, or et statue = 10. Bombe atomique pour la dernière minute. 2 min 30.","color":"gray"}]
