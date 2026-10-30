setblock 10017 91 -105 air
tp @n[tag=morbex_valor_tower,distance=0..] 10022 90 -98 0 0
particle minecraft:trial_spawner_detection_ominous 10022 95 -98 0.3 0.5 0.3 0 100
playsound minecraft:entity.glow_squid.squirt master @a[tag=mg.flw] 10022 93 -98 1 2

schedule function floaty:sched/npc/overworld_cutscene/valor_morbex/9 3s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
