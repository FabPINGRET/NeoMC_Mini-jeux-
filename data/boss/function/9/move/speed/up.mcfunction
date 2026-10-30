scoreboard players add @e[tag=wm_drone_pivot,distance=0..] Value 1
execute as @e[tag=wm_drone_pivot,distance=0..] if score @s Value matches 6.. run scoreboard players set @s Value 5
