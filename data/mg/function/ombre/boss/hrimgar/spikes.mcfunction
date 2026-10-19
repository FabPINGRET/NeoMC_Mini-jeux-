# Hrimgar, le géant du givre : spikes
execute as @a[tag=mg.olw,gamemode=adventure,distance=..18] at @s run summon minecraft:marker ~ ~ ~ {Tags:["mg.ol","mg.olspike"]}
scoreboard players set @e[tag=mg.olspike] mg.olst 2
playsound minecraft:block.glass.break hostile @a ~ ~ ~ 1.5 0.5
