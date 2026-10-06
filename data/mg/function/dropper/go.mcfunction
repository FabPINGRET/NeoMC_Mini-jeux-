# The Dropper — début : on ouvre les sols, c'est la chute libre
effect give @a[tag=mg.play] minecraft:saturation infinite 0 true
execute as @a[tag=mg.play] run function mg:dropper/attr_on
scoreboard objectives setdisplay below_name mg.dp
scoreboard objectives setdisplay list mg.dp
tellraw @a[tag=mg.play] [{"text":"⬇ THE DROPPER ! ","color":"aqua","bold":true},{"text":"Saute dans le trou du puits (au GO !) et esquive les obstacles : atterris dans l'UNIQUE bloc d'eau au fond ! Touche un obstacle ou le sol = retour en haut. Premier à 2 manches gagne !","color":"gray"}]
execute if score $sg mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":"Tube commun : tout le monde saute dans le MÊME puits, le premier à atterrir dans l'eau gagne la manche !","color":"yellow"}]
function mg:dropper/start_round
