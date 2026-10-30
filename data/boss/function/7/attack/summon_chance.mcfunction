function boss:7/hand_position/none
execute store result score boss:st_summon_chance bool run random value 1..2
execute if score boss:st_summon_chance bool matches 1 run function boss:7/hand_frame/point_down
execute if score boss:st_summon_chance bool matches 1 positioned ~ -21 ~ run function summon:knucklehead
execute if score boss:st_summon_chance bool matches 1 positioned ~ -20 ~ run particle minecraft:egg_crack ~ ~ ~ 0.5 1 0.5 0 50
execute if score boss:st_summon_chance bool matches 1 positioned ~ -20 ~ run particle minecraft:block{block_state:"stone"} ~ ~ ~ 0.5 1 0.5 0 25
execute if score boss:st_summon_chance bool matches 1 run playsound minecraft:block.respawn_anchor.set_spawn hostile @a[tag=mg.flw] ~ -20 ~ 2 2
schedule function floaty:sched/boss/7/attack/summon_return 20t replace
