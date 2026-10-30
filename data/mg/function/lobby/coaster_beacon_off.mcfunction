# Ancienne balise de la montagne russe (supprimée) : une seule fois, drapeau mg:lobby coasterbeacon
setblock -48 63 41 minecraft:air
setblock -48 64 41 minecraft:air
kill @e[type=minecraft:text_display,tag=mg.csd]
kill @e[type=minecraft:minecart,tag=mg.cst]
data modify storage mg:lobby coasterbeacon set value 1b
