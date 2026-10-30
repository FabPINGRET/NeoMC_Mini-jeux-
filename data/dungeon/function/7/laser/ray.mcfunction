particle egg_crack ^ ^ ^ 0.15 0.15 0.15 0 1

execute if entity @s[tag=due_east] if block ^ ^ ^ structure_void if entity @e[tag=st_mirror,dx=0.1,dy=0.1,dz=0.1,tag=nw] run tag @s add change_north
execute if entity @s[tag=due_west] if block ^ ^ ^ structure_void if entity @e[tag=st_mirror,dx=0.1,dy=0.1,dz=0.1,tag=ne] run tag @s add change_north

execute if entity @s[tag=due_east] if block ^ ^ ^ structure_void if entity @e[tag=st_mirror,dx=0.1,dy=0.1,dz=0.1,tag=sw] run tag @s add change_south
execute if entity @s[tag=due_west] if block ^ ^ ^ structure_void if entity @e[tag=st_mirror,dx=0.1,dy=0.1,dz=0.1,tag=se] run tag @s add change_south

execute if entity @s[tag=due_north] if block ^ ^ ^ structure_void if entity @e[tag=st_mirror,dx=0.1,dy=0.1,dz=0.1,tag=se] run tag @s add change_east
execute if entity @s[tag=due_south] if block ^ ^ ^ structure_void if entity @e[tag=st_mirror,dx=0.1,dy=0.1,dz=0.1,tag=ne] run tag @s add change_east

execute if entity @s[tag=due_north] if block ^ ^ ^ structure_void if entity @e[tag=st_mirror,dx=0.1,dy=0.1,dz=0.1,tag=sw] run tag @s add change_west
execute if entity @s[tag=due_south] if block ^ ^ ^ structure_void if entity @e[tag=st_mirror,dx=0.1,dy=0.1,dz=0.1,tag=nw] run tag @s add change_west

execute if entity @s[tag=due_east] if block ^ ^ ^ structure_void if entity @e[tag=st_mirror,dx=0.1,dy=0.1,dz=0.1,tag=ne] run tag @s remove due_east
execute if entity @s[tag=due_east] if block ^ ^ ^ structure_void if entity @e[tag=st_mirror,dx=0.1,dy=0.1,dz=0.1,tag=se] run tag @s remove due_east

execute if entity @s[tag=due_west] if block ^ ^ ^ structure_void if entity @e[tag=st_mirror,dx=0.1,dy=0.1,dz=0.1,tag=nw] run tag @s remove due_west
execute if entity @s[tag=due_west] if block ^ ^ ^ structure_void if entity @e[tag=st_mirror,dx=0.1,dy=0.1,dz=0.1,tag=sw] run tag @s remove due_west

execute if entity @s[tag=due_north] if block ^ ^ ^ structure_void if entity @e[tag=st_mirror,dx=0.1,dy=0.1,dz=0.1,tag=ne] run tag @s remove due_north
execute if entity @s[tag=due_north] if block ^ ^ ^ structure_void if entity @e[tag=st_mirror,dx=0.1,dy=0.1,dz=0.1,tag=nw] run tag @s remove due_north

execute if entity @s[tag=due_south] if block ^ ^ ^ structure_void if entity @e[tag=st_mirror,dx=0.1,dy=0.1,dz=0.1,tag=se] run tag @s remove due_south
execute if entity @s[tag=due_south] if block ^ ^ ^ structure_void if entity @e[tag=st_mirror,dx=0.1,dy=0.1,dz=0.1,tag=sw] run tag @s remove due_south


execute if entity @s[tag=change_north] run tag @s remove due_east
execute if entity @s[tag=change_north] run tag @s remove due_west
execute if entity @s[tag=change_north] run tag @s add due_north

execute if entity @s[tag=change_south] run tag @s remove due_east
execute if entity @s[tag=change_south] run tag @s remove due_west
execute if entity @s[tag=change_south] run tag @s add due_south

execute if entity @s[tag=change_east] run tag @s remove due_north
execute if entity @s[tag=change_east] run tag @s remove due_south
execute if entity @s[tag=change_east] run tag @s add due_east

execute if entity @s[tag=change_west] run tag @s remove due_north
execute if entity @s[tag=change_west] run tag @s remove due_south
execute if entity @s[tag=change_west] run tag @s add due_west

tag @s remove change_north
tag @s remove change_south
tag @s remove change_west
tag @s remove change_east

execute if block ^ ^ ^ white_stained_glass_pane at @s run setblock ~ ~-5 ~ redstone_block
execute if block ^ ^ ^ white_stained_glass_pane run fill ~-3 ~-3 ~-3 ~3 ~3 ~3 lime_stained_glass replace white_stained_glass
execute if block ^ ^ ^ white_stained_glass_pane run fill ~-3 ~-3 ~-3 ~3 ~3 ~3 lime_stained_glass_pane replace white_stained_glass_pane

execute unless block ^ ^ ^ air unless block ^ ^ ^ structure_void run tag @s remove due_east
execute unless block ^ ^ ^ air unless block ^ ^ ^ structure_void run tag @s remove due_west
execute unless block ^ ^ ^ air unless block ^ ^ ^ structure_void run tag @s remove due_north
execute unless block ^ ^ ^ air unless block ^ ^ ^ structure_void run tag @s remove due_south


execute if entity @s[tag=due_east] if block ^ ^ ^ air positioned ~1 ~ ~ run function dungeon:7/laser/ray
execute if entity @s[tag=due_west] if block ^ ^ ^ air positioned ~-1 ~ ~ run function dungeon:7/laser/ray
execute if entity @s[tag=due_south] if block ^ ^ ^ air positioned ~ ~ ~1 run function dungeon:7/laser/ray
execute if entity @s[tag=due_north] if block ^ ^ ^ air positioned ~ ~ ~-1 run function dungeon:7/laser/ray

execute if entity @s[tag=due_east] if block ^ ^ ^ structure_void positioned ~1 ~ ~ run function dungeon:7/laser/ray
execute if entity @s[tag=due_west] if block ^ ^ ^ structure_void positioned ~-1 ~ ~ run function dungeon:7/laser/ray
execute if entity @s[tag=due_south] if block ^ ^ ^ structure_void positioned ~ ~ ~1 run function dungeon:7/laser/ray
execute if entity @s[tag=due_north] if block ^ ^ ^ structure_void positioned ~ ~ ~-1 run function dungeon:7/laser/ray
