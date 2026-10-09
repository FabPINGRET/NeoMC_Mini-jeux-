# @s : hélico de police (chaque tick) : vole vers 14 blocs au-dessus du joueur recherché le plus proche
execute unless entity @a[tag=mg.gtw,scores={mg.gwl=5..},distance=..120] run return run function mg:gta/pheli_remove
execute at @p[tag=mg.gtw,scores={mg.gwl=5..}] positioned ~ ~14 ~ run summon minecraft:marker ~ ~ ~ {Tags:["mg.gta","mg.gphto"]}
execute at @s facing entity @e[type=minecraft:marker,tag=mg.gphto,limit=1,sort=nearest] feet unless entity @e[type=minecraft:marker,tag=mg.gphto,distance=..1.5] run tp @s ^ ^ ^0.45 ~ 0
kill @e[type=minecraft:marker,tag=mg.gphto]
scoreboard players operation $gv mg.st = @s mg.gvid
execute at @s as @e[type=minecraft:block_display,tag=mg.gphb] if score @s mg.gvid = $gv mg.st run tp @s ~ ~ ~ ~ 0
execute at @s as @e[type=minecraft:block_display,tag=mg.gphr] if score @s mg.gvid = $gv mg.st rotated as @s run tp @s ~ ~ ~ ~40 0
execute if score $gq mg.st matches 0 at @s run playsound minecraft:entity.bee.loop hostile @a ~ ~ ~ 3 0.5
execute if score $gq mg.st matches 10 at @s run playsound minecraft:entity.bee.loop hostile @a ~ ~ ~ 3 0.5
execute if score $gq2 mg.st matches 0 at @p[tag=mg.gtw,scores={mg.gwl=5..}] run particle minecraft:dust{color:[1.0,1.0,0.85],scale:2.5} ~ ~0.2 ~ 1.4 0.05 1.4 0 14 force
