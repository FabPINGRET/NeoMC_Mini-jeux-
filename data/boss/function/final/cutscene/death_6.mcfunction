title @a[tag=mg.flw] subtitle "Thanks for playing!"
title @a[tag=mg.flw] title "The End"

#stop black glass death tick
setblock -9772 273 431 air

tp @a[tag=mg.flw] -12354 -28 355 90 0
spawnpoint @a[tag=mg.flw] -12354 -28 355 90 0
scoreboard players set $flsp mg.st 3
execute as @a[tag=mg.flw] run playsound minecraft:soundtrack.9am_1 record @s ~ ~ ~ 1 1 1

function boss:final/init


#","color":"white"},{"text":"
