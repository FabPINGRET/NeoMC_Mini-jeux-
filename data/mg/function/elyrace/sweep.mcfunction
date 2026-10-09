# @s = joueur en course (en tete de c<N>/rings) : origine du balayage (position du tick precedent, mg.xq1..3) dans #xox..#xoz,
# position courante (centiemes) dans #xqx..#xqz, puis memorisee comme origine du tick suivant
scoreboard players operation #xox mg.st = @s mg.xq1
scoreboard players operation #xoy mg.st = @s mg.xq2
scoreboard players operation #xoz mg.st = @s mg.xq3
execute store result score #xqx mg.st run data get entity @s Pos[0] 100
execute store result score #xqy mg.st run data get entity @s Pos[1] 100
execute store result score #xqz mg.st run data get entity @s Pos[2] 100
scoreboard players operation @s mg.xq1 = #xqx mg.st
scoreboard players operation @s mg.xq2 = #xqy mg.st
scoreboard players operation @s mg.xq3 = #xqz mg.st
scoreboard players set #xhit mg.st 0
scoreboard players operation #xqd mg.st = #xqx mg.st
scoreboard players operation #xqd mg.st -= #xox mg.st
# deplacement hors de 1..1900 centiemes (teleportation, premier tick, retour en arriere) : aucun anneau franchi ce tick
execute unless score #xqd mg.st matches 1..1900 run scoreboard players set #xox mg.st 2147483647
