function mg:ctf2/kill_all
tag @a remove mg.cfcr
tag @a remove mg.cfcb
effect clear @a[tag=mg.play] minecraft:glowing
scoreboard players reset * mg.cf
forceload remove -44 41376 44 41424
schedule clear mg:ctf2/prepare_b
