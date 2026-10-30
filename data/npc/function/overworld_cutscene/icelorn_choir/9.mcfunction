function boss:mini/icelorn_choir/song/stop

schedule function floaty:sched/npc/overworld_cutscene/icelorn_choir/10 2s replace

execute as @e[tag=icelorn_corpse,distance=0..] run item replace entity @s armor.head from block -10056 105 188 container.0
execute as @e[tag=icelorn_corpse,distance=0..] run data modify entity @s equipment.chest.components."minecraft:trim".material set value netherite
execute as @e[tag=icelorn_corpse,distance=0..] run data modify entity @s equipment.legs.components."minecraft:trim".material set value netherite
execute as @e[tag=icelorn_corpse,distance=0..] run data modify entity @s equipment.feet.components."minecraft:trim".material set value netherite

#","color":"white"},{"text":"
