data modify entity @n[tag=morbex_machine,distance=0..] Pose set value {}

particle minecraft:sculk_soul 10396 172 -12 0.4 0.5 0.4 0.1 100
playsound minecraft:block.trial_spawner.spawn_item master @a[tag=mg.flw] 10396 170 -12 2 0.1
playsound minecraft:entity.copper_golem_weathered.hurt master @a[tag=mg.flw] 10396 170 -12 2 0.1

#start particles
fill 10381 43 -8 10389 43 -14 stone replace glass
setblock 10389 43 -12 clay
setblock 10388 43 -8 minecraft:redstone_block
setblock 10393 62 -15 minecraft:redstone_block

data modify entity @n[tag=morbex_machine,distance=0..] Pose set value {Body:[350f,0f,0f],Head:[350f,0f,0f],LeftLeg:[330f,280f,0f],RightLeg:[330f,80f,0f],LeftArm:[80f,330f,330f],RightArm:[80f,30f,30f]}

execute positioned 10396 170 -12 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> ","color":"white","bold":false},{"text":"Hrk! What is this???","color":"white","italic":true},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/machine/3 4s replace

#","color":"white"},{"text":"
