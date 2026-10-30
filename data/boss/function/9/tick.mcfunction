execute as @e[tag=wm_drone_draw,tag=1,distance=0..] at @n[tag=wm_drone_pos,tag=1,distance=0..] run tp @s ~ ~ ~
execute as @e[tag=wm_drone_draw,tag=2,distance=0..] at @n[tag=wm_drone_pos,tag=2,distance=0..] run tp @s ~ ~ ~
execute as @e[tag=wm_drone_draw,tag=3,distance=0..] at @n[tag=wm_drone_pos,tag=3,distance=0..] run tp @s ~ ~ ~

execute as @n[tag=wm_drone_pos,tag=1,distance=0..] at @s facing entity @n[tag=wm_drone_dest,tag=1,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
execute as @n[tag=wm_drone_pos,tag=2,distance=0..] at @s facing entity @n[tag=wm_drone_dest,tag=2,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
execute as @n[tag=wm_drone_pos,tag=3,distance=0..] at @s facing entity @n[tag=wm_drone_dest,tag=3,distance=0..] eyes run tp @s ~ ~ ~ ~ ~

execute if score wm_follow_dest bool matches 1 as @n[tag=wm_drone_pos,tag=1,distance=0..] at @s unless entity @n[tag=wm_drone_dest,tag=1,distance=..1] run tp @s ^ ^ ^1
execute if score wm_follow_dest bool matches 1 as @n[tag=wm_drone_pos,tag=1,distance=0..] at @s if entity @n[tag=wm_drone_dest,tag=1,distance=..1] at @n[tag=wm_drone_dest,tag=1,distance=0..] run tp @s ~ ~ ~
execute if score wm_follow_dest bool matches 1 as @e[tag=wm_drone_draw,tag=1,distance=0..] at @s unless entity @n[tag=wm_drone_dest,tag=1,distance=..1] run particle dripping_dripstone_water ~ ~ ~ 0.3 0.3 0.3 0 3

execute if score wm_follow_dest bool matches 1 as @n[tag=wm_drone_pos,tag=2,distance=0..] at @s unless entity @n[tag=wm_drone_dest,tag=2,distance=..1] run tp @s ^ ^ ^1
execute if score wm_follow_dest bool matches 1 as @n[tag=wm_drone_pos,tag=2,distance=0..] at @s if entity @n[tag=wm_drone_dest,tag=2,distance=..1] at @n[tag=wm_drone_dest,tag=2,distance=0..] run tp @s ~ ~ ~
execute if score wm_follow_dest bool matches 1 as @e[tag=wm_drone_draw,tag=2,distance=0..] at @s unless entity @n[tag=wm_drone_dest,tag=2,distance=..1] run particle dripping_dripstone_water ~ ~ ~ 0.3 0.3 0.3 0 3

execute if score wm_follow_dest bool matches 1 as @n[tag=wm_drone_pos,tag=3,distance=0..] at @s unless entity @n[tag=wm_drone_dest,tag=3,distance=..1] run tp @s ^ ^ ^1
execute if score wm_follow_dest bool matches 1 as @n[tag=wm_drone_pos,tag=3,distance=0..] at @s if entity @n[tag=wm_drone_dest,tag=3,distance=..1] at @n[tag=wm_drone_dest,tag=3,distance=0..] run tp @s ~ ~ ~
execute if score wm_follow_dest bool matches 1 as @e[tag=wm_drone_draw,tag=3,distance=0..] at @s unless entity @n[tag=wm_drone_dest,tag=3,distance=..1] run particle dripping_dripstone_water ~ ~ ~ 0.3 0.3 0.3 0 3

#SLAM LOCATION
execute if score wm_follow_dest bool matches 0 as @n[tag=wm_drone_pos,tag=1,distance=0..] at @n[tag=wm_grav_ref,tag=1,distance=0..] run tp @s ~ ~1 ~
execute if score wm_follow_dest bool matches 0 as @n[tag=wm_drone_pos,tag=2,distance=0..] at @n[tag=wm_grav_ref,tag=2,distance=0..] run tp @s ~ ~1 ~
execute if score wm_follow_dest bool matches 0 as @n[tag=wm_drone_pos,tag=3,distance=0..] at @n[tag=wm_grav_ref,tag=3,distance=0..] run tp @s ~ ~1 ~

#LOCATION MODES
# 0 = RING POSITION, 1 = FLOOR RING, 2 = STATIC, 3 = SLAM
execute if score @n[tag=wm_drone_pos,tag=1,distance=0..] Value matches 0..1 as @n[tag=wm_drone_pivot,tag=1,distance=0..] at @s run tp @n[tag=wm_drone_dest,tag=1,distance=0..] ^ ^ ^20
execute if score @n[tag=wm_drone_pos,tag=2,distance=0..] Value matches 0..1 as @n[tag=wm_drone_pivot,tag=2,distance=0..] at @s run tp @n[tag=wm_drone_dest,tag=2,distance=0..] ^ ^ ^16
execute if score @n[tag=wm_drone_pos,tag=3,distance=0..] Value matches 0..1 as @n[tag=wm_drone_pivot,tag=3,distance=0..] at @s run tp @n[tag=wm_drone_dest,tag=3,distance=0..] ^ ^ ^12

execute if score @n[tag=wm_drone_pos,tag=1,distance=0..] Value matches 1 as @n[tag=wm_drone_dest,tag=1,distance=0..] at @s run tp @s ~ -18.5 ~
execute if score @n[tag=wm_drone_pos,tag=2,distance=0..] Value matches 1 as @n[tag=wm_drone_dest,tag=2,distance=0..] at @s run tp @s ~ -18.5 ~
execute if score @n[tag=wm_drone_pos,tag=3,distance=0..] Value matches 1 as @n[tag=wm_drone_dest,tag=3,distance=0..] at @s run tp @s ~ -18.5 ~

#execute if score @n[tag=wm_drone_pos,tag=1] Value matches 3

function boss:9/move/pivot_tick

#VIEW MODES
# 0 = NEAREST PLAYER, 1 = TARGET, 2 = GROUND, 3 = EACH OTHER (2), 4 = EACH OTHER (3), 5 = CENTER, 6 = NO CONTROL, 7 = CEILING

execute as @e[tag=wm_drone_draw,distance=0..] if score @s Value matches 0 at @s facing entity @p[gamemode=!spectator,tag=bossroom,tag=mg.flw] eyes run tp @s ~ ~ ~ ~ ~
execute as @e[tag=wm_drone_draw,distance=0..] if score @s Value matches 1 at @s facing entity @p[gamemode=!spectator,tag=bossroom,tag=targeted,tag=mg.flw] eyes run tp @s ~ ~ ~ ~ ~
execute as @e[tag=wm_drone_draw,distance=0..] if score @s Value matches 2 at @s run tp @s ~ ~ ~ ~10 ~5
execute as @e[tag=wm_drone_draw,tag=1,distance=0..] if score @s Value matches 3 at @s facing entity @n[tag=wm_drone_pos,tag=2,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
execute as @e[tag=wm_drone_draw,tag=2,distance=0..] if score @s Value matches 3 at @s facing entity @n[tag=wm_drone_pos,tag=1,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
execute as @e[tag=wm_drone_draw,tag=1,distance=0..] if score @s Value matches 4 at @s facing entity @n[tag=wm_drone_pos,tag=2,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
execute as @e[tag=wm_drone_draw,tag=2,distance=0..] if score @s Value matches 4 at @s facing entity @n[tag=wm_drone_pos,tag=3,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
execute as @e[tag=wm_drone_draw,tag=3,distance=0..] if score @s Value matches 4 at @s facing entity @n[tag=wm_drone_pos,tag=1,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
execute as @e[tag=wm_drone_draw,distance=0..] if score @s Value matches 5 at @s facing -11223 -19 -109 run tp @s ~ ~ ~ ~ ~
execute as @e[tag=wm_drone_draw,distance=0..] if score @s Value matches 7 at @s facing -11223 22 -109 run tp @s ~ ~ ~ ~ ~

# VELO CHECK

execute as @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] store result score @s y_velocity run data get entity @s Motion[1] 1000
execute as @a[tag=mg.flw] if score @s y_velocity matches ..-100 run scoreboard players set @s use_trident 0
execute as @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] if score @s use_trident matches 1.. at @s if entity @e[tag=wm_drone_draw,distance=..2.25] as @n[tag=wm_drone_draw,distance=0..] at @s run function boss:9/break/increment
