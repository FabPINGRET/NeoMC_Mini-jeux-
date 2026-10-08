# Départ
scoreboard players set $cft mg.st 0
execute as @a[tag=mg.play] run function mg:ctf/kit
scoreboard players set @a mg.deaths 0
scoreboard players set Rouge mg.cf 0
scoreboard players set Bleu mg.cf 0
scoreboard objectives setdisplay sidebar mg.cf
tellraw @a[tag=mg.play] [{"text":"🚩 CAPTURE THE FLAG : ","color":"gold","bold":true},{"text":"va chercher le drapeau adverse (au fond de sa base) et ramène-le sur ton socle doré, pendant que TON drapeau y est. 3 captures pour gagner, 10 min max.","color":"gray"}]
