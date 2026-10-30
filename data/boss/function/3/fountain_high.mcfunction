execute unless block -10122 174 -181 sandstone run summon area_effect_cloud ~ ~ ~ {Tags:["stal_temp","1","exclude"]}
execute unless block -10122 174 -189 sandstone run summon area_effect_cloud ~ ~ ~ {Tags:["stal_temp","2","exclude"]}
execute unless block -10122 174 -197 sandstone run summon area_effect_cloud ~ ~ ~ {Tags:["stal_temp","3","exclude"]}
execute unless block -10116 174 -203 sandstone run summon area_effect_cloud ~ ~ ~ {Tags:["stal_temp","4","exclude"]}
execute unless block -10108 174 -203 sandstone run summon area_effect_cloud ~ ~ ~ {Tags:["stal_temp","5","exclude"]}
execute unless block -10100 174 -203 sandstone run summon area_effect_cloud ~ ~ ~ {Tags:["stal_temp","6","exclude"]}
execute unless block -10094 174 -197 sandstone run summon area_effect_cloud ~ ~ ~ {Tags:["stal_temp","7","exclude"]}
execute unless block -10094 174 -189 sandstone run summon area_effect_cloud ~ ~ ~ {Tags:["stal_temp","8","exclude"]}
execute unless block -10094 174 -181 sandstone run summon area_effect_cloud ~ ~ ~ {Tags:["stal_temp","9","exclude"]}
execute unless block -10100 174 -175 sandstone run summon area_effect_cloud ~ ~ ~ {Tags:["stal_temp","10","exclude"]}
execute unless block -10108 174 -175 sandstone run summon area_effect_cloud ~ ~ ~ {Tags:["stal_temp","11","exclude"]}
execute unless block -10116 174 -175 sandstone run summon area_effect_cloud ~ ~ ~ {Tags:["stal_temp","12","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=stal_temp,limit=1,sort=random,distance=0..] remove exclude

kill @e[type=minecraft:area_effect_cloud,tag=stal_temp,tag=exclude,distance=0..]

# WORM SPAWN CHANCE
summon area_effect_cloud ~ ~ ~ {Tags:["lod_boss_w_spawn_temp","1","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["lod_boss_w_spawn_temp","2","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["lod_boss_w_spawn_temp","2","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=lod_boss_w_spawn_temp,limit=1,sort=random,distance=0..] remove exclude

kill @e[type=minecraft:area_effect_cloud,tag=lod_boss_w_spawn_temp,tag=exclude,distance=0..]

execute if entity @e[tag=stal_temp,tag=1,distance=0..] run particle block{block_state:"minecraft:sandstone"} -10122 160 -181 0.5 10 0.5 0 300 force
execute if entity @e[tag=stal_temp,tag=1,distance=0..] run function boss:3/stal/1
execute if entity @e[tag=stal_temp,tag=1,distance=0..] if entity @e[tag=lod_boss_w_spawn_temp,tag=1,distance=0..] positioned -10122 146 -181 as @a[gamemode=!spectator,tag=mg.flw] run function summon:wyrm_spawn
execute if entity @e[tag=stal_temp,tag=2,distance=0..] run particle block{block_state:"minecraft:sandstone"} -10122 160 -189 0.5 10 0.5 0 300 force
execute if entity @e[tag=stal_temp,tag=2,distance=0..] run function boss:3/stal/2
execute if entity @e[tag=stal_temp,tag=2,distance=0..] if entity @e[tag=lod_boss_w_spawn_temp,tag=1,distance=0..] positioned -10122 146 -189 as @a[gamemode=!spectator,tag=mg.flw] run function summon:wyrm_spawn
execute if entity @e[tag=stal_temp,tag=3,distance=0..] run particle block{block_state:"minecraft:sandstone"} -10122 160 -197 0.5 10 0.5 0 300 force
execute if entity @e[tag=stal_temp,tag=3,distance=0..] run function boss:3/stal/3
execute if entity @e[tag=stal_temp,tag=3,distance=0..] if entity @e[tag=lod_boss_w_spawn_temp,tag=1,distance=0..] positioned -10122 146 -197 as @a[gamemode=!spectator,tag=mg.flw] run function summon:wyrm_spawn
execute if entity @e[tag=stal_temp,tag=4,distance=0..] run particle block{block_state:"minecraft:sandstone"} -10116 160 -203 0.5 10 0.5 0 300 force
execute if entity @e[tag=stal_temp,tag=4,distance=0..] run function boss:3/stal/4
execute if entity @e[tag=stal_temp,tag=4,distance=0..] if entity @e[tag=lod_boss_w_spawn_temp,tag=1,distance=0..] positioned -10116 146 -203 as @a[gamemode=!spectator,tag=mg.flw] run function summon:wyrm_spawn
execute if entity @e[tag=stal_temp,tag=5,distance=0..] run particle block{block_state:"minecraft:sandstone"} -10108 160 -203 0.5 10 0.5 0 300 force
execute if entity @e[tag=stal_temp,tag=5,distance=0..] run function boss:3/stal/5
execute if entity @e[tag=stal_temp,tag=5,distance=0..] if entity @e[tag=lod_boss_w_spawn_temp,tag=1,distance=0..] positioned -10108 146 -203 as @a[gamemode=!spectator,tag=mg.flw] run function summon:wyrm_spawn
execute if entity @e[tag=stal_temp,tag=6,distance=0..] run particle block{block_state:"minecraft:sandstone"} -10100 160 -203 0.5 10 0.5 0 300 force
execute if entity @e[tag=stal_temp,tag=6,distance=0..] run function boss:3/stal/6
execute if entity @e[tag=stal_temp,tag=6,distance=0..] if entity @e[tag=lod_boss_w_spawn_temp,tag=1,distance=0..] positioned -10100 146 -203 as @a[gamemode=!spectator,tag=mg.flw] run function summon:wyrm_spawn
execute if entity @e[tag=stal_temp,tag=7,distance=0..] run particle block{block_state:"minecraft:sandstone"} -10094 160 -197 0.5 10 0.5 0 300 force
execute if entity @e[tag=stal_temp,tag=7,distance=0..] run function boss:3/stal/7
execute if entity @e[tag=stal_temp,tag=7,distance=0..] if entity @e[tag=lod_boss_w_spawn_temp,tag=1,distance=0..] positioned -10094 146 -197 as @a[gamemode=!spectator,tag=mg.flw] run function summon:wyrm_spawn
execute if entity @e[tag=stal_temp,tag=8,distance=0..] run particle block{block_state:"minecraft:sandstone"} -10094 160 -189 0.5 10 0.5 0 300 force
execute if entity @e[tag=stal_temp,tag=8,distance=0..] run function boss:3/stal/8
execute if entity @e[tag=stal_temp,tag=8,distance=0..] if entity @e[tag=lod_boss_w_spawn_temp,tag=1,distance=0..] positioned -10094 146 -189 as @a[gamemode=!spectator,tag=mg.flw] run function summon:wyrm_spawn
execute if entity @e[tag=stal_temp,tag=9,distance=0..] run particle block{block_state:"minecraft:sandstone"} -10094 160 -181 0.5 10 0.5 0 300 force
execute if entity @e[tag=stal_temp,tag=9,distance=0..] run function boss:3/stal/9
execute if entity @e[tag=stal_temp,tag=9,distance=0..] if entity @e[tag=lod_boss_w_spawn_temp,tag=1,distance=0..] positioned -10094 146 -181 as @a[gamemode=!spectator,tag=mg.flw] run function summon:wyrm_spawn
execute if entity @e[tag=stal_temp,tag=10,distance=0..] run particle block{block_state:"minecraft:sandstone"} -10100 160 -175 0.5 10 0.5 0 300 force
execute if entity @e[tag=stal_temp,tag=10,distance=0..] run function boss:3/stal/10
execute if entity @e[tag=stal_temp,tag=10,distance=0..] if entity @e[tag=lod_boss_w_spawn_temp,tag=1,distance=0..] positioned -10100 146 -175 as @a[gamemode=!spectator,tag=mg.flw] run function summon:wyrm_spawn
execute if entity @e[tag=stal_temp,tag=11,distance=0..] run particle block{block_state:"minecraft:sandstone"} -10108 160 -175 0.5 10 0.5 0 300 force
execute if entity @e[tag=stal_temp,tag=11,distance=0..] run function boss:3/stal/11
execute if entity @e[tag=stal_temp,tag=11,distance=0..] if entity @e[tag=lod_boss_w_spawn_temp,tag=1,distance=0..] positioned -10108 146 -175 as @a[gamemode=!spectator,tag=mg.flw] run function summon:wyrm_spawn
execute if entity @e[tag=stal_temp,tag=12,distance=0..] run particle block{block_state:"minecraft:sandstone"} -10116 160 -175 0.5 10 0.5 0 300 force
execute if entity @e[tag=stal_temp,tag=12,distance=0..] run function boss:3/stal/12
execute if entity @e[tag=stal_temp,tag=12,distance=0..] if entity @e[tag=lod_boss_w_spawn_temp,tag=1,distance=0..] positioned -10116 146 -175 as @a[gamemode=!spectator,tag=mg.flw] run function summon:wyrm_spawn

kill @e[type=minecraft:area_effect_cloud,tag=lod_boss_w_spawn_temp,distance=0..]

execute unless entity @e[tag=stal_temp,distance=0..] run function boss:3/bite_attack_start

execute if entity @e[tag=stal_temp,distance=0..] run setblock -10083 134 -201 minecraft:redstone_block

kill @e[type=minecraft:area_effect_cloud,tag=stal_temp,distance=0..]
