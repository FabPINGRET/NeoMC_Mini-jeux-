scoreboard players set boss:ta BossHealth 6
bossbar set boss:ta players
bossbar set boss:ta value 6
bossbar set boss:ta color green

tag @a[tag=mg.flw] remove bossroom

# Reset Start Latch
setblock -11798 202 362 air

# Reset stand facing player
setblock -11798 203 360 air
kill @n[tag=boss_ta_cutscene_stand,distance=0..]

# Reset cutscene soul pivot
scoreboard players set boss_ta_cutscene_soul_pivot_pitch Value 0
setblock -11799 202 358 air
kill @e[tag=boss_ta_cutscene_soul_display,distance=0..]
kill @e[tag=boss_ta_cutscene_soul_pivot,distance=0..]
fill -11800 202 354 -11798 202 354 air

scoreboard players set boss_ta_active_face Value 0
scoreboard players set boss_ta_last_face Value 0
scoreboard players set boss:ta_lastattack Value 0

# Stop tick
setblock -11798 203 351 air

# Reset damage latch
setblock -11807 203 351 air

# Reset lord of smoke spawn line
setblock -11798 202 313 air

function boss:10/soul_attack_disable

kill @e[tag=allsoul_loc,distance=0..]
kill @e[tag=allsoul_head,distance=0..]
kill @e[tag=allsoul_buffer,distance=0..]
kill @e[tag=allsoul_tornado,distance=0..]
kill @e[tag=allsoul_tornado_display,distance=0..]
kill @e[tag=allsoul_arm,distance=0..]
kill @e[tag=allsoul_arm_display,distance=0..]
kill @e[tag=ta_boss_spike,distance=0..]
kill @e[tag=ta_boss_spike_display,distance=0..]

scoreboard players set boss_ta_move_mode Value 1

kill @e[tag=a_soul,distance=0..]
kill @e[tag=l_soul,distance=0..]
