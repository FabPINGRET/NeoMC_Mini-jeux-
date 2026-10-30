execute positioned -12384 123 355 run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1 1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Scourgelord Morbex","color":"dark_aqua","bold":true},{"text":"> O, ","color":"white"},{"text":"Hero","color":"gold"},{"text":". You stand alone.","color":"white"}]

#Start health tracking
setblock -12346 43 383 minecraft:redstone_block

schedule function floaty:sched/boss/final/cutscene/3 6s replace

#","color":"white"},{"text":"
