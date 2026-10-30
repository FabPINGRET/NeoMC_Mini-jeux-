fill -9995 100 -437 -9995 100 -439 air
fill -9996 102 -437 -9996 99 -439 air replace lava
fill -9927 90 -438 -9925 90 -435 air replace lava
setblock -9927 90 -433 air
fill -9925 90 -429 -9927 90 -431 air replace lava
setblock -9922 95 -429 air
fill -9985 117 -357 -9986 91 -357 air replace lava

execute if block -9994 125 -357 air if block -9985 117 -357 air if block -9990 113 -350 air run fill -9996 90 -349 -9984 90 -361 air replace lava
execute if block -9994 125 -357 air if block -9985 117 -357 air if block -9990 113 -350 air run fill -9988 89 -353 -9992 89 -357 air
playsound minecraft:entity.generic.extinguish_fire master @a[tag=mg.flw] -9996 101 -438 1 0.1 1
playsound minecraft:entity.generic.extinguish_fire master @a[tag=mg.flw] -9996 101 -438 1 1 1
playsound minecraft:entity.generic.extinguish_fire master @a[tag=mg.flw] -9996 101 -438 1 2 1

tellraw @a[tag=mg.flw] [{"text":"Lava has stopped flowing through the ","italic":true},{"text":"Green ","color":"green"},{"text":"pipe...","color":"white"}]
