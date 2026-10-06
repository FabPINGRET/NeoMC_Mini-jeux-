# Une rafale de vent a été lancée (@s = lanceur) : chute ralentie pour tous les joueurs du lobby (pas de dégâts de chute)
scoreboard players reset @s mg.wc
execute if score $state mg.st matches 0 run effect give @a[tag=!mg.play] minecraft:slow_falling 8 0 true
