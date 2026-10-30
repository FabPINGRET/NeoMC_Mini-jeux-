summon area_effect_cloud -10106 133 -187 {Tags:["lod_boss_pick_temp","1","exclude"]}
summon area_effect_cloud -10106 133 -187 {Tags:["lod_boss_pick_temp","1","exclude"]}

execute if entity @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] if block -10083 158 -184 sand run summon area_effect_cloud -10106 133 -187 {Tags:["lod_boss_pick_temp","2","exclude"]}
execute if entity @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] if block -10083 158 -184 sand run summon area_effect_cloud -10106 133 -187 {Tags:["lod_boss_pick_temp","2","exclude"]}
execute if entity @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] if block -10083 158 -184 sand run summon area_effect_cloud -10106 133 -187 {Tags:["lod_boss_pick_temp","2","exclude"]}

execute if entity @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] if block -10083 158 -184 air run summon area_effect_cloud -10106 133 -187 {Tags:["lod_boss_pick_temp","3","exclude"]}
execute if entity @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] if block -10083 158 -184 air run summon area_effect_cloud -10106 133 -187 {Tags:["lod_boss_pick_temp","3","exclude"]}
execute if entity @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] if block -10083 158 -184 air run summon area_effect_cloud -10106 133 -187 {Tags:["lod_boss_pick_temp","3","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=lod_boss_pick_temp,limit=1,sort=random,distance=0..] remove exclude

kill @e[type=minecraft:area_effect_cloud,tag=lod_boss_pick_temp,tag=exclude,distance=0..]

execute if entity @e[tag=lod_boss_pick_temp,tag=1,distance=0..] run function boss:3/bite_attack_start
execute if entity @e[tag=lod_boss_pick_temp,tag=2,distance=0..] run function boss:3/fountain_low
execute if entity @e[tag=lod_boss_pick_temp,tag=3,distance=0..] run function boss:3/fountain_high


kill @e[type=minecraft:area_effect_cloud,tag=lod_boss_pick_temp,distance=0..]
