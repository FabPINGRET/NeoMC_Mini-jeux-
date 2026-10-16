# Vallée de Terra Nova prête : drapeau, puis construction des régions du RPG
execute in mg:terranova run kill @e[type=minecraft:item,x=-100,y=40,z=-100,dx=200,dy=80,dz=200]
execute in mg:terranova if block 0 64 0 minecraft:chiseled_stone_bricks run data modify storage mg:terra built set value 1b
function mg:terra/world_build2
