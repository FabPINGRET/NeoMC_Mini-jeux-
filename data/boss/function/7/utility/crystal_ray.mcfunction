execute as @a[distance=..2,tag=mg.flw] run damage @s 12 minecraft:indirect_magic by @n[tag=st_hand_loc,distance=0..]

execute if score boss:st_prism_color Value matches 1 run particle dust{scale:1,color:[1,0,0]} ^ ^ ^ 0.05 0.05 0.05 0 1
execute if score boss:st_prism_color Value matches 2 run particle dust{scale:1,color:[1.0,0.5,0.0]} ^ ^ ^ 0.05 0.05 0.05 0 1
execute if score boss:st_prism_color Value matches 3 run particle dust{scale:1,color:[1,1,0]} ^ ^ ^ 0.05 0.05 0.05 0 1
execute if score boss:st_prism_color Value matches 4 run particle dust{scale:1,color:[0.5,1.0,0.0]} ^ ^ ^ 0.05 0.05 0.05 0 1
execute if score boss:st_prism_color Value matches 5 run particle dust{scale:1,color:[0,1,0]} ^ ^ ^ 0.05 0.05 0.05 0 1
execute if score boss:st_prism_color Value matches 6 run particle dust{scale:1,color:[0.0,1.0,0.5]} ^ ^ ^ 0.05 0.05 0.05 0 1
execute if score boss:st_prism_color Value matches 7 run particle dust{scale:1,color:[0,1,1]} ^ ^ ^ 0.05 0.05 0.05 0 1
execute if score boss:st_prism_color Value matches 8 run particle dust{scale:1,color:[0.0,0.5,1.0]} ^ ^ ^ 0.05 0.05 0.05 0 1
execute if score boss:st_prism_color Value matches 9 run particle dust{scale:1,color:[0,0,1]} ^ ^ ^ 0.05 0.05 0.05 0 1
execute if score boss:st_prism_color Value matches 10 run particle dust{scale:1,color:[0.5,0.0,1.0]} ^ ^ ^ 0.05 0.05 0.05 0 1
execute if score boss:st_prism_color Value matches 11 run particle dust{scale:1,color:[1,0,1]} ^ ^ ^ 0.05 0.05 0.05 0 1
execute if score boss:st_prism_color Value matches 12 run particle dust{scale:1,color:[1.0,0.0,0.5]} ^ ^ ^ 0.05 0.05 0.05 0 1

execute if block ^ ^ ^ air positioned ^ ^ ^0.1 run function boss:7/utility/crystal_ray
