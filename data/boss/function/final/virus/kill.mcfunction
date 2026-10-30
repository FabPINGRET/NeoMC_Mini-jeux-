function music:end
scoreboard players set wv_alive bool 0

fill -12371 43 332 -12389 42 333 air replace minecraft:redstone_block
kill @e[tag=wv_aoe,distance=0..]

effect clear @a[tag=mg.flw] wither

particle minecraft:explosion ~ ~ ~ 0.5 0.5 0.5 0 5
playsound minecraft:entity.dragon_fireball.explode master @a[tag=mg.flw] ~ ~ ~ 3 1
playsound minecraft:block.respawn_anchor.set_spawn master @a[tag=mg.flw] ~ ~ ~ 3 2
playsound minecraft:entity.wither.hurt master @a[tag=mg.flw] ~ ~ ~ 3 0.7

kill @e[tag=wv_model_flamesword,distance=0..]
kill @e[tag=wv_model_forestsword,distance=0..]
kill @e[tag=wv_model_sporessword,distance=0..]
kill @e[tag=wv_model_stonesword,distance=0..]
kill @e[tag=wv_model_icesword,distance=0..]
kill @e[tag=wv_model_watersword,distance=0..]
kill @e[tag=wv_model_valorsword,distance=0..]

scoreboard players set lordsword_mode bool 0

#stop door sword barrier
fill -12339 128 356 -12339 130 354 air

function boss:final/morbex/equipment/armor

kill @e[tag=m_caster,distance=0..]

kill @e[tag=wv_skull_loc,distance=0..]

kill @e[tag=wv_model_sword,distance=0..]
kill @e[tag=wv_model_eye,distance=0..]
kill @e[tag=wv_model_forearm,distance=0..]
kill @e[tag=wv_model_forearm2,distance=0..]
kill @e[tag=wv_model_bicep,distance=0..]
kill @e[tag=wv_model_bicep2,distance=0..]
kill @e[tag=wv_model_crown,distance=0..]
kill @e[tag=wv_model_smallarm,distance=0..]
kill @e[tag=world_virus_portal,distance=0..]

kill @e[tag=wv_wrist,distance=0..]
kill @e[tag=wv_center,distance=0..]
kill @e[tag=wv_wrist_dest,distance=0..]
kill @e[tag=wv_smallarm,distance=0..]
kill @e[tag=wv_elbow,distance=0..]
kill @e[tag=wv_elbow2,distance=0..]

playsound minecraft:entity.wither.death master @a[tag=mg.flw] -12384 129 355 6 0.5
#start crazy death particles
setblock -12346 43 348 minecraft:redstone_block
#stop tick
fill -12346 43 346 -12346 43 342 air

advancement grant @a[tag=mg.flw] only main_quest:game_finish
scoreboard players set $fla11 mg.fla 1
scoreboard players set beat_game bool 1
execute as @a[tag=mg.flw] run function game:100_check

schedule function floaty:sched/boss/final/cutscene/death_0 8s replace

bossbar set boss:final value 0
