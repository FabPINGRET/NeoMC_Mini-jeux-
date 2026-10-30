execute at @n[tag=frostbyte_head,distance=0..] positioned ~ ~1 ~ run function boss:8/down_beam/ray
#execute at @n[tag=frostbyte_head] run summon lightning_bolt ~ 89 ~
execute at @n[tag=frostbyte_head,distance=0..] run summon area_effect_cloud ~ 89.5 ~ {custom_particle:{type:"dust_color_transition",from_color:[0.659,0.898,1.000],scale:1,to_color:[0.039,1.000,0.969]},Radius:6f,RadiusPerTick:0.03f,RadiusOnUse:0f,Duration:400,DurationOnUse:0f,potion_contents:{potion:"minecraft:strong_harming"}}

execute at @n[tag=frostbyte_head,distance=0..] run playsound minecraft:block.respawn_anchor.deplete hostile @a[tag=mg.flw] ~ ~ ~ 3 1
execute at @n[tag=frostbyte_head,distance=0..] run playsound minecraft:block.conduit.deactivate hostile @a[tag=mg.flw] ~ ~ ~ 3 1

setblock -10828 67 393 air
