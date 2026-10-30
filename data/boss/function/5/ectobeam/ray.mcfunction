#summon slime ~ ~-200 ~ {Silent:1b,Invulnerable:1b,Glowing:1b,CustomNameVisible:0b,Team:"NoCollide",PersistenceRequired:1b,NoAI:1b,Health:999f,Size:0,Tags:["boss_skt_ectobeam_slime"],CustomName:'"Ectobeam"',active_effects:[{id:"minecraft:invisibility",amplifier:1,duration:-1,show_particles:0b}],attributes:[{id:"minecraft:attack_damage",base:0},{id:"minecraft:attack_knockback",base:0},{id:"minecraft:attack_speed",base:0},{id:"minecraft:max_health",base:999},{id:"minecraft:scale",base:0.5}]}

summon block_display ~ ~ ~ {NoGravity:1b,Silent:1b,Glowing:1b,CustomNameVisible:0b,Tags:["boss_skt_ectobeam_slime"],CustomName:'"Ectobeam"',glow_color_override:5635925,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]},block_state:{Name:"minecraft:cobweb"}}

execute unless block ^ ^ ^ air unless block ^ ^ ^ lime_stained_glass unless block ^ ^ ^ white_stained_glass run playsound minecraft:block.sweet_berry_bush.break hostile @a[tag=mg.flw] ~ ~ ~ 2 2
execute unless block ^ ^ ^ air unless block ^ ^ ^ lime_stained_glass unless block ^ ^ ^ white_stained_glass run playsound minecraft:entity.bee.sting master @a[tag=mg.flw] ~ ~ ~ 2 1

scoreboard players add boss:skt_ectobeam shortray 1

execute if score boss:skt_ectobeam shortray matches ..400 if block ^ ^ ^ air positioned ^ ^ ^0.1 run function boss:5/ectobeam/ray
execute if score boss:skt_ectobeam shortray matches ..400 if block ^ ^ ^ lime_stained_glass positioned ^ ^ ^0.1 run function boss:5/ectobeam/ray
execute if score boss:skt_ectobeam shortray matches ..400 if block ^ ^ ^ white_stained_glass positioned ^ ^ ^0.1 run function boss:5/ectobeam/ray
