tag @e[tag=mind_boss_rand,tag=!picked,limit=1,sort=random,distance=0..] add new_picked
tag @e[tag=mind_boss_rand,tag=new_picked,distance=0..] add picked
tag @e[tag=mind_boss_rand,tag=new_picked,distance=0..] add 9

execute as @e[tag=mind_boss_rand,tag=9,distance=0..] at @s run playsound minecraft:block.sand.break hostile @a[tag=mg.flw] ~ 173 ~ 1 1
execute as @e[tag=mind_boss_rand,tag=9,distance=0..] at @s run fill ~ 173 ~ ~ 176 ~ structure_void replace air
execute as @e[tag=mind_boss_rand,tag=9,distance=0..] at @s run fill ~ 173 ~ ~ 175 ~ cactus replace structure_void strict
execute as @e[tag=mind_boss_rand,tag=9,distance=0..] at @s run particle minecraft:block{block_state:"red_sand"} ~ 173 ~ 0.4 0.4 0.4 0 40

execute as @e[tag=mind_boss_rand,tag=4,distance=0..] at @s run setblock ~ 175 ~ structure_void strict
execute as @e[tag=mind_boss_rand,tag=2,distance=0..] at @s run setblock ~ 174 ~ structure_void strict
execute as @e[tag=mind_boss_rand,tag=0,distance=0..] at @s run setblock ~ 173 ~ structure_void strict

execute as @e[tag=mind_boss_rand,tag=0,distance=0..] at @s run particle dust_color_transition{from_color:[1.000,0.431,0.792],to_color:[0.059,1.000,0.529],scale:3} ~ 173.5 ~ 0.3 0.3 0.3 1 50 normal
execute as @e[tag=mind_boss_rand,tag=0,distance=0..] at @s run particle dust_color_transition{from_color:[1.000,0.431,0.792],to_color:[0.059,1.000,0.529],scale:2} ~ 173.5 ~ 1 1 1 1 100 normal
execute as @e[tag=mind_boss_rand,tag=0,distance=0..] at @s run particle dust_color_transition{from_color:[1.000,0.431,0.792],to_color:[0.059,1.000,0.529],scale:1} ~ 173.5 ~ 1.5 1.5 1.5 1 100 normal
execute as @e[tag=mind_boss_rand,tag=0,distance=0..] at @s run fill ~1 172 ~3 ~-1 172 ~-3 pink_concrete_powder replace red_sand
execute as @e[tag=mind_boss_rand,tag=0,distance=0..] at @s run fill ~3 172 ~1 ~-3 172 ~-1 pink_concrete_powder replace red_sand
execute as @e[tag=mind_boss_rand,tag=0,distance=0..] at @s run fill ~2 172 ~2 ~-2 172 ~-2 pink_concrete_powder replace red_sand

execute as @e[tag=mind_boss_rand,tag=0,distance=0..] at @s run playsound minecraft:block.conduit.deactivate hostile @a[tag=mg.flw] ~ 173 ~ 1 2
execute as @e[tag=mind_boss_rand,tag=0,distance=0..] at @s positioned ~ 173 ~ as @a[distance=..4,tag=mg.flw] run effect give @s minecraft:nausea 15 0 true
execute store result score cactus_bomb_burst_chance Value run random value 1..4
execute as @e[tag=mind_boss_rand,tag=0,distance=0..] at @s if score cactus_bomb_burst_chance Value matches 1 positioned ~ 173 ~ run function boss:mini/mind_contagion/attacks/cactus_burst


tag @e[tag=mind_boss_rand,tag=9,distance=0..] add 9_to_8
tag @e[tag=mind_boss_rand,tag=8,distance=0..] add 8_to_7
tag @e[tag=mind_boss_rand,tag=7,distance=0..] add 7_to_6
tag @e[tag=mind_boss_rand,tag=6,distance=0..] add 6_to_5
tag @e[tag=mind_boss_rand,tag=5,distance=0..] add 5_to_4
tag @e[tag=mind_boss_rand,tag=4,distance=0..] add 4_to_3
tag @e[tag=mind_boss_rand,tag=3,distance=0..] add 3_to_2
tag @e[tag=mind_boss_rand,tag=2,distance=0..] add 2_to_1
tag @e[tag=mind_boss_rand,tag=1,distance=0..] add 1_to_0
tag @e[tag=mind_boss_rand,tag=0,distance=0..] add 0_to_z

tag @e[tag=mind_boss_rand,tag=9_to_8,distance=0..] remove 9
tag @e[tag=mind_boss_rand,tag=9_to_8,distance=0..] add 8

tag @e[tag=mind_boss_rand,tag=8_to_7,distance=0..] remove 8
tag @e[tag=mind_boss_rand,tag=8_to_7,distance=0..] add 7

tag @e[tag=mind_boss_rand,tag=7_to_6,distance=0..] remove 7
tag @e[tag=mind_boss_rand,tag=7_to_6,distance=0..] add 6

tag @e[tag=mind_boss_rand,tag=6_to_5,distance=0..] remove 6
tag @e[tag=mind_boss_rand,tag=6_to_5,distance=0..] add 5

tag @e[tag=mind_boss_rand,tag=5_to_4,distance=0..] remove 5
tag @e[tag=mind_boss_rand,tag=5_to_4,distance=0..] add 4

tag @e[tag=mind_boss_rand,tag=4_to_3,distance=0..] remove 4
tag @e[tag=mind_boss_rand,tag=4_to_3,distance=0..] add 3

tag @e[tag=mind_boss_rand,tag=3_to_2,distance=0..] remove 3
tag @e[tag=mind_boss_rand,tag=3_to_2,distance=0..] add 2

tag @e[tag=mind_boss_rand,tag=2_to_1,distance=0..] remove 2
tag @e[tag=mind_boss_rand,tag=2_to_1,distance=0..] add 1

tag @e[tag=mind_boss_rand,tag=1_to_0,distance=0..] remove 1
tag @e[tag=mind_boss_rand,tag=1_to_0,distance=0..] add 0

tag @e[tag=mind_boss_rand,tag=0_to_z,distance=0..] remove 0
tag @e[tag=mind_boss_rand,tag=0_to_z,distance=0..] remove cactus_bomb_pool

tag @e[tag=mind_boss_rand,distance=0..] remove new_picked
tag @e[tag=mind_boss_rand,distance=0..] remove 9_to_8
tag @e[tag=mind_boss_rand,distance=0..] remove 8_to_7
tag @e[tag=mind_boss_rand,distance=0..] remove 7_to_6
tag @e[tag=mind_boss_rand,distance=0..] remove 6_to_5
tag @e[tag=mind_boss_rand,distance=0..] remove 5_to_4
tag @e[tag=mind_boss_rand,distance=0..] remove 4_to_3
tag @e[tag=mind_boss_rand,distance=0..] remove 3_to_2
tag @e[tag=mind_boss_rand,distance=0..] remove 2_to_1
tag @e[tag=mind_boss_rand,distance=0..] remove 1_to_0
tag @e[tag=mind_boss_rand,distance=0..] remove 0_to_z

execute if entity @e[tag=mind_boss_rand,tag=cactus_bomb_pool,distance=0..] run schedule function floaty:sched/boss/mini/mind_contagion/attacks/cactus_bomb_tick 6t replace
execute unless entity @e[tag=mind_boss_rand,tag=cactus_bomb_pool,distance=0..] run schedule function floaty:sched/boss/mini/mind_contagion/attacks/cactus_bomb_end 2s replace
