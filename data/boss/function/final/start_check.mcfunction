execute as @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] at @s unless block ~ ~ ~ light run tag @s add no_light
execute if entity @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] unless entity @a[tag=bossroom,tag=no_light,tag=mg.flw] run setblock -12346 43 340 air
execute if entity @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] unless entity @a[tag=bossroom,tag=no_light,tag=mg.flw] run schedule function floaty:sched/boss/final/cutscene/0 3s replace
tag @a[tag=mg.flw] remove no_light
