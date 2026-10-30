execute unless entity @a[gamemode=!spectator,tag=bossroom,tag=targeted,tag=mg.flw] run schedule function floaty:sched/boss/7/target_check 2s replace
execute if entity @a[gamemode=!spectator,tag=bossroom,tag=targeted,tag=mg.flw] run function boss:7/pick_attack
