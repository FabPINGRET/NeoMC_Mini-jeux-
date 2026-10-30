execute at @n[tag=sc_boss_colorball,distance=0..] run summon item ~ ~1.6 ~ {Item:{id:"minecraft:arrow",count:1}}

execute as @n[tag=sc_boss_colorball,distance=0..] at @s run particle minecraft:explosion_emitter ~ ~1.6 ~ 0 0 0 0 1
execute as @n[tag=sc_boss_colorball,distance=0..] at @s run playsound minecraft:entity.dragon_fireball.explode hostile @a[tag=mg.flw] ~ ~ ~ 4 1

schedule clear floaty:sched/boss/secret/attack/do_switch

kill @e[tag=sc_boss_colorball,distance=0..]

#stop switch steps
fill -12462 161 -157 -12459 161 -157 glass replace stone

function boss:secret/new_position
schedule function floaty:sched/boss/secret/attack/do_colorball 2s replace

function boss:secret/display/pose/idle
function boss:secret/display/target/target
