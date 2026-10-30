#Stop bossbar tracking and miniboss things
setblock 10014 91 -103 minecraft:air

tp @n[tag=morbex_valor_tower,distance=0..] 10022 94 -98 0 0
particle minecraft:trial_spawner_detection_ominous 10022 95 -98 0.3 0.5 0.3 0 100
bossbar set boss:morbex players

execute at @n[tag=l_morbex_1,distance=0..] run particle minecraft:trial_spawner_detection_ominous ~ ~1 ~ 0.3 0.5 0.3 0 100
execute at @n[tag=l_morbex_1,distance=0..] run playsound minecraft:entity.glow_squid.squirt master @a[tag=mg.flw] ~ ~ ~ 1 2
tp @n[tag=l_morbex_1,distance=0..] 10021 41 -97
kill @n[tag=l_morbex_1,distance=0..]

#eye tracking
setblock 10017 91 -105 minecraft:redstone_block

execute positioned 10022 94 -98 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> Enough!","color":"white","bold":false}]

function music:end
tag @a[tag=mg.flw] add cutscene

schedule function floaty:sched/npc/overworld_cutscene/valor_morbex/6 4s
