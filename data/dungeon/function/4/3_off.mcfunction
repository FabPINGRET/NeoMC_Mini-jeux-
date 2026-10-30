fill -9944 93 -242 -9946 93 -242 air
fill -9944 95 -241 -9946 92 -241 air replace lava
fill -9943 90 -262 -9941 90 -264 air replace lava
fill -9941 90 -268 -9940 90 -271 air replace lava
setblock -9941 90 -266 air
setblock -9937 95 -271 air
fill -9994 125 -357 -9993 91 -357 air replace lava

execute if block -9994 125 -357 air if block -9985 117 -357 air if block -9990 113 -350 air run fill -9996 90 -349 -9984 90 -361 air replace lava
execute if block -9994 125 -357 air if block -9985 117 -357 air if block -9990 113 -350 air run fill -9988 89 -353 -9992 89 -357 air
playsound minecraft:entity.generic.extinguish_fire master @a[tag=mg.flw] -9945 94 -241 1 0.1 1
playsound minecraft:entity.generic.extinguish_fire master @a[tag=mg.flw] -9945 94 -241 1 1 1
playsound minecraft:entity.generic.extinguish_fire master @a[tag=mg.flw] -9945 94 -241 1 2 1

tellraw @a[tag=mg.flw] [{"text":"Lava has stopped flowing through the ","italic":true},{"text":"Red ","color":"red"},{"text":"pipe...","color":"white"}]
