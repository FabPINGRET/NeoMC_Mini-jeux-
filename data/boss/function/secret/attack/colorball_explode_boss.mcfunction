scoreboard players set sc_boss_damaged bool 0

execute if score sc_boss_color bool matches 0 if entity @e[tag=sc_boss_colorball,tag=blue,distance=0..] run scoreboard players set sc_boss_damaged bool 1
execute if score sc_boss_color bool matches 1 if entity @e[tag=sc_boss_colorball,tag=red,distance=0..] run scoreboard players set sc_boss_damaged bool 1

execute if score sc_boss_damaged bool matches 0 at @n[tag=sc_boss_colorball,distance=0..] run summon item ~ ~1.6 ~ {Item:{id:"minecraft:arrow",count:1}}

execute as @n[tag=sc_boss_colorball,distance=0..] at @s run particle minecraft:explosion_emitter ~ ~1.6 ~ 0 0 0 0 1
execute as @n[tag=sc_boss_colorball,distance=0..] at @s run playsound minecraft:entity.dragon_fireball.explode hostile @a[tag=mg.flw] ~ ~ ~ 4 1

schedule clear floaty:sched/boss/secret/attack/do_switch

kill @e[tag=sc_boss_colorball,distance=0..]

#stop switch steps
fill -12462 161 -157 -12459 161 -157 glass replace stone

function boss:secret/display/pose/idle
function boss:secret/display/target/target

execute if score sc_boss_damaged bool matches 0 if score sc_boss_color bool matches 0 run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"God of Keys","color":"dark_purple","bold":true},{"text":"> My","bold":false,"color":"white"},{"text":" red cloak","color":"red"},{"text":" protects me from ","color":"white"},{"text":"red magic","color":"red"},{"text":"!","color":"white"}]
execute if score sc_boss_damaged bool matches 0 if score sc_boss_color bool matches 1 run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"God of Keys","color":"dark_purple","bold":true},{"text":"> My","bold":false,"color":"white"},{"text":" blue cloak","color":"blue"},{"text":" protects me from ","color":"white"},{"text":"blue magic","color":"blue"},{"text":"!","color":"white"}]
execute if score sc_boss_damaged bool matches 0 run schedule function floaty:sched/boss/secret/attack/do_colorball 2s replace
execute if score sc_boss_damaged bool matches 0 run function boss:secret/new_position

execute if score sc_boss_damaged bool matches 1 run function boss:secret/damage
