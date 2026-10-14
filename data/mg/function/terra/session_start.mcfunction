# Premier joueur à Terra Nova : chargement de la carte, entités dans 1,5 s
scoreboard players set $tvw mg.st 1
scoreboard players set $tvt mg.st 0
scoreboard players set $tvsu mg.st 0
execute in mg:terranova run forceload add -112 -112 111 111
schedule function mg:terra/session_setup 30t
