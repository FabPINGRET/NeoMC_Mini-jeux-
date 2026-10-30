execute if score boss:ta BossHealth matches 6 at @n[tag=boss_ta_helper,distance=0..] run tellraw @a[tag=mg.flw] {"text":"<?> Scatter... Its life force is spread thinly across the entire room. It's on you to find a way to hurt it now..."}
execute if score boss:ta BossHealth matches 3..5 at @n[tag=boss_ta_helper,distance=0..] run tellraw @a[tag=mg.flw] {"text":"<?> Scatter..."}
execute if score boss:ta BossHealth matches 2 at @n[tag=boss_ta_helper,distance=0..] run tellraw @a[tag=mg.flw] {"text":"<?> Scatter... It is weak now..."}

execute at @n[tag=boss_ta_helper,distance=0..] run playsound minecraft:entity.allay.ambient_without_item neutral @a[tag=mg.flw] ~ ~ ~ 5 0.5 

execute as @n[tag=boss_ta_helper,distance=0..] at @s run particle minecraft:white_smoke ~ 218 ~ 0.6 1.5 0.6 0 200

function boss:10/soul_attack_disable

kill @e[tag=allsoul_loc,distance=0..]
kill @e[tag=allsoul_head,distance=0..]
kill @e[tag=allsoul_buffer,distance=0..]
kill @e[tag=allsoul_tornado,distance=0..]
kill @e[tag=allsoul_tornado_display,distance=0..]
kill @e[tag=allsoul_arm,distance=0..]
kill @e[tag=allsoul_arm_display,distance=0..]

scoreboard players set boss_ta_move_mode Value 1

# End helper check
kill @e[tag=boss_ta_helper,distance=0..]

schedule function floaty:sched/boss/10/phase_2_in 3s replace
