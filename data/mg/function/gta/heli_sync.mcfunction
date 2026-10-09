# @s : hélico. La carrosserie suit, les rotors tournent (plus vite avec un pilote)
scoreboard players operation $gv mg.st = @s mg.gvid
execute on passengers run tag @s add mg.gpil
execute as @e[type=minecraft:block_display,tag=mg.ghbody] if score @s mg.gvid = $gv mg.st run function mg:gta/vd_follow
execute if entity @a[tag=mg.gpil] as @e[type=minecraft:block_display,tag=mg.ghrot] if score @s mg.gvid = $gv mg.st rotated as @s run function mg:gta/rotor_fast
execute unless entity @a[tag=mg.gpil] as @e[type=minecraft:block_display,tag=mg.ghrot] if score @s mg.gvid = $gv mg.st rotated as @s run function mg:gta/rotor_slow
execute if entity @a[tag=mg.gpil] run particle minecraft:cloud ~ ~-0.3 ~ 1.5 0.1 1.5 0.02 2
execute if entity @a[tag=mg.gpil] if score $gq mg.st matches 0 run playsound minecraft:entity.bee.loop neutral @a ~ ~ ~ 1.2 0.5
execute if entity @a[tag=mg.gpil] if score $gq mg.st matches 10 run playsound minecraft:entity.bee.loop neutral @a ~ ~ ~ 1.2 0.5
tag @a remove mg.gpil
