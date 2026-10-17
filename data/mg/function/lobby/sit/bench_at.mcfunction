# @s : position = coin du bloc (align xyz). Banc libre (pas de siège à moins de 0,3) ? Oui : s'y assoit (sit/seat), retourne 1 ; non : 0
# siège au centre du bloc, 0.5 au-dessus de son pied (SEAT_DY) ; regard vers la marche basse : yaw opposé au facing (east 90, west -90, north 0, south 180)
execute positioned ~0.5 ~0.5 ~0.5 if entity @e[type=minecraft:item_display,tag=mg.seat,distance=..0.3] run return 0
execute if block ~ ~ ~ minecraft:spruce_stairs[half=bottom,facing=east] positioned ~0.5 ~0.5 ~0.5 rotated 90 0 run return run function mg:lobby/sit/seat
execute if block ~ ~ ~ minecraft:spruce_stairs[half=bottom,facing=west] positioned ~0.5 ~0.5 ~0.5 rotated -90 0 run return run function mg:lobby/sit/seat
execute if block ~ ~ ~ minecraft:spruce_stairs[half=bottom,facing=north] positioned ~0.5 ~0.5 ~0.5 rotated 0 0 run return run function mg:lobby/sit/seat
execute if block ~ ~ ~ minecraft:spruce_stairs[half=bottom,facing=south] positioned ~0.5 ~0.5 ~0.5 rotated 180 0 run return run function mg:lobby/sit/seat
return 0
