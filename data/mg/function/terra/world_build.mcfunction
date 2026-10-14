# Première construction de Terra Nova (ou reconstruction complète, ~2 min)
execute in mg:terranova run forceload add -112 -112 111 111
scoreboard players set $tvb mg.st 0
schedule function mg:terra/wb_step 40t
