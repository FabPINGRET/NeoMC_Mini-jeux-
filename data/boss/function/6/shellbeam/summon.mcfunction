execute as @n[tag=boss_sh_loc,distance=0..] at @s positioned ^ ^2.5 ^-1 run summon armor_stand ~ ~ ~ {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_sh_shellbeam"],DisabledSlots:4144959}

execute as @n[tag=boss_sh_shellbeam,distance=0..] at @s facing entity @n[tag=boss_sh_loc,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
execute as @n[tag=boss_sh_shellbeam,distance=0..] at @s run tp @s ~ ~ ~ ~130 0

setblock -10462 42 -70 stone
setblock -10462 42 -68 minecraft:redstone_block
