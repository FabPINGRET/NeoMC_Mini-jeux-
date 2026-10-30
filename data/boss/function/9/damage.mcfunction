function boss:9/arena/dry_up

scoreboard players remove boss:wm BossHealth 1

execute if score boss:wm BossHealth matches 6 run bossbar set boss:wm value 6
execute if score boss:wm BossHealth matches 5 run bossbar set boss:wm value 5
execute if score boss:wm BossHealth matches 4 run bossbar set boss:wm value 4
execute if score boss:wm BossHealth matches 4 run setblock -11219 -35 -131 air
execute if score boss:wm BossHealth matches 4 run schedule function floaty:sched/boss/9/cutscene/phase2_1 2s
execute if score boss:wm BossHealth matches 4 run setblock -11219 -35 -131 air
execute if score boss:wm BossHealth matches 4 run schedule clear floaty:sched/boss/9/pick_attack
execute if score boss:wm BossHealth matches 4 run kill @e[tag=encruster,distance=0..]
execute if score boss:wm BossHealth matches 3 run bossbar set boss:wm value 3
execute if score boss:wm BossHealth matches 3 run bossbar set boss:wm color yellow
execute if score boss:wm BossHealth matches 3 run function boss:9/setup/3_to_other
execute if score boss:wm BossHealth matches 2 run bossbar set boss:wm value 2
execute if score boss:wm BossHealth matches 2 run function boss:9/move/speed/up
execute if score boss:wm BossHealth matches 1 run bossbar set boss:wm value 1
execute if score boss:wm BossHealth matches 1 run bossbar set boss:wm color red
execute if score boss:wm BossHealth matches 0 run bossbar set boss:wm value 0

execute if score boss:wm BossHealth matches 1 run function boss:9/arena/barnacle_kill
execute if score boss:wm BossHealth matches 1 run setblock -11219 -35 -131 air
execute if score boss:wm BossHealth matches 1 run schedule clear floaty:sched/boss/9/pick_attack
execute if score boss:wm BossHealth matches 1 run schedule function floaty:sched/boss/9/cutscene/dreadwarden_1 2s

execute if score boss:wm BossHealth matches 0 run schedule function floaty:sched/boss/9/win 0.1s
execute if score boss:wm BossHealth matches 0 run schedule function floaty:sched/boss/9/cutscene/lord_1 2s
