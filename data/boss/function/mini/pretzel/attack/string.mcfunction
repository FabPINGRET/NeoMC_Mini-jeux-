execute as @a[gamemode=!spectator,tag=mg.flw] at @s run particle minecraft:block{block_state:"cobweb"} ~ ~1 ~ 0.5 0.8 0.5 0 100
execute as @a[gamemode=!spectator,sort=arbitrary,tag=mg.flw] run function boss:mini/pretzel/utility/rearrange
playsound minecraft:entity.breeze.charge hostile @a[tag=mg.flw] -10340 89 446 3 1

schedule function floaty:sched/boss/mini/pretzel/schedule_attack 3s
