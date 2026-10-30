# Premier joueur : chunk forcé de la carte, load de la carte (message de version) une fois par session
scoreboard players set $flw mg.st 1
execute in mg:floaty run forceload add -9776 416 -9761 431
execute in mg:floaty positioned 1274 209 181 run function floaty:map/load
