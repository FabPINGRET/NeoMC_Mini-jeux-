# @s : un banc (spruce_stairs[half=bottom]) sous les pieds ou à côté ? Oui : s'y assoit (sit/seat), retourne 1 ; non : retourne 0
# siège au centre du bloc, 0.5 au-dessus de son pied (SEAT_DY) ; regard vers la marche basse : yaw opposé au facing (east 90, west -90, north 0, south 180)
execute if block ~ ~-1 ~ minecraft:spruce_stairs[half=bottom,facing=east] positioned ~ ~-1 ~ align xyz positioned ~0.5 ~0.5 ~0.5 rotated 90 0 run return run function mg:lobby/sit/seat
execute if block ~ ~-1 ~ minecraft:spruce_stairs[half=bottom,facing=west] positioned ~ ~-1 ~ align xyz positioned ~0.5 ~0.5 ~0.5 rotated -90 0 run return run function mg:lobby/sit/seat
execute if block ~ ~-1 ~ minecraft:spruce_stairs[half=bottom,facing=north] positioned ~ ~-1 ~ align xyz positioned ~0.5 ~0.5 ~0.5 rotated 0 0 run return run function mg:lobby/sit/seat
execute if block ~ ~-1 ~ minecraft:spruce_stairs[half=bottom,facing=south] positioned ~ ~-1 ~ align xyz positioned ~0.5 ~0.5 ~0.5 rotated 180 0 run return run function mg:lobby/sit/seat
execute if block ~ ~ ~ minecraft:spruce_stairs[half=bottom,facing=east] positioned ~ ~ ~ align xyz positioned ~0.5 ~0.5 ~0.5 rotated 90 0 run return run function mg:lobby/sit/seat
execute if block ~ ~ ~ minecraft:spruce_stairs[half=bottom,facing=west] positioned ~ ~ ~ align xyz positioned ~0.5 ~0.5 ~0.5 rotated -90 0 run return run function mg:lobby/sit/seat
execute if block ~ ~ ~ minecraft:spruce_stairs[half=bottom,facing=north] positioned ~ ~ ~ align xyz positioned ~0.5 ~0.5 ~0.5 rotated 0 0 run return run function mg:lobby/sit/seat
execute if block ~ ~ ~ minecraft:spruce_stairs[half=bottom,facing=south] positioned ~ ~ ~ align xyz positioned ~0.5 ~0.5 ~0.5 rotated 180 0 run return run function mg:lobby/sit/seat
execute if block ~1 ~ ~ minecraft:spruce_stairs[half=bottom,facing=east] positioned ~1 ~ ~ align xyz positioned ~0.5 ~0.5 ~0.5 rotated 90 0 run return run function mg:lobby/sit/seat
execute if block ~1 ~ ~ minecraft:spruce_stairs[half=bottom,facing=west] positioned ~1 ~ ~ align xyz positioned ~0.5 ~0.5 ~0.5 rotated -90 0 run return run function mg:lobby/sit/seat
execute if block ~1 ~ ~ minecraft:spruce_stairs[half=bottom,facing=north] positioned ~1 ~ ~ align xyz positioned ~0.5 ~0.5 ~0.5 rotated 0 0 run return run function mg:lobby/sit/seat
execute if block ~1 ~ ~ minecraft:spruce_stairs[half=bottom,facing=south] positioned ~1 ~ ~ align xyz positioned ~0.5 ~0.5 ~0.5 rotated 180 0 run return run function mg:lobby/sit/seat
execute if block ~-1 ~ ~ minecraft:spruce_stairs[half=bottom,facing=east] positioned ~-1 ~ ~ align xyz positioned ~0.5 ~0.5 ~0.5 rotated 90 0 run return run function mg:lobby/sit/seat
execute if block ~-1 ~ ~ minecraft:spruce_stairs[half=bottom,facing=west] positioned ~-1 ~ ~ align xyz positioned ~0.5 ~0.5 ~0.5 rotated -90 0 run return run function mg:lobby/sit/seat
execute if block ~-1 ~ ~ minecraft:spruce_stairs[half=bottom,facing=north] positioned ~-1 ~ ~ align xyz positioned ~0.5 ~0.5 ~0.5 rotated 0 0 run return run function mg:lobby/sit/seat
execute if block ~-1 ~ ~ minecraft:spruce_stairs[half=bottom,facing=south] positioned ~-1 ~ ~ align xyz positioned ~0.5 ~0.5 ~0.5 rotated 180 0 run return run function mg:lobby/sit/seat
execute if block ~ ~ ~1 minecraft:spruce_stairs[half=bottom,facing=east] positioned ~ ~ ~1 align xyz positioned ~0.5 ~0.5 ~0.5 rotated 90 0 run return run function mg:lobby/sit/seat
execute if block ~ ~ ~1 minecraft:spruce_stairs[half=bottom,facing=west] positioned ~ ~ ~1 align xyz positioned ~0.5 ~0.5 ~0.5 rotated -90 0 run return run function mg:lobby/sit/seat
execute if block ~ ~ ~1 minecraft:spruce_stairs[half=bottom,facing=north] positioned ~ ~ ~1 align xyz positioned ~0.5 ~0.5 ~0.5 rotated 0 0 run return run function mg:lobby/sit/seat
execute if block ~ ~ ~1 minecraft:spruce_stairs[half=bottom,facing=south] positioned ~ ~ ~1 align xyz positioned ~0.5 ~0.5 ~0.5 rotated 180 0 run return run function mg:lobby/sit/seat
execute if block ~ ~ ~-1 minecraft:spruce_stairs[half=bottom,facing=east] positioned ~ ~ ~-1 align xyz positioned ~0.5 ~0.5 ~0.5 rotated 90 0 run return run function mg:lobby/sit/seat
execute if block ~ ~ ~-1 minecraft:spruce_stairs[half=bottom,facing=west] positioned ~ ~ ~-1 align xyz positioned ~0.5 ~0.5 ~0.5 rotated -90 0 run return run function mg:lobby/sit/seat
execute if block ~ ~ ~-1 minecraft:spruce_stairs[half=bottom,facing=north] positioned ~ ~ ~-1 align xyz positioned ~0.5 ~0.5 ~0.5 rotated 0 0 run return run function mg:lobby/sit/seat
execute if block ~ ~ ~-1 minecraft:spruce_stairs[half=bottom,facing=south] positioned ~ ~ ~-1 align xyz positioned ~0.5 ~0.5 ~0.5 rotated 180 0 run return run function mg:lobby/sit/seat
return 0
