execute as @a[tag=mg.flw] at @s run playsound minecraft:entity.frog.death neutral @s ~ ~ ~ 1 0.7
execute as @a[tag=mg.flw] at @s run tellraw @s [{"text":"<"},{"text":"Frogcrates","color":"#44BBFF"},{"text":"> The way you arranged that furniture, it reminds me of how we had this room set up when we got work done on the house! We added a ","color":"white"},{"text":"door","color":"#44BBFF"},{"text":" in that left wall. There's something else wrong with this room too, if could only remember...","color":"white"}]

execute as @a[gamemode=!spectator,tag=mg.flw] positioned -11028 81 -38 run function summon:intrusive_thought
execute as @a[gamemode=!spectator,tag=mg.flw] positioned -11050 81 -38 run function summon:intrusive_thought

execute as @a[gamemode=!spectator,tag=mg.flw] positioned -11035 109 -45 run function summon:fell_notion
execute as @a[gamemode=!spectator,tag=mg.flw] positioned -11010 123 -171 run function summon:fell_notion
execute as @a[gamemode=!spectator,tag=mg.flw] positioned -11030 109 -124 run function summon:fell_notion
execute as @a[gamemode=!spectator,tag=mg.flw] positioned -11030 109 -124 run function summon:doubt
execute as @a[gamemode=!spectator,tag=mg.flw] positioned -11079 95 -182 run function summon:fell_notion

return 1
