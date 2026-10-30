execute as @e[type=snowball,tag=sc_boss_red_block,distance=0..] at @s run setblock ~ ~ ~ air
execute as @e[type=snowball,tag=sc_boss_blue_block,distance=0..] at @s run setblock ~ ~ ~ blue_concrete
execute as @e[type=snowball,tag=sc_boss_red_block_invis,distance=0..] at @s run setblock ~ ~ ~ air
execute as @e[type=snowball,tag=sc_boss_blue_block_invis,distance=0..] at @s run setblock ~ ~ ~ barrier

scoreboard players set sc_boss_color bool 1

function boss:secret/display/color/blue
execute as @n[tag=sc_boss_pos,distance=0..] at @s run particle dust{color:[0.000,0.000,1.000],scale:3} ~ ~3 ~ 1 1 1 0 100 normal

execute as @e[tag=illock,tag=red,distance=0..] run function boss:secret/illock/deactivate
execute as @e[tag=illock,tag=blue,distance=0..] run function boss:secret/illock/blue_activate
function boss:secret/attack/explode_red

execute if entity @e[tag=sc_boss_colorball,tag=red,distance=0..] if score boss:secret BossHealth matches 3..4 run schedule function floaty:sched/boss/secret/attack/do_switch 3s replace
execute if entity @e[tag=sc_boss_colorball,tag=red,distance=0..] if score boss:secret BossHealth matches 1..2 run schedule function floaty:sched/boss/secret/attack/do_switch 2s replace
