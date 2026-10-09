# Départ : le plancher disparaît, tout le monde s'envole dans la ville
scoreboard players set $btt mg.st 0
fill -88 170 32312 88 170 32488 minecraft:air replace minecraft:barrier
effect give @a[tag=mg.play] minecraft:slow_falling 3 0 true
execute unless score $bbs mg.st matches 119.. run function mg:bomber/build_rest
execute as @a[tag=mg.play] run function mg:bomber/kit
scoreboard players reset @a mg.qs
scoreboard objectives setdisplay sidebar mg.bmb
tellraw @a[tag=mg.play] [{"text":"💣 BOMBARDIER : ","color":"red","bold":true},{"text":"saute et ouvre tes élytres (Espace) : vole entre les gratte-ciel (fusées illimitées, case 9), vise et clic droit pour larguer. Posé au sol : accroupis-toi pour repartir. Chaque bloc détruit = 1 point, or et statue = 10. Bombe atomique pour la dernière minute. 2 min 30.","color":"gray"}]
