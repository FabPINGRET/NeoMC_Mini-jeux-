# 🎢 Montagne russe — tick (seulement si quelqu'un est au guichet ou en wagon)
execute as @a[x=-45,y=64,z=41,dx=0,dy=1,dz=0,tag=!mg.play,tag=!mg.csr] unless predicate mg:coaster_riding run function mg:coaster/board
tag @a[tag=mg.csr] remove mg.csr
tag @a[x=-45,y=64,z=41,dx=0,dy=1,dz=0] add mg.csr
execute as @e[type=minecraft:minecart,tag=mg.cst,x=-65,y=85,z=33,dx=2,dy=3,dz=3] run function mg:coaster/arrive
execute as @e[type=minecraft:minecart,tag=mg.cst] unless predicate mg:coaster_has_rider run kill @s
execute as @e[type=minecraft:minecart,tag=mg.cst] at @s if entity @s[y=-64,dy=140] run kill @s
