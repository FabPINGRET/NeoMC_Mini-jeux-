execute unless block -10985 76 -176 #wool run scoreboard players set wm_match_state bool 0
execute if block -10985 76 -176 #wool run scoreboard players set wm_match_state bool 1

setblock ~ ~1 ~ minecraft:purple_wool
setblock ~ ~2 ~ minecraft:air
setblock ~ ~2 ~1 minecraft:purple_banner[rotation=8]{components:{},patterns:[{color:"white",pattern:"minecraft:flow"}]}

execute if score wm_match_state bool matches 0 run function dungeon:9/match/1/purple
execute if score wm_match_state bool matches 1 run function dungeon:9/match/2/purple
