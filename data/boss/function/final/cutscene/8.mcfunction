execute positioned -12384 123 355 run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1 1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Scourgelord Morbex","color":"dark_aqua","bold":true},{"text":"> GAHHHH!!!","color":"white"},{"text":" ⇒","color":"light_purple"}]

function boss:final/virus/setup/lords

schedule function floaty:sched/boss/final/cutscene/9 6s replace

#","color":"white"},{"text":"
