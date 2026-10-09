# @s : plus de piste libre → spectateur de la partie
tag @s remove mg.play
tag @s add mg.out
gamemode spectator @s
tp @s 0.5 72 35146.5 0 20
tellraw @s [{"text":"🎳 Les 8 pistes sont prises : tu regardes cette partie en spectateur.","color":"gray"}]
