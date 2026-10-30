particle minecraft:cherry_leaves ~ ~ ~ 0.1 0.1 0.1 0 1

execute unless block ^ ^ ^ air run playsound minecraft:block.azalea.break hostile @a[tag=mg.flw] ~ ~ ~ 1 0.1
execute unless block ^ ^ ^ air run playsound minecraft:block.bamboo.break hostile @a[tag=mg.flw] ~ ~ ~ 1 1
execute unless block ^ ^ ^ air run playsound minecraft:item.bucket.empty_powder_snow hostile @a[tag=mg.flw] ~ ~ ~ 1 2
execute unless block ^ ^ ^ air run playsound minecraft:item.trident.return hostile @a[tag=mg.flw] ~ ~ ~ 1 0.1
execute unless block ^ ^ ^ air run summon armor_stand ~ ~ ~ {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["cherry_bomb_loc"],DisabledSlots:4144959}
execute unless block ^ ^ ^ air run function boss:1/summon_flowerbomb
execute unless block ^ ^ ^ air run schedule function floaty:sched/boss/1/cherry_explode 3s

execute if block ^ ^ ^ air positioned ^ ^ ^0.1 run function boss:1/cherry_ray
