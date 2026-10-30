#tp @n[tag=a_golem] -10720 109 -260
execute store result bossbar boss:attestor value run data get entity @n[tag=a_golem,distance=0..] Health

execute unless entity @e[tag=a_golem,distance=0..] if entity @a[tag=in_trial_well_3,gamemode=!spectator,tag=mg.flw] run setblock -10688 123 -269 minecraft:redstone_block

scoreboard players remove a_golem_breath_timer Value 1

execute if score a_golem_breath_timer Value matches ..0 run playsound minecraft:entity.iron_golem.repair hostile @a[tag=mg.flw] -10720 109 -260 3 0.1
execute if score a_golem_breath_timer Value matches ..0 run summon area_effect_cloud -10720 109 -260 {custom_particle:{type:"block",block_state:"minecraft:mud_bricks"},ReapplicationDelay:40,Radius:3f,RadiusPerTick:0.04f,RadiusOnUse:0f,Duration:150,DurationOnUse:3f,WaitTime:20,potion_contents:{potion:"minecraft:strong_harming"}}
execute if score a_golem_breath_timer Value matches ..0 run scoreboard players set a_golem_breath_timer Value 300
