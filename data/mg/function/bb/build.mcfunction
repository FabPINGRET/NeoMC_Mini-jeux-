# Build Battle — décor permanent : studio + 12 parcelles (idempotent)
function mg:bb/studio
scoreboard players set $bbpi mg.st 0
execute positioned 0 64 13700 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 1
execute positioned 640 64 13700 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 2
execute positioned 1280 64 13700 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 3
execute positioned 1920 64 13700 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 4
execute positioned 2560 64 13700 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 5
execute positioned 3200 64 13700 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 6
execute positioned 0 64 14340 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 7
execute positioned 640 64 14340 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 8
execute positioned 1280 64 14340 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 9
execute positioned 1920 64 14340 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 10
execute positioned 2560 64 14340 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 11
execute positioned 3200 64 14340 run function mg:bb/plot_reset
