kill @e[type=minecart,distance=..2]
summon minecart ~ ~ ~ {Invulnerable:1b,Tags:["valorforge_minecart"]}

execute as @a[gamemode=!spectator,tag=mg.flw] at @s run tag @e[tag=valorforge_minecart,distance=..15] add safe_minecart
kill @e[tag=valorforge_minecart,tag=!safe_minecart,distance=0..]
tag @e[distance=0..] remove safe_minecart
