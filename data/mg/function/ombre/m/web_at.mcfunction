execute if block ~ ~ ~ minecraft:air run summon minecraft:marker ~ ~ ~ {Tags:["mg.ol","mg.olweb"]}
execute if block ~ ~ ~ minecraft:air run setblock ~ ~ ~ minecraft:cobweb
scoreboard players set @e[tag=mg.olweb,distance=..0.5] mg.olst 60
