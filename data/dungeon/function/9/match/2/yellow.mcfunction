execute if block -10985 76 -176 minecraft:yellow_wool run scoreboard players set wm_match_yellow bool 1
execute if block -10985 76 -176 minecraft:yellow_wool run scoreboard players set wm_match_correctflag bool 1

fill -11001 81 -188 -10987 81 -182 air replace minecraft:polished_blackstone_button

function dungeon:9/match/wincheck

#Delay until state 1
setblock -11005 76 -181 minecraft:redstone_block
