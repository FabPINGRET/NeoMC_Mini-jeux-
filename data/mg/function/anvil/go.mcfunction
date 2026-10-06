# Pluie d'Enclumes — début de partie
scoreboard players set $c2 mg.st 2
scoreboard players set $amin mg.st 3
scoreboard players set $ai mg.st 26
scoreboard players set $ac mg.st 30
scoreboard players set $lv mg.st 1
scoreboard players set $lt mg.st 160
scoreboard players set $cl mg.st 10
scoreboard players set $hc mg.st 120
scoreboard players set $hmin mg.st 45
scoreboard players set $c6 mg.st 6
effect give @a[tag=mg.play] minecraft:saturation infinite 0 true
tellraw @a[tag=mg.play] [{"text":"⚓ PLUIE D'ENCLUMES ! ","color":"gray","bold":true},{"text":"Des enclumes tombent du ciel : surveille le sol, une tache noire = une enclume dans 1,5 s ! La pluie s'intensifie toutes les 8 s. Dernier debout = gagnant !","color":"dark_gray"}]
execute if score $sg mg.st matches 2 run tellraw @a[tag=mg.play] [{"text":"⚓ SOL TROUÉ : ","color":"red","bold":true},{"text":"de temps en temps, une zone du sol vire au rouge puis disparaît pendant 6 s. Ne reste pas dessus !","color":"gray"}]
