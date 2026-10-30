execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run fill ~-1 ~ ~-1 ~1 ~5 ~1 air
execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run clone -10183 72 457 -10181 79 459 ~-1 ~ ~-1
summon slime -10222 93 434 {NoGravity:1b,Silent:1b,Invulnerable:1b,Glowing:1b,Team:"NoCollide",PersistenceRequired:1b,NoAI:1b,Health:999f,Size:0,Tags:["boss_skt_ecto_tele"],active_effects:[{id:"minecraft:invisibility",amplifier:0,duration:-1,show_particles:0b}],attributes:[{id:"minecraft:attack_damage",base:0},{id:"minecraft:attack_knockback",base:0},{id:"minecraft:attack_speed",base:0},{id:"minecraft:max_health",base:999}]}
schedule function floaty:sched/boss/5/ectobeam/attack_execute 1.5s replace
