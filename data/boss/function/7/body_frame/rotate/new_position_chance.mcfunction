execute store result score boss:st_turn_chance bool run random value 1..2
execute if score boss:st_turn_chance bool matches 1 run function boss:7/body_frame/rotate/new_position
