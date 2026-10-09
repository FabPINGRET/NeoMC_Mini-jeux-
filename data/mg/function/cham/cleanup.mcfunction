function mg:cham/kill_all
execute as @a[tag=mg.cmx] run attribute @s minecraft:scale base set 1
effect clear @a[tag=mg.cmx]
team leave @a[team=mg_cm]
tag @a remove mg.cmh
tag @a remove mg.cms
tag @a remove mg.cmout
tag @a remove mg.cmhunt
tag @a remove mg.cmx
scoreboard players reset @a mg.cmp
scoreboard players reset @a mg.cmo
