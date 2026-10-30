scoreboard players set boss:final_morbex BossHealth 200
bossbar set boss:final_morbex players
bossbar set boss:final_morbex value 200
bossbar set boss:final_morbex color green

scoreboard players set boss:final BossHealth 658
bossbar set boss:final players
bossbar set boss:final value 658
bossbar set boss:final color purple

tag @a[tag=mg.flw] remove bossroom
tag @a[tag=mg.flw] remove targeted

function boss:final/arena/full_platform
function boss:final/virus/clear_sphere

setblock -12346 43 340 minecraft:redstone_block

# MORBEX INIT ----------
# Reset morbex health tracking
fill -12349 43 381 -12346 42 384 air replace minecraft:redstone_block
# Stop tick
setblock -12346 43 334 air
# Reset spinning sword attack counter
setblock -12346 42 338 minecraft:black_wool
# Reset death check
setblock -12354 42 378 air
setblock -12354 42 383 air

function boss:final/morbex/pose/neutral
function boss:final/morbex/equipment/armor
function boss:final/morbex/equipment/sword
schedule clear floaty:sched/boss/final/morbex/pick_attack

tp @n[tag=lord_morbex_stand,distance=0..] -12384 71 355 -90 0

scoreboard players set final_morbex_target_mode Value 0
scoreboard players set morbex_hurtable bool 0
scoreboard players set morbex_repo_timer Value 100

kill @e[tag=l_morbex_2,distance=0..]
kill @e[tag=mutarid_strong,distance=0..]

# VIRUS INIT ----------

#Stop tick
fill -12346 43 346 -12346 43 342 air
#stop door sword barrier
fill -12339 128 356 -12339 130 354 air

kill @e[tag=m_caster,distance=0..]

kill @e[tag=wv_lord,distance=0..]
kill @e[tag=wv_pivot,distance=0..]

kill @e[tag=wv_model_sword,distance=0..]
kill @e[tag=wv_model_eye,distance=0..]
kill @e[tag=wv_model_forearm,distance=0..]
kill @e[tag=wv_model_forearm2,distance=0..]
kill @e[tag=wv_model_bicep,distance=0..]
kill @e[tag=wv_model_bicep2,distance=0..]
kill @e[tag=wv_model_crown,distance=0..]
kill @e[tag=wv_model_smallarm,distance=0..]
kill @e[tag=world_virus_portal,distance=0..]
kill @e[tag=wv_model_heart,distance=0..]

kill @e[tag=wv_model_bell,distance=0..]

kill @e[tag=wv_wrist,distance=0..]
kill @e[tag=wv_center,distance=0..]
kill @e[tag=wv_wrist_dest,distance=0..]
kill @e[tag=wv_smallarm,distance=0..]
kill @e[tag=wv_elbow,distance=0..]
kill @e[tag=wv_elbow2,distance=0..]

kill @e[tag=wv_model_flamesword,distance=0..]
kill @e[tag=wv_model_forestsword,distance=0..]
kill @e[tag=wv_model_sporessword,distance=0..]
kill @e[tag=wv_model_stonesword,distance=0..]
kill @e[tag=wv_model_icesword,distance=0..]
kill @e[tag=wv_model_watersword,distance=0..]
kill @e[tag=wv_model_valorsword,distance=0..]

scoreboard players set wv_one_left bool 0
scoreboard players set wv_alive bool 1
scoreboard players set wv_pose Value 0
scoreboard players set wv_target_mode Value 0
scoreboard players set wv_focused bool 0
scoreboard players set wv_fire_color bool 0
scoreboard players set wv_lord_timer Value -1

scoreboard players set wv_eye_speed Value 1
scoreboard players set wv_wrist_speed Value 2

scoreboard players set lordsword_mode bool 0

schedule clear floaty:sched/boss/final/virus/pick_attack
