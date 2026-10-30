scoreboard players remove thren_fountain_timer Value 1

execute if score thren_fountain_timer Value matches ..0 run function boss:mini/threnodist/attack/fountain/summon

execute if score thren_fountain_timer Value matches ..0 run scoreboard players operation thren_fountain_timer Value = thren_fountain_freq Value

execute as @e[tag=thren_arrow,tag=gravity,distance=0..] at @s if entity @s[y=57,dy=1.5] run function boss:mini/threnodist/attack/fountain/shoot
execute as @e[tag=thren_arrow,distance=0..] at @s if block ~1 ~ ~1 air if block ~-1 ~ ~1 air if block ~1 ~ ~-1 air if block ~-1 ~ ~-1 air run particle dragon_breath ~ ~ ~ 0 0 0 0 0 normal
