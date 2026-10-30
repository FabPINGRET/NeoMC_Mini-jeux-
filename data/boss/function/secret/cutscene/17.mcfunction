playsound minecraft:block.trial_spawner.detect_player neutral @a[tag=mg.flw] -12476 184 -171 3 0.5
playsound minecraft:entity.happy_ghast.ambient neutral @a[tag=mg.flw] -12476 184 -171 3 0.7

particle minecraft:end_rod -12476 187 -171 1 1 1 0.3 200
particle minecraft:witch -12476 187 -171 1 1 1 1 200
playsound minecraft:block.trial_spawner.ominous_activate master @a[tag=mg.flw] -12476 187 -171 3 0.4
playsound minecraft:entity.enderman.teleport master @a[tag=mg.flw] -12476 187 -171 3 0.4

setblock -12472 185 -169 minecraft:polished_blackstone_button[face=floor,facing=west,powered=false]
setblock -12471 185 -171 minecraft:polished_blackstone_button[face=floor,facing=west,powered=false]
setblock -12472 185 -173 minecraft:polished_blackstone_button[face=floor,facing=west,powered=false]
setblock -12472 183 -169 minecraft:command_block[conditional=false,facing=up]{Command:"/function game:nacre_heart/1",SuccessCount:0,TrackOutput:1b,UpdateLastExecution:1b,auto:0b,components:{},conditionMet:0b,powered:0b}
setblock -12471 183 -171 minecraft:command_block[conditional=false,facing=up]{Command:"/function game:nacre_heart/2",SuccessCount:0,TrackOutput:1b,UpdateLastExecution:1b,auto:0b,components:{},conditionMet:0b,powered:0b}
setblock -12472 183 -173 minecraft:command_block[conditional=false,facing=up]{Command:"/function game:nacre_heart/3",SuccessCount:0,TrackOutput:1b,UpdateLastExecution:1b,auto:0b,components:{},conditionMet:0b,powered:0b}

#STOP TICK
setblock -12453 162 -153 air

tag @a[tag=mg.flw] remove bossroom
tag @a[tag=mg.flw] remove targeted

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

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"God of Keys","color":"dark_purple","bold":true},{"text":"> Until next time, old friend.","color":"white","bold":false}]

function game:blue_light_on

#","color":"white"},{"text":"
