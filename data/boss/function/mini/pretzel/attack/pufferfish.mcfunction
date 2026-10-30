summon pufferfish -10335 98 451 {PersistenceRequired:1b,Tags:["pretzel_pufferfish","enemy"],attributes:[{id:"minecraft:safe_fall_distance",base:100}]}
summon pufferfish -10345 98 451 {PersistenceRequired:1b,Tags:["pretzel_pufferfish","enemy"],attributes:[{id:"minecraft:safe_fall_distance",base:100}]}
summon pufferfish -10345 98 441 {PersistenceRequired:1b,Tags:["pretzel_pufferfish","enemy"],attributes:[{id:"minecraft:safe_fall_distance",base:100}]}
summon pufferfish -10335 98 441 {PersistenceRequired:1b,Tags:["pretzel_pufferfish","enemy"],attributes:[{id:"minecraft:safe_fall_distance",base:100}]}


particle minecraft:splash -10335 98 451 0.2 0.2 0.2 0 50
particle minecraft:splash -10345 98 451 0.2 0.2 0.2 0 50
particle minecraft:splash -10345 98 441 0.2 0.2 0.2 0 50
particle minecraft:splash -10335 98 441 0.2 0.2 0.2 0 50

playsound minecraft:entity.generic.splash hostile @a[tag=mg.flw] -10335 98 451 2 1
playsound minecraft:entity.generic.splash hostile @a[tag=mg.flw] -10345 98 451 2 1
playsound minecraft:entity.generic.splash hostile @a[tag=mg.flw] -10345 98 441 2 1
playsound minecraft:entity.generic.splash hostile @a[tag=mg.flw] -10335 98 441 2 1

schedule function floaty:sched/boss/mini/pretzel/schedule_attack 3s
