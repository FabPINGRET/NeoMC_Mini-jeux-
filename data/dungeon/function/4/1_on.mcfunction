playsound minecraft:item.flintandsteel.use master @a[tag=mg.flw] -10011 95 -337 1 1 1
playsound minecraft:entity.blaze.shoot master @a[tag=mg.flw] -10011 95 -337 1 0.1 1
playsound minecraft:entity.blaze.shoot master @a[tag=mg.flw] -10011 95 -337 1 1 1
playsound minecraft:item.trident.thunder master @a[tag=mg.flw] -10011 95 -337 1 2 1
playsound minecraft:entity.firework_rocket.twinkle master @a[tag=mg.flw] -10011 95 -337 1 2 1
fill -10010 96 -337 -10012 96 -337 lava
fill -10012 94 -336 -10010 94 -336 fire
particle minecraft:small_flame -10011 95 -335 1 1 1 0.2 300 force
fill -10002 91 -320 -10004 91 -318 lava replace air
fill -9998 91 -318 -9995 91 -321 lava replace air
setblock -10000 91 -318 minecraft:redstone_torch
setblock -9995 96 -324 lava
setblock -9961 112 -317 minecraft:redstone_block
setblock -9990 113 -350 lava


fill -9992 89 -353 -9988 89 -357 glass
fill -9984 90 -361 -9996 90 -349 lava replace air

tellraw @a[tag=mg.flw] [{"text":"Lava has started flowing through the ","italic":true},{"text":"Blue ","color":"blue"},{"text":"pipe...","color":"white"}]
