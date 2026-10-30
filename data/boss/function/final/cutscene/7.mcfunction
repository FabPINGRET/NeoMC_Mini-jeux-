function boss:final/morbex/pose/transforming

execute at @n[tag=lord_morbex_stand,distance=0..] run playsound minecraft:entity.creaking.activate master @a[tag=mg.flw] ~ ~ ~ 4 1
execute positioned -12384 123 355 run playsound minecraft:block.bell.use master @a[tag=mg.flw] ~ ~ ~ 5 0.5

#Start transforming tick
setblock -12346 43 344 minecraft:redstone_block
#Stop facing player
setblock -12346 43 336 air

schedule function floaty:sched/boss/final/cutscene/8 3s replace

#","color":"white"},{"text":"
