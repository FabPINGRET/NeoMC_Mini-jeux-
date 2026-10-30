execute at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.wither_skeleton.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if score ios_humor_created bool matches 1 run setblock 9982 35 228 redstone_block

execute unless block 9982 35 228 redstone_block at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Ethqiketh","color":"dark_aqua"},{"text":"> This machine mixes vital humors to create life, but balancing them correctly is an art. If the incorrect humors are used, or in an incorrect order, the resulting lifeform will be ghastly. If only Ethqiketh could see how a balanced creature could be composed, it might produce a ","color":"white"},{"text":"feeling of great happiness","color":"red"},{"text":".","color":"white"}]

execute if block 9982 35 228 redstone_block at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Ethqiketh","color":"dark_aqua"},{"text":"> You did it, you created a balanced lifeform! The Doctor must have taught you everything he knows. This manifested a ","color":"white"},{"text":"strong feeling of happiness","color":"red"},{"text":" in the blackened bones of Ethqiketh.","color":"white"}]


execute if block 9982 35 228 redstone_block at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~2.25 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
