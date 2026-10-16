# Régions prêtes : bords de la carte, drapeau, plus de chargement forcé si personne ne joue
execute in mg:terranova run kill @e[type=minecraft:item,x=-260,y=40,z=-260,dx=520,dy=140,dz=520]
execute in mg:terranova run function mg:terra/walls_old
execute in mg:terranova run function mg:terra/walls
data modify storage mg:terra v2 set value 1b
execute unless score $tvw mg.st matches 1 in mg:terranova run forceload remove -112 -112 111 111
execute unless score $tvw mg.st matches 1 in mg:terranova run forceload remove -96 -256 95 -97
execute unless score $tvw mg.st matches 1 in mg:terranova run forceload remove 96 -96 255 95
execute unless score $tvw mg.st matches 1 in mg:terranova run forceload remove -256 -96 -97 95
execute unless score $tvw mg.st matches 1 in mg:terranova run forceload remove -96 96 95 255
function mg:terra/bio_try
tellraw @a[tag=mg.admin] {"text":"🦖 Terra Nova est construite (vallée et régions du RPG).","color":"green"}
