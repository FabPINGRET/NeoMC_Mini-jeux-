# Fin de la construction du spawn : eau qui coule, décor, chargement des zones
setblock -5 67 -5 minecraft:water
setblock -5 67 5 minecraft:water
setblock 5 67 -5 minecraft:water
setblock 5 67 5 minecraft:water
setblock -30 67 30 minecraft:water
setblock 60 63 40 minecraft:water
setblock -39 63 59 minecraft:water
setblock -59 63 -39 minecraft:water
setblock 40 63 -60 minecraft:water
setblock 27 90 -27 minecraft:water
function mg:lobby/deco
function mg:lobby/armory_build
function mg:parkour/build
forceload remove -80 -80 80 80
forceload remove 81 -32 144 32
function mg:core/forceloads
data modify storage mg:lobby v2 set value 1b
tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Spawn construit.","color":"green"}]
