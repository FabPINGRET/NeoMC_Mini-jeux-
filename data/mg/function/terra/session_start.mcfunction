# Premier joueur à Terra Nova : chargement de la carte, entités dans 1,5 s
scoreboard players set $tvw mg.st 1
scoreboard players add $tvses mg.st 1
scoreboard players set $tvt mg.st 0
scoreboard players set $tvsu mg.st 0
execute in mg:terranova run forceload add -112 -112 111 111
execute in mg:terranova run forceload add -96 -256 95 -97
execute in mg:terranova run forceload add 96 -96 255 95
execute in mg:terranova run forceload add -256 -96 -97 95
execute in mg:terranova run forceload add -96 96 95 255
schedule function mg:terra/session_setup 30t
schedule function mg:terra/rpg/setup_s 100t
