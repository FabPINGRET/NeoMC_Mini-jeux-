function boss:10/soul_attack_enable

function boss:10/setup/tornado_form

schedule function floaty:sched/boss/10/try_attack 3s replace


kill @e[tag=boss_ta_spike,distance=0..]
kill @e[tag=boss_ta_spike_display,distance=0..]

kill @e[tag=boss_ta_light_pivot,distance=0..]
kill @e[tag=allsoul_light,distance=0..]
kill @e[tag=allsoul_light_display,distance=0..]
setblock -11824 202 323 air

schedule function floaty:sched/boss/10/helper/place_helper 24s replace

playsound minecraft:block.trial_spawner.spawn_mob hostile @a[tag=mg.flw] -11830 218 330 5 0.1
particle minecraft:sculk_soul -11830 219 330 2 3 2 0.2 600
