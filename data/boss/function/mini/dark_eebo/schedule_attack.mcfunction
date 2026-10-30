execute if score boss:deebo BossHealth matches 4..6 unless block -11549 173 -171 minecraft:white_wool if block -11551 173 -171 stone run schedule function floaty:sched/boss/mini/dark_eebo/pick_attack 4s replace
execute if score boss:deebo BossHealth matches 2..3 unless block -11549 173 -171 minecraft:white_wool if block -11551 173 -171 stone run schedule function floaty:sched/boss/mini/dark_eebo/pick_attack 3s replace
execute if score boss:deebo BossHealth matches 1 unless block -11549 173 -171 minecraft:white_wool if block -11551 173 -171 stone run schedule function floaty:sched/boss/mini/dark_eebo/pick_attack 2s replace

execute if block -11549 173 -171 minecraft:white_wool if block -11551 173 -171 stone run schedule function floaty:sched/boss/mini/dark_eebo/attack/deebo_out_start 2s replace
