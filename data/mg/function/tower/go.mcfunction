# Départ : survie (construction libre)
scoreboard players set $twt mg.st 0
gamemode survival @a[tag=mg.play]
execute as @a[tag=mg.play] run function mg:tower/kit
scoreboard players set @a mg.deaths 0
scoreboard players reset @a mg.tw
scoreboard players set Rouge mg.tw 0
scoreboard players set Bleu mg.tw 0
scoreboard objectives setdisplay sidebar mg.tw
tellraw @a[tag=mg.play] [{"text":"🏰 THE TOWERS : ","color":"gold","bold":true},{"text":"saute dans le PUITS de l'équipe adverse (au bout de son île) = +1 point. 5 points pour gagner, 10 min max. Construis tes ponts, défends ton puits !","color":"gray"}]
