# Biomes des régions posés une seule fois, dès que le serveur les connaît (après un redémarrage)
execute if data storage mg:terra bio run return 0
execute unless data storage mg:terra v2 run return 0
scoreboard players set $tvbo mg.st 0
execute store result score $tvbo mg.st run function mg:terra/bio/ok
execute unless score $tvbo mg.st matches 1 run return 0
data modify storage mg:terra bio set value 1b
scoreboard players set $tvbs mg.st 0
execute in mg:terranova run forceload add -112 -112 111 111
execute in mg:terranova run forceload add -96 -256 95 -97
execute in mg:terranova run forceload add 96 -96 255 95
execute in mg:terranova run forceload add -256 -96 -97 95
execute in mg:terranova run forceload add -96 96 95 255
schedule function mg:terra/bio_step 60t
