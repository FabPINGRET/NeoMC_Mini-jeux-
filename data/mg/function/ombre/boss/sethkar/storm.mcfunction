# Sethkar, le pharaon-liche : storm
playsound minecraft:entity.breeze.idle_air hostile @a ~ ~ ~ 2 0.4
particle minecraft:falling_dust{block_state:"minecraft:sand"} ~ ~4 ~ 8 3 8 0 400 force
execute as @a[tag=mg.olw,gamemode=adventure,distance=..14] run damage @s 5 minecraft:mob_attack by @e[tag=mg.olb_sethkar,limit=1]
effect give @a[tag=mg.olw,gamemode=adventure,distance=..14] minecraft:blindness 3 0 true
