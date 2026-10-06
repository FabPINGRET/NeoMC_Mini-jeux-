# Joueur éclaboussé (@s = victime, $st = équipe du tireur) : flaque de peinture, retour à la base
tellraw @a [{"selector":"@s","color":"gray"},{"text":" a été éclaboussé par ","color":"dark_gray"},{"selector":"@a[tag=mg.qsh,limit=1]","color":"gray"}]
execute at @s if score $st mg.st matches 1 run function mg:paintball/burst_o
execute at @s if score $st mg.st matches 2 run function mg:paintball/burst_b
execute at @s run particle minecraft:explosion ~ ~1 ~ 0.3 0.3 0.3 0 3
execute at @s run playsound minecraft:entity.generic.splash master @a ~ ~ ~ 1 0.8
function mg:paintball/respawn
