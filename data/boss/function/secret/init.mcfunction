scoreboard players set boss:secret BossHealth 6
bossbar set boss:secret players
bossbar set boss:secret value 6
bossbar set boss:secret color green

tag @a[tag=mg.flw] remove bossroom
tag @a[tag=mg.flw] remove targeted

clone -12493 181 -193 -12450 181 -149 -12493 183 -193

#START LATCH
setblock -12456 161 -153 air
#STOP TICK
setblock -12453 162 -153 air

kill @e[tag=illock,distance=0..]

kill @e[tag=sc_boss_model_body,distance=0..]
kill @e[tag=sc_boss_model_head,distance=0..]
kill @e[tag=sc_boss_model_rarm,distance=0..]
kill @e[tag=sc_boss_model_larm,distance=0..]
kill @e[tag=sc_boss_model_keystar,distance=0..]
kill @e[tag=sc_boss_model_keyring,distance=0..]

kill @e[tag=sc_boss_body_draw,distance=0..]
kill @e[tag=sc_boss_head_draw,distance=0..]
kill @e[tag=sc_boss_rarm_draw,distance=0..]
kill @e[tag=sc_boss_larm_draw,distance=0..]
kill @e[tag=sc_boss_pos,distance=0..]
kill @e[tag=sc_boss_draw,distance=0..]
kill @e[tag=sc_boss_dest,distance=0..]

kill @e[tag=sc_boss_turret,distance=0..]
kill @e[tag=sc_boss_bomb,distance=0..]
kill @e[tag=sc_keyring_pos,distance=0..]

scoreboard players set sc_targeting_mode Value 0
scoreboard players set sc_pose Value 0
scoreboard players set sc_boss_color bool 1

function boss:secret/display/color/purple

scoreboard players set sc_boss_countdown Value 0

schedule clear floaty:sched/boss/secret/pick_attack
