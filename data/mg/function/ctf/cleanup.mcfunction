function mg:ctf/kill_all
tag @a remove mg.cfcr
tag @a remove mg.cfcb
effect clear @a[tag=mg.play] minecraft:glowing
scoreboard players reset * mg.cf
