execute positioned -12384 123 355 run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1 1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Scourgelord Morbex","color":"dark_aqua","bold":true},{"text":"> O, ","color":"white"},{"text":"Virus","color":"dark_aqua"},{"text":"! The ","color":"white"},{"text":"Bell of Life","color":"gold"},{"text":" is ours!","color":"white"},{"text":" ⇒","color":"light_purple"}]

spawnpoint @a[tag=mg.flw] -12342 128 355 90 0
scoreboard players set $flsp mg.st 2

schedule function floaty:sched/boss/final/cutscene/1 9s replace

#","color":"white"},{"text":"

function music:end
