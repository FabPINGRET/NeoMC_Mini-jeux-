scoreboard players set wv_chop_check bool 0
execute positioned -12384 123 355 if entity @n[tag=targeted,gamemode=!spectator,distance=..25] run scoreboard players set wv_chop_check bool 1

execute if score wv_chop_check bool matches 1 run function boss:final/virus/display/pose/chop_near
execute if score wv_chop_check bool matches 0 run function boss:final/virus/display/pose/chop_far
