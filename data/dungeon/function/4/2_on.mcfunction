playsound minecraft:item.flintandsteel.use master @a[tag=mg.flw] -9996 101 -438 1 1 1
playsound minecraft:entity.blaze.shoot master @a[tag=mg.flw] -9996 101 -438 1 0.1 1
playsound minecraft:entity.blaze.shoot master @a[tag=mg.flw] -9996 101 -438 1 1 1
playsound minecraft:item.trident.thunder master @a[tag=mg.flw] -9996 101 -438 1 2 1
playsound minecraft:entity.firework_rocket.twinkle master @a[tag=mg.flw] -9996 101 -438 1 2 1
particle minecraft:small_flame -9993 101 -438 1 1 1 0.2 300 force

fill -9995 100 -437 -9995 100 -439 fire
fill -9996 102 -437 -9996 102 -439 lava
fill -9927 90 -438 -9925 90 -435 lava replace air
setblock -9927 90 -433 minecraft:redstone_torch
fill -9927 90 -431 -9925 90 -429 lava replace air
setblock -9922 95 -429 lava
setblock -9985 117 -357 lava
setblock -9945 153 -418 air

fill -9992 89 -353 -9988 89 -357 glass
fill -9984 90 -361 -9996 90 -349 lava replace air

tellraw @a[tag=mg.flw] [{"text":"Lava has started flowing through the ","italic":true},{"text":"Green ","color":"green"},{"text":"pipe...","color":"white"}]
