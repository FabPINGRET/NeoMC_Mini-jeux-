# @s touche la faille temporelle (étape 85) : elle se referme (cinématique, retour à la colonie)
function mg:terra/rpg/ch {n:90}
function mg:terra/rpg/cs/rift
execute at @s run playsound minecraft:block.end_portal.spawn player @a ~ ~ ~ 1 0.8
particle minecraft:reverse_portal 0.5 101 177 1 2 1 0.3 400 force
function mg:terra/rpg/xp {n:200}
