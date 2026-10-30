bossbar set boss:eye_in_the_grove value 60
bossbar set boss:eye_in_the_grove color green
bossbar set boss:eye_in_the_grove players

kill @n[tag=g_eye_boss,distance=0..]
kill @n[tag=grove_eye_horse,distance=0..]
kill @e[tag=scleratic,distance=0..]

tp @n[tag=grove_eye_cutscene,distance=0..] -10060 117 328 180 0

setblock -10044 105 327 air
setblock -10063 105 349 minecraft:black_wool
fill -10046 106 330 -10046 106 332 air
setblock -10044 105 323 air
setblock -10044 106 334 air
setblock -10059 105 349 air

scoreboard players set grove_eye_horse_mode Value 0
