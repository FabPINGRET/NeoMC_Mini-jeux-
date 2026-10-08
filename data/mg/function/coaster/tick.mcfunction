# 🎢 Montagne russe — tick (seulement si quelqu'un est en gare ou en wagon)
execute as @a[x=-111,y=64,z=1,dx=1,dy=1,dz=0,tag=!mg.play,tag=!mg.csr] unless predicate mg:coaster_riding run function mg:coaster/board
tag @a[tag=mg.csr] remove mg.csr
tag @a[x=-111,y=64,z=1,dx=1,dy=1,dz=0] add mg.csr
execute as @e[type=minecraft:minecart,tag=mg.cst,x=-120,y=63,z=-7,dx=6,dy=3,dz=2] run function mg:coaster/arrive
execute as @e[type=minecraft:minecart,tag=mg.cst] unless predicate mg:coaster_has_rider run kill @s
execute as @e[type=minecraft:minecart,tag=mg.cst] at @s if entity @s[y=-64,dy=104] run kill @s
