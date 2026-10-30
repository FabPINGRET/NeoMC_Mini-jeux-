scoreboard players set @a[distance=..2.5,tag=mg.flw] use_trident 0

# KILL IF NO CANNON
execute if entity @s[tag=1] unless entity @e[tag=wm_drone_part,tag=1,tag=cannon,distance=0..] at @s run function boss:9/break/all
execute if entity @s[tag=2] unless entity @e[tag=wm_drone_part,tag=2,tag=cannon,distance=0..] at @s run function boss:9/break/all
execute if entity @s[tag=3] unless entity @e[tag=wm_drone_part,tag=3,tag=cannon,distance=0..] at @s run function boss:9/break/all

# BREAK SECOND SHIELD AND CANNON
execute if entity @s[tag=hit,tag=1] if entity @e[tag=wm_drone_part,tag=1,tag=cannon,distance=0..] at @s run function boss:9/break/shield_all
execute if entity @s[tag=hit,tag=2] if entity @e[tag=wm_drone_part,tag=2,tag=cannon,distance=0..] at @s run function boss:9/break/shield_all
execute if entity @s[tag=hit,tag=3] if entity @e[tag=wm_drone_part,tag=3,tag=cannon,distance=0..] at @s run function boss:9/break/shield_all

# BREAK FIRST SHIELD
execute unless entity @s[tag=hit] store result score temp Value run random value 1..2

execute unless entity @s[tag=hit] if score temp Value matches 1 at @s run function boss:9/break/shield_l
execute unless entity @s[tag=hit] if score temp Value matches 2 at @s run function boss:9/break/shield_r
