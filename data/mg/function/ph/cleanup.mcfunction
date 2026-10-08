function mg:ph/kill_all
execute as @a[tag=mg.phx] run attribute @s minecraft:scale base set 1
effect clear @a[tag=mg.phx] minecraft:invisibility
effect clear @a[tag=mg.phx] minecraft:speed
effect clear @a[tag=mg.phx] minecraft:blindness
team leave @a[team=mg_ph]
tag @a remove mg.phh
tag @a remove mg.phs
tag @a remove mg.phsn
tag @a remove mg.phx
