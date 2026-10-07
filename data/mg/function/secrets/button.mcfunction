# Le bouton secret du garage : feu d'artifice au-dessus du podium
scoreboard players set $ebt mg.st 100
execute as @a[x=0.5,y=65,z=50.5,distance=..5] run advancement grant @s only mg:secrets/bouton
execute positioned 0.5 80 48.5 run function mg:lobby/boom
execute positioned -6.5 76 48.5 run function mg:lobby/boom
execute positioned 7.5 77 48.5 run function mg:lobby/boom
