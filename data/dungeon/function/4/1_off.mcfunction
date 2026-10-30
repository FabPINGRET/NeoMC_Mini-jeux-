fill -9990 113 -350 -9990 91 -351 air replace lava
fill -10012 94 -336 -10010 94 -336 air
fill -10012 93 -337 -10010 96 -337 air replace lava
fill -10004 91 -318 -10002 91 -320 air replace lava
fill -9998 91 -318 -9995 91 -321 air replace lava
setblock -9995 96 -324 air
setblock -10000 91 -318 air
setblock -9961 112 -317 air
clone -9992 73 -310 -9975 86 -302 -9991 91 -322
execute if block -9994 125 -357 air if block -9985 117 -357 air if block -9990 113 -350 air run fill -9996 90 -349 -9984 90 -361 air replace lava
execute if block -9994 125 -357 air if block -9985 117 -357 air if block -9990 113 -350 air run fill -9988 89 -353 -9992 89 -357 air
playsound minecraft:entity.generic.extinguish_fire master @a[tag=mg.flw] -10011 95 -337 1 0.1 1
playsound minecraft:entity.generic.extinguish_fire master @a[tag=mg.flw] -10011 95 -337 1 1 1
playsound minecraft:entity.generic.extinguish_fire master @a[tag=mg.flw] -10011 95 -337 1 2 1

tellraw @a[tag=mg.flw] [{"text":"Lava has stopped flowing through the ","italic":true},{"text":"Blue ","color":"blue"},{"text":"pipe...","color":"white"}]
