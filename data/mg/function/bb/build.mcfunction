# Build Battle — décor permanent : studio + 12 parcelles (idempotent)
function mg:bb/studio
scoreboard players set $bbpi mg.st 0
execute positioned -120 64 13700 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 1
execute positioned -72 64 13700 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 2
execute positioned -24 64 13700 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 3
execute positioned 24 64 13700 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 4
execute positioned 72 64 13700 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 5
execute positioned 120 64 13700 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 6
execute positioned -120 64 13748 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 7
execute positioned -72 64 13748 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 8
execute positioned -24 64 13748 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 9
execute positioned 24 64 13748 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 10
execute positioned 72 64 13748 run function mg:bb/plot_reset
scoreboard players set $bbpi mg.st 11
execute positioned 120 64 13748 run function mg:bb/plot_reset
