data modify entity @n[tag=morbex_machine,distance=0..] Pose set value {}
setblock 10389 43 -12 air
fill 10381 43 -8 10389 43 -14 glass replace stone
setblock 10393 62 -15 air
fill 10381 46 -7 10389 46 -15 minecraft:red_wool
tp @n[tag=morbex_machine,distance=0..] 10384 43 -11

particle minecraft:trial_spawner_detection_ominous 10396 172 -12 0.3 0.5 0.3 0 100

playsound minecraft:entity.glow_squid.hurt master @a[tag=mg.flw] 10396 170 -12 2 0.1
playsound minecraft:event.mob_effect.raid_omen master @a[tag=mg.flw] 10396 170 -12 2 2
playsound minecraft:ambient.crimson_forest.mood master @a[tag=mg.flw] 10396 170 -12

schedule function floaty:sched/npc/overworld_cutscene/machine/15 3s replace

function music:end
