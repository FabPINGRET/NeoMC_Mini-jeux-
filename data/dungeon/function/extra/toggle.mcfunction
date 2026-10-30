scoreboard players operation sc_toggle bool = sc_color bool

execute if score sc_toggle bool matches 0 run function dungeon:extra/blue_switch
execute if score sc_toggle bool matches 1 run function dungeon:extra/red_switch
