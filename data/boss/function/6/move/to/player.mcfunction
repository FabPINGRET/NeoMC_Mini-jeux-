execute unless entity @a[tag=bossroom,tag=sh_targeted,gamemode=!spectator,tag=mg.flw] run tag @r[gamemode=!spectator,tag=bossroom,tag=mg.flw] add sh_targeted

execute as @n[tag=boss_sh_loc,distance=0..] at @s run summon armor_stand ^ ^ ^1 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_sh_forward_check","boss_sh_bait_check"],DisabledSlots:4144959}
execute as @n[tag=boss_sh_loc,distance=0..] at @s run summon armor_stand ^1 ^ ^ {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_sh_left_check","boss_sh_bait_check"],DisabledSlots:4144959}
execute as @n[tag=boss_sh_loc,distance=0..] at @s run summon armor_stand ^-1 ^ ^ {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_sh_right_check","boss_sh_bait_check"],DisabledSlots:4144959}

execute at @n[tag=bossroom,tag=sh_targeted,distance=0..] as @n[tag=boss_sh_bait_check,distance=0..] if entity @s[tag=boss_sh_forward_check] run function boss:6/move/forward
execute at @n[tag=bossroom,tag=sh_targeted,distance=0..] as @n[tag=boss_sh_bait_check,distance=0..] if entity @s[tag=boss_sh_left_check] run function boss:6/move/turn_left
execute at @n[tag=bossroom,tag=sh_targeted,distance=0..] as @n[tag=boss_sh_bait_check,distance=0..] if entity @s[tag=boss_sh_right_check] run function boss:6/move/turn_right

kill @e[tag=boss_sh_bait_check,distance=0..]

schedule function floaty:sched/boss/6/select_cycle 30t replace
