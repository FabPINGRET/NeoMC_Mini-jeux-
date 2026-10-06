# Tir (@s = joueur qui vient de lancer un œuf) : munitions rechargées + rayon instantané le long de son regard (portée 80 blocs)
function mg:splegg/give_egg
playsound minecraft:entity.chicken.egg master @a ~ ~ ~ 0.8 1.4
scoreboard players set $rs mg.st 160
execute at @s anchored eyes positioned ^ ^ ^0.5 run function mg:splegg/ray
