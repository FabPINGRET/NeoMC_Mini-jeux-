# Départ
scoreboard players set $cft mg.st 0
execute as @a[tag=mg.play] run function mg:ctf/kit
scoreboard players set @a mg.deaths 0
scoreboard players set Rouge mg.cf 0
scoreboard players set Bleu mg.cf 0
scoreboard objectives setdisplay sidebar mg.cf
execute if score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] [{"text":"🚩 CAPTURE THE FLAG : ","color":"gold","bold":true},{"text":"va chercher le drapeau adverse (au fond de sa base) et ramène-le sur ton socle doré, pendant que TON drapeau y est. 3 captures pour gagner, 10 min max.","color":"gray"}]
execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] [{"text":"🚩 CAPTURE THE FLAG : ","color":"gold","bold":true},{"text":"va chercher le drapeau adverse (au fond de sa base) et ramène-le sur ton socle doré, pendant que TON drapeau y est. 10 min max.","color":"gray"}]
execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] [{"text":"🚩 Mode entraînement (seul) : le drapeau bleu n'est pas défendu, entraîne-toi aux captures. Pas de victoire ; il faut au moins 2 joueurs pour une vraie partie.","color":"yellow"}]
