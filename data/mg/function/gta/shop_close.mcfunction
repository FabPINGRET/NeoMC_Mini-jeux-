# @s (caisse) : fermé 3 min
scoreboard players set @s mg.gpc 3600
scoreboard players operation $gs mg.st = @s mg.gsid
execute as @e[type=minecraft:text_display,tag=mg.gshl] if score @s mg.gsid = $gs mg.st run data merge entity @s {text:{"text":"🔒 Fermé (braquage)","color":"red","bold":true}}
