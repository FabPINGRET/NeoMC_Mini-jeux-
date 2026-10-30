playsound minecraft:entity.illusioner.cast_spell hostile @a[tag=mg.flw] -10473 -21 -378 3 1
particle minecraft:composter -10473 -18 -378 3 3 3 0 500
summon area_effect_cloud -10473 -21 -378 {custom_particle:{type:"composter"},ReapplicationDelay:40,Radius:4f,RadiusPerTick:0.04f,RadiusOnUse:0f,Duration:160,DurationOnUse:3f,WaitTime:20,potion_contents:{potion:"minecraft:strong_harming"}}
playsound minecraft:entity.ravager.attack hostile @a[tag=mg.flw] -10473 -20 -378 2 0.5
schedule function floaty:sched/boss/7/target_check 3s replace
