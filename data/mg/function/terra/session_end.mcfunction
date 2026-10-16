# Plus personne à Terra Nova : entités retirées, outposts réparés, plus de chargement forcé
scoreboard players set $tvw mg.st 0
scoreboard players set $tvsu mg.st 0
schedule clear mg:terra/session_setup
function mg:terra/clear
team remove mg_tv
execute in mg:terranova run function mg:terra/out_build_1
execute in mg:terranova run function mg:terra/out_build_2
execute in mg:terranova run function mg:terra/out_build_3
execute in mg:terranova run forceload remove -112 -112 111 111
execute in mg:terranova run forceload remove -96 -256 95 -97
execute in mg:terranova run forceload remove 96 -96 255 95
execute in mg:terranova run forceload remove -256 -96 -97 95
execute in mg:terranova run forceload remove -96 96 95 255
schedule clear mg:terra/rpg/setup_s
