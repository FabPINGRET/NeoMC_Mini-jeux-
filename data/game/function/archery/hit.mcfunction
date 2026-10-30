fill ~-1 ~-1 ~-1 ~1 ~1 ~1 chiseled_sandstone replace target
scoreboard players add archery_points Value 1
execute positioned 113 40 164 run give @p[gamemode=!spectator,tag=mg.flw] arrow
playsound minecraft:block.note_block.bell master @a[tag=mg.flw] ~ ~ ~ 2 0.5

execute unless block 126 50 168 minecraft:target unless block 126 50 172 minecraft:target unless block 126 46 168 minecraft:target unless block 126 46 172 minecraft:target unless block 126 42 168 minecraft:target unless block 126 42 172 minecraft:target unless block 117 50 180 minecraft:target unless block 113 50 180 minecraft:target unless block 109 50 180 minecraft:target unless block 117 46 180 minecraft:target unless block 113 46 180 minecraft:target unless block 109 46 180 minecraft:target unless block 117 42 180 minecraft:target unless block 113 42 180 minecraft:target unless block 109 42 180 minecraft:target unless block 100 50 172 minecraft:target unless block 100 50 168 minecraft:target unless block 100 46 172 minecraft:target unless block 100 46 168 minecraft:target unless block 100 42 172 minecraft:target unless block 100 42 168 minecraft:target run schedule function floaty:sched/game/archery/next_frame 10t
