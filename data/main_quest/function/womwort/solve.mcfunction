fill 10669 78 -74 10671 81 -74 air replace minecraft:lapis_block
fill 10662 78 -71 10662 79 -56 air replace minecraft:polished_blackstone_button

playsound minecraft:zelda.secret master @a[tag=mg.flw] 10670 78 -73 1 1 1

data modify entity @n[tag=meekwy,distance=0..] Rotation set value [165.0f,0.0f]
execute positioned 10671 78 -66 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7
execute positioned 10671 78 -66 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..20,tag=mg.flw] [{"text":"<"},{"text":"Trusted Meekwy","color":"#44BBFF"},{"text":"> That's right! Womwort's high priest is... me! I remember how to open his sanctum! And... whoa, who is that?","color":"white"}]
