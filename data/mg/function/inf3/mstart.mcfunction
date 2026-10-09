# Joueurs contre mobs : réglages des zombies et première vague
data modify storage mg:zm hp set value 24
data modify storage mg:zm sp set value 0.25d
scoreboard players set $imc mg.st 0
scoreboard players set $imz mg.st 0
execute store result score $imw mg.st if entity @a[tag=mg.play]
scoreboard players add $imw mg.st 2
function mg:inf3/mwave
tellraw @a[tag=mg.play] [{"text":"🧟 JOUEURS CONTRE MOBS : ","color":"red","bold":true},{"text":"des zombies envahissent le bunker. Un seul coup d'un zombie et tu es infecté : tu chasses alors les survivants (ton coup les infecte aussi). Tenez 3 minutes !","color":"gray"}]
