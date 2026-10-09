# Départ : survie (construction libre)
scoreboard players set $twt mg.st 0
gamemode survival @a[tag=mg.play]
execute as @a[tag=mg.play] run function mg:tower/kit
scoreboard players set @a mg.deaths 0
scoreboard players reset @a mg.tw
scoreboard players set Rouge mg.tw 0
scoreboard players set Bleu mg.tw 0
scoreboard objectives setdisplay sidebar mg.tw
execute if score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] [{"text":"🏰 THE TOWERS : ","color":"gold","bold":true},{"text":"saute dans le PUITS de l'équipe adverse (au bout de son île) = +1 point. 5 points pour gagner, 10 min max. Construis tes ponts, défends ton puits !","color":"gray"}]
execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] [{"text":"🏰 THE TOWERS : ","color":"gold","bold":true},{"text":"saute dans le PUITS de l'équipe adverse (au bout de son île) = +1 point. 10 min max. Construis tes ponts, défends ton puits !","color":"gray"}]
execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] [{"text":"🏰 Mode entraînement (seul) : saute dans le puits bleu pour marquer, construis tes ponts. Pas de victoire ; il faut au moins 2 joueurs pour une vraie partie.","color":"yellow"}]
