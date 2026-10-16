# Roi enragé (20 %)
tag @s add mg.trp3
effect give @s minecraft:speed infinite 0 true
effect give @s minecraft:strength infinite 0 true
function mg:terra/rpg/boss/rex_roar
tellraw @a[tag=mg.tvw,distance=..60] {"text":"🦖 Le Roi Tyran est fou de rage !","color":"red","bold":true}
