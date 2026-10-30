function boss:mini/eye_in_the_grove/bush_attack_end

spreadplayers -10060 336 6 9 false @e[tag=grove_eye_rand,distance=0..]
execute as @e[tag=grove_eye_rand,distance=0..] at @s unless block ~ 116 ~ air run tag @s add used
tag @e[tag=grove_eye_rand,tag=!used,sort=random,limit=1,distance=0..] add bush1
tag @n[tag=bush1,tag=grove_eye_rand,distance=0..] add used

tag @e[tag=grove_eye_rand,tag=!used,sort=random,limit=1,distance=0..] add bush2
tag @n[tag=bush2,tag=grove_eye_rand,distance=0..] add used

tag @e[tag=grove_eye_rand,tag=!used,sort=random,limit=1,distance=0..] add bush3
tag @n[tag=bush3,tag=grove_eye_rand,distance=0..] add used

tag @e[tag=grove_eye_rand,tag=!used,sort=random,limit=1,distance=0..] add bush4
tag @n[tag=bush4,tag=grove_eye_rand,distance=0..] add used

tag @e[tag=grove_eye_rand,tag=!used,sort=random,limit=1,distance=0..] add bush5
tag @n[tag=bush5,tag=grove_eye_rand,distance=0..] add used

tag @e[tag=grove_eye_rand,tag=!used,sort=random,limit=1,distance=0..] add bush6
tag @n[tag=bush6,tag=grove_eye_rand,distance=0..] add used

tag @e[tag=grove_eye_rand,tag=!used,sort=random,limit=1,distance=0..] add bush7
tag @n[tag=bush7,tag=grove_eye_rand,distance=0..] add used

tag @e[tag=grove_eye_rand,tag=!used,sort=random,limit=1,distance=0..] add monster1
tag @n[tag=monster1,tag=grove_eye_rand,distance=0..] add used

tag @e[tag=grove_eye_rand,tag=!used,sort=random,limit=1,distance=0..] add monster2
tag @n[tag=monster2,tag=grove_eye_rand,distance=0..] add used

setblock -10065 105 349 minecraft:redstone_block
