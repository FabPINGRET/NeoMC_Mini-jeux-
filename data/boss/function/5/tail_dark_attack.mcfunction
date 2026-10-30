execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run fill ~-1 ~ ~-1 ~1 ~9 ~1 air
execute as @e[tag=boss_skt_hole_last,limit=1,distance=0..] at @s run clone -10193 72 457 -10191 76 459 ~-1 ~ ~-1
execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run effect give @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] minecraft:darkness infinite 0 true
execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run playsound minecraft:block.conduit.attack.target master @a[tag=mg.flw] ~ ~ ~ 3 2
execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run playsound minecraft:block.conduit.deactivate master @a[tag=mg.flw] ~ ~ ~ 4 0.5
execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run particle minecraft:squid_ink ~ ~3 ~ 1 2 1 0.1 200
setblock -10196 56 413 redstone_block
function boss:5/neutral_anim

schedule function floaty:sched/boss/5/soul_summon 1s replace
schedule function floaty:sched/boss/5/reposition_center_tail 3s
