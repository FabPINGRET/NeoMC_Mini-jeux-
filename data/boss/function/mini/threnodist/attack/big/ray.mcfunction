particle dust{color:[0.000,0.000,0.000],scale:2} ~ ~ ~ 0.1 0.1 0.1 0 0 normal
particle reverse_portal ~ ~ ~ 0 0 0 0.1 1 normal

#execute positioned ~ ~ ~ as @a[gamemode=!spectator,distance=..2] run damage @s 16 minecraft:dragon_breath by @n[tag=deebo_name]

execute positioned ^ ^ ^0.1 if block ^ ^ ^ air run function boss:mini/threnodist/attack/big/ray

#execute unless block ^ ^ ^0.1 air unless entity @e[tag=thren_aoe,distance=..9] run summon area_effect_cloud ~ 58 ~ {custom_particle:{type:"dust_color_transition",from_color:[0.000,0.000,0.000],to_color:[0.529,0.000,0.529],scale:3},NoGravity:1b,ReapplicationDelay:1,Radius:3f,RadiusPerTick:0.08f,RadiusOnUse:0f,Duration:80,DurationOnUse:0f,potion_contents:{custom_effects:[{id:"minecraft:darkness",amplifier:0,duration:160,show_particles:0b},{id:"minecraft:instant_damage",amplifier:2,duration:60,show_particles:0b}]},Tags:["thren_aoe"]}

execute unless block ^ ^ ^0.1 air unless entity @e[tag=thren_aoe,distance=..9] run summon area_effect_cloud ~ 58 ~ {custom_particle:{type:"dust_pillar",block_state:"minecraft:crying_obsidian"},NoGravity:1b,ReapplicationDelay:1,Radius:3f,RadiusPerTick:0.08f,RadiusOnUse:0f,Duration:80,DurationOnUse:0f,potion_contents:{custom_effects:[{id:"minecraft:darkness",amplifier:0,duration:160,show_particles:0b},{id:"minecraft:instant_damage",amplifier:2,duration:60,show_particles:0b}]},Tags:["thren_aoe"]}
