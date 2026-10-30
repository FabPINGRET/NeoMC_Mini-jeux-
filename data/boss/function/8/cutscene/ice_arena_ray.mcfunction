#particle dust_color_transition{from_color:[0.659,0.898,1.000],scale:2,to_color:[0.039,1.000,0.969]} ~ ~ ~ 0.2 0.2 0.2 0 1
particle block{block_state:"packed_ice"} ~ ~ ~ 0.2 0 0.2 0 1
particle snowflake ~ ~ ~ 0.2 0 0.2 0 1

execute positioned ~ ~-0.1 ~ if block ~ ~ ~ air run function boss:8/cutscene/ice_arena_ray
