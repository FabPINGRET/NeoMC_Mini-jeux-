kill @e[tag=mutarid_strong,distance=0..]
tp @a[tag=mg.flw] -12359 123 355 90 0
fill -12362 123 360 -12356 127 360 barrier
fill -12362 123 350 -12362 127 360 barrier
fill -12362 127 350 -12356 123 350 barrier
fill -12356 127 350 -12356 123 360 barrier
fill -12357 127 360 -12362 127 350 barrier
playsound minecraft:entity.player.teleport master @a[tag=mg.flw] -12359 123 355 2 1

#start stand face player
setblock -12346 43 336 minecraft:redstone_block

tp @n[tag=lord_morbex_stand,distance=0..] -12384 130 355
function boss:final/morbex/equipment/no_sword
function boss:final/morbex/equipment/armor
function boss:final/morbex/pose/neutral

schedule function floaty:sched/boss/final/cutscene/5 3s replace
