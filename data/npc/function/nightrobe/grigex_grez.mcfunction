execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.strider.happy neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute if score Inventory FeatherBrush matches 0 unless block 283 56 -162 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Grigex-Grez","color":"light_purple"},{"text":"> We've completely tied off the section of space around the","color":"white"},{"text":" dust contagion","color":"gold"},{"text":". It's slowed the spread but not eliminated the threat. Go up from here to the ","color":"white"},{"text":"Warped Land","color":"light_purple"},{"text":", there you will find the Mindczar waiting for you in ","color":"white"},{"text":"Limbohold","color":"light_purple"},{"text":". She can create a blade for you able to sever this spacial knot.","color":"white"}]
execute if score Inventory FeatherBrush matches 0 if block 283 56 -162 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Grigex-Grez","color":"light_purple"},{"text":"> You've severed the knot! Good luck in there.","color":"white"}]

execute if score Inventory FeatherBrush matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Grigex-Grez","color":"light_purple"},{"text":"> Do you hear it? The creaking of the world before it tears? It reverberates through the sky over these Isles.","color":"white"},{"text":" Talk to the Mindczar","color":"light_purple"},{"text":", right away. I'll see you soon.","color":"white"}]
execute if score Inventory FeatherBrush matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] at @s run playsound minecraft:ambient.soul_sand_valley.mood master @s ~ ~ ~ 1 0.1
execute if score Inventory FeatherBrush matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] at @s run playsound minecraft:ambient.soul_sand_valley.mood master @s ~ ~ ~ 1 0.1
execute if score Inventory FeatherBrush matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] at @s run playsound minecraft:ambient.soul_sand_valley.mood master @s ~ ~ ~ 1 0.1
execute if score Inventory FeatherBrush matches 1 run setblock 288 49 -176 redstone_block
execute if score Inventory FeatherBrush matches 1 run scoreboard players set mindczar Story 4
#Quest Marker on Mindczar
execute if score Inventory FeatherBrush matches 1 run setblock -9769 268 422 minecraft:redstone_block

execute positioned 285 58 -162 run kill @e[tag=quest_marker,distance=..4]
execute positioned 283 58 -173 run kill @e[tag=quest_marker,distance=..4]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
