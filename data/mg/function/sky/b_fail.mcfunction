# Zone jamais chargée : abandon propre
function mg:sky/fl_secs_off
scoreboard players set $skbm mg.st 0
tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Élytra : zone pas chargée, construction interrompue (relance mg:sky/build).","color":"red"}]
