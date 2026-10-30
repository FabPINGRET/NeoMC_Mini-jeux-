scoreboard players set wm_drone_count Value 0
execute as @e[tag=wm_drone_draw,distance=0..] run scoreboard players add wm_drone_count Value 1

execute if score wm_drone_count Value matches 1 as @e[tag=wm_drone_draw,distance=0..] at @s run function boss:9/move/view_mode/center
execute if score wm_drone_count Value matches 2 as @e[tag=wm_drone_draw,distance=0..] at @s run function boss:9/move/view_mode/face_2
execute if score wm_drone_count Value matches 3 as @e[tag=wm_drone_draw,distance=0..] at @s run function boss:9/move/view_mode/face_3
