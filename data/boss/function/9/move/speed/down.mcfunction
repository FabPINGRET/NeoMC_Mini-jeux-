scoreboard players remove @e[tag=wm_drone_pivot,distance=0..] Value 1
execute as @e[tag=wm_drone_pivot,distance=0..] if score @s Value matches ..0 run scoreboard players set @s Value 1
