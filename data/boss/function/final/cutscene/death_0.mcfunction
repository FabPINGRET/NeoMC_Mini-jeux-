function music:end
setblock -12346 43 348 minecraft:air
kill @e[tag=wv_model_heart,distance=0..]

function boss:final/virus/model/bell

playsound minecraft:block.bell.use master @a[tag=mg.flw] -12384 123 355 6 1
playsound minecraft:block.bell.resonate master @a[tag=mg.flw] -12384 123 355 6 1

schedule function floaty:sched/boss/final/cutscene/death_1 2s replace
bossbar set boss:final players

#","color":"white"},{"text":"

tag @a[tag=mg.flw] remove bossroom
tag @a[tag=mg.flw] remove targeted
