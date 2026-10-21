# Ombrelune construite : entités permanentes ensuite
execute in mg:ombrelune run kill @e[type=minecraft:item,x=-240,y=0,z=-240,dx=480,dy=300,dz=480]
execute in mg:ombrelune run forceload remove all
data modify storage mg:ombre built set value 1b
data remove storage mg:ombre q
data remove storage mg:ombre doors
tellraw @a[tag=mg.admin] {"text":"🌙 Ombrelune est construite (PNJ et objets en cours de pose).","color":"light_purple"}
function mg:ombre/st/start
