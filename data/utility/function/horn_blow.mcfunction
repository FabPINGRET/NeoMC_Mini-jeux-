execute positioned ~ ~-1 ~ run summon armor_stand ~ ~ ~ {NoGravity:1b,Invulnerable:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["horn_low","horn_stand"],DisabledSlots:4144959}
execute positioned ~ ~1 ~ run summon armor_stand ~ ~ ~ {NoGravity:1b,Invulnerable:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["horn_high","horn_stand"],DisabledSlots:4144959}

execute positioned ^ ^ ^1 run summon armor_stand ~ ~ ~ {NoGravity:1b,Invulnerable:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["horn_check"],DisabledSlots:4144959}

#HARM
execute as @s as @n[tag=horn_check,distance=0..] at @s as @n[tag=horn_stand,distance=0..] if entity @s[tag=horn_low] as @n[scores={horn_blow=1..},distance=0..] at @s run particle minecraft:angry_villager ~ ~1 ~ 3 3 3 0 50
execute as @s as @n[tag=horn_check,distance=0..] at @s as @n[tag=horn_stand,distance=0..] if entity @s[tag=horn_low] as @n[scores={horn_blow=1..},distance=0..] at @s as @e[tag=enemy,distance=..15] run damage @s 12 minecraft:magic by @n[scores={horn_blow=1..},distance=0..]

#HEAL
execute as @s as @n[tag=horn_check,distance=0..] at @s as @n[tag=horn_stand,distance=0..] if entity @s[tag=horn_high] as @n[scores={horn_blow=1..},distance=0..] at @s run particle minecraft:heart ~ ~1 ~ 3 3 3 0 50
execute as @s as @n[tag=horn_check,distance=0..] at @s as @n[tag=horn_stand,distance=0..] if entity @s[tag=horn_high] as @n[scores={horn_blow=1..},distance=0..] at @s run effect give @a[distance=..15,tag=mg.flw] minecraft:instant_health 1 1 true

kill @e[tag=horn_stand,distance=0..]
kill @e[tag=horn_check,distance=0..]
