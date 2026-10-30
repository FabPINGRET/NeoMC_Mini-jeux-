summon skeleton_horse -10060 116 328 {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["grove_eye_horse"]}
execute as @n[tag=grove_eye_pivot,distance=0..] at @s run tp @s ~ ~ ~ 180 0
scoreboard players set grove_eye_horse_mode Value 1
