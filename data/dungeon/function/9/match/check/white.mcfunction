execute unless block -10985 76 -176 #wool run scoreboard players set wm_match_state bool 0
execute if block -10985 76 -176 #wool run scoreboard players set wm_match_state bool 1

setblock ~ ~1 ~ minecraft:white_wool
setblock ~ ~2 ~ minecraft:air
setblock ~ ~2 ~1 minecraft:white_banner[rotation=8]{components:{},patterns:[{color:"black",pattern:"minecraft:cross"},{color:"white",pattern:"minecraft:curly_border"}]}

execute if score wm_match_state bool matches 0 run function dungeon:9/match/1/white
execute if score wm_match_state bool matches 1 run function dungeon:9/match/2/white
