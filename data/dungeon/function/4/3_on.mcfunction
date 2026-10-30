playsound minecraft:item.flintandsteel.use master @a[tag=mg.flw] -9945 94 -241 1 1 1
playsound minecraft:entity.blaze.shoot master @a[tag=mg.flw] -9945 94 -241 1 0.1 1
playsound minecraft:entity.blaze.shoot master @a[tag=mg.flw] -9945 94 -241 1 1 1
playsound minecraft:item.trident.thunder master @a[tag=mg.flw] -9945 94 -241 1 2 1
playsound minecraft:entity.firework_rocket.twinkle master @a[tag=mg.flw] -9945 94 -241 1 2 1
particle minecraft:small_flame -9945 94 -244 1 1 1 0.2 300 force

fill -9944 93 -242 -9946 93 -242 fire
fill -9944 95 -241 -9946 95 -241 lava
fill -9943 90 -262 -9941 90 -264 lava replace air
fill -9940 90 -271 -9941 90 -268 lava replace air
setblock -9937 95 -271 lava
setblock -9941 90 -266 minecraft:redstone_torch
setblock -9994 125 -357 lava

fill -9992 89 -353 -9988 89 -357 glass
fill -9984 90 -361 -9996 90 -349 lava replace air

tellraw @a[tag=mg.flw] [{"text":"Lava has started flowing through the ","italic":true},{"text":"Red ","color":"red"},{"text":"pipe...","color":"white"}]
