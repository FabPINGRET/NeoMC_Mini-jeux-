execute as @n[tag=allsoul_loc,tag=high,distance=0..] at @s run tp @s @n[tag=allsoul_buffer,tag=6,distance=0..]
execute as @n[tag=allsoul_buffer,tag=6,distance=0..] at @s run tp @s @n[tag=allsoul_buffer,tag=5,distance=0..]
execute as @n[tag=allsoul_buffer,tag=5,distance=0..] at @s run tp @s @n[tag=allsoul_loc,tag=high_mid,distance=0..]
execute as @n[tag=allsoul_loc,tag=high_mid,distance=0..] at @s run tp @s @n[tag=allsoul_buffer,tag=4,distance=0..]
execute as @n[tag=allsoul_buffer,tag=4,distance=0..] at @s run tp @s @n[tag=allsoul_buffer,tag=3,distance=0..]
execute as @n[tag=allsoul_buffer,tag=3,distance=0..] at @s run tp @s @n[tag=allsoul_loc,tag=low_mid,distance=0..]
execute as @n[tag=allsoul_loc,tag=low_mid,distance=0..] at @s run tp @s @n[tag=allsoul_buffer,tag=2,distance=0..]
execute as @n[tag=allsoul_buffer,tag=2,distance=0..] at @s run tp @s @n[tag=allsoul_buffer,tag=1,distance=0..]
execute as @n[tag=allsoul_buffer,tag=1,distance=0..] at @s run tp @s @n[tag=allsoul_loc,tag=low,distance=0..]

execute as @n[tag=allsoul_tornado,tag=low,distance=0..] at @s run tp @s @n[tag=allsoul_loc,tag=low,distance=0..]
execute as @n[tag=allsoul_tornado,tag=low_mid,distance=0..] at @s run tp @s @n[tag=allsoul_loc,tag=low_mid,distance=0..]
execute as @n[tag=allsoul_tornado,tag=high_mid,distance=0..] at @s run tp @s @n[tag=allsoul_loc,tag=high_mid,distance=0..]
execute as @n[tag=allsoul_tornado,tag=high,distance=0..] at @s run tp @s @n[tag=allsoul_loc,tag=high,distance=0..]

execute as @n[tag=allsoul_tornado,tag=low,distance=0..] at @s run rotate @s ~-7 0
execute as @n[tag=allsoul_tornado,tag=low_mid,distance=0..] at @s run rotate @s ~-8 0
execute as @n[tag=allsoul_tornado,tag=high_mid,distance=0..] at @s run rotate @s ~-9 0
execute as @n[tag=allsoul_tornado,tag=high,distance=0..] at @s run rotate @s ~-10 0

execute as @n[tag=allsoul_hands,distance=0..] at @s run tp @s @n[tag=allsoul_loc,tag=low,distance=0..]
execute as @n[tag=allsoul_hands,distance=0..] at @s run tp @s ~ 219.5 ~

execute as @e[tag=allsoul_arm,distance=0..] at @s facing entity @p[gamemode=!spectator,tag=bossroom,tag=mg.flw] eyes run tp @s ~ ~ ~ ~ 0

execute as @e[tag=ta_boss_spike,distance=0..] at @s run tp @s ~ ~ ~ ~10 0


# particles
execute as @n[tag=allsoul_loc,tag=low,distance=0..] at @s run particle minecraft:large_smoke ~ ~1 ~ 0.3 0.5 0.3 0 1
execute as @n[tag=allsoul_loc,tag=low_mid,distance=0..] at @s run particle minecraft:large_smoke ~ ~3 ~ 0.5 0.5 0.5 0 1
execute as @n[tag=allsoul_loc,tag=high_mid,distance=0..] at @s run particle minecraft:large_smoke ~ ~5 ~ 0.9 0.5 0.9 0 1
execute as @n[tag=allsoul_loc,tag=high,distance=0..] at @s run particle minecraft:large_smoke ~ ~7 ~ 1.5 0.5 1.5 0 1

execute as @n[tag=allsoul_loc,tag=low,distance=0..] at @s run particle minecraft:sculk_soul ~ ~1 ~ 0.3 0.5 0.3 0 1
execute as @n[tag=allsoul_loc,tag=low_mid,distance=0..] at @s run particle minecraft:sculk_soul ~ ~3 ~ 0.5 0.5 0.5 0 1
execute as @n[tag=allsoul_loc,tag=high_mid,distance=0..] at @s run particle minecraft:sculk_soul ~ ~5 ~ 0.9 0.5 0.9 0 1
execute as @n[tag=allsoul_loc,tag=high,distance=0..] at @s run particle minecraft:sculk_soul ~ ~7 ~ 1.5 0.5 1.5 0 1


execute as @n[tag=allsoul_loc,tag=low,distance=0..] at @s run tp @n[tag=allsoul_head,tag=top,distance=0..] ^ ^3 ^
execute as @n[tag=allsoul_loc,tag=low,distance=0..] at @s run tp @n[tag=allsoul_head,tag=bottom,distance=0..] ^ ^ ^
execute as @n[tag=allsoul_loc,tag=low,distance=0..] at @s run tp @n[tag=allsoul_head,tag=right,distance=0..] ^1.5 ^1.5 ^
execute as @n[tag=allsoul_loc,tag=low,distance=0..] at @s run tp @n[tag=allsoul_head,tag=left,distance=0..] ^-1.5 ^1.5 ^

# movement modes (0 still no turn, 1 still and turn, 2 turn and follow, 3 forward no turn)

#0
execute if score boss_ta_move_mode Value matches 1..2 as @e[tag=allsoul_head,distance=0..] at @s facing entity @p[gamemode=!spectator,tag=bossroom,tag=mg.flw] eyes run tp @s ~ ~ ~ ~ ~

#1
execute if score boss_ta_move_mode Value matches 1..2 as @n[tag=allsoul_loc,tag=low,distance=0..] at @s facing entity @p[gamemode=!spectator,tag=bossroom,tag=mg.flw] eyes run tp @s ~ 217 ~ ~ 0

#2
execute if score boss_ta_move_mode Value matches 2 as @n[tag=allsoul_loc,tag=low,distance=0..] at @s facing entity @p[gamemode=!spectator,tag=bossroom,tag=mg.flw] eyes if block ^ ^ ^0.1 air run tp @s ^ ^ ^0.1

#3
execute if score boss_ta_move_mode Value matches 3 as @n[tag=allsoul_loc,tag=low,distance=0..] at @s if block ^ ^ ^1 air run tp @s ^ ^ ^1

execute as @n[tag=allsoul_loc,tag=low,distance=0..] at @s as @a[gamemode=!spectator,tag=bossroom,distance=..2,tag=mg.flw] run damage @s 18 minecraft:falling_anvil by @n[tag=ta_boss_name,distance=0..]

# Helper Tick
execute as @n[tag=boss_ta_helper,distance=0..] at @s run particle minecraft:white_smoke ~ 217 ~ 2 0.1 2 0 5
execute as @n[tag=boss_ta_helper,distance=0..] at @s if entity @n[tag=allsoul_loc,tag=low,distance=..2] run function boss:10/phase_1_out
