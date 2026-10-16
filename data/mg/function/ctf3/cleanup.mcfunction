function mg:ctf3/kill_all
tag @a remove mg.cfcr
tag @a remove mg.cfcb
effect clear @a[tag=mg.play] minecraft:glowing
scoreboard players reset * mg.cf
forceload remove -44 41476 44 41524
schedule clear mg:ctf3/prepare_b
