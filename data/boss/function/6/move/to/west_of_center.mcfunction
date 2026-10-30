execute as @n[tag=boss_sh_loc,distance=0..] at @s run summon armor_stand ^ ^ ^1 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_sh_forward_check","boss_sh_bait_check"],DisabledSlots:4144959}
execute as @n[tag=boss_sh_loc,distance=0..] at @s run summon armor_stand ^1 ^ ^ {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_sh_left_check","boss_sh_bait_check"],DisabledSlots:4144959}
execute as @n[tag=boss_sh_loc,distance=0..] at @s run summon armor_stand ^-1 ^ ^ {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_sh_right_check","boss_sh_bait_check"],DisabledSlots:4144959}

execute positioned -10490 63 -70 as @n[tag=boss_sh_bait_check,distance=0..] if entity @s[tag=boss_sh_forward_check] run function boss:6/move/forward
execute positioned -10490 63 -70 as @n[tag=boss_sh_bait_check,distance=0..] if entity @s[tag=boss_sh_left_check] run function boss:6/move/turn_left
execute positioned -10490 63 -70 as @n[tag=boss_sh_bait_check,distance=0..] if entity @s[tag=boss_sh_right_check] run function boss:6/move/turn_right

kill @e[tag=boss_sh_bait_check,distance=0..]

execute as @n[tag=boss_sh_loc,distance=0..] unless entity @s[tag=x2,tag=z3] run schedule function floaty:sched/boss/6/move/to/west_of_center 30t replace
execute as @n[tag=boss_sh_loc,distance=0..] if entity @s[tag=x2,tag=z3] run schedule function floaty:sched/boss/6/move/to/center 30t replace
