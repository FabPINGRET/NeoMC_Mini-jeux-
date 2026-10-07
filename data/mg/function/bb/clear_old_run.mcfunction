# Suite de clear_old : zone chargée → entités puis blocs
kill @e[type=!minecraft:player,x=-14,y=40,z=13636,dx=28,dy=100,dz=28]
fill -14 58 13636 14 80 13664 minecraft:air
kill @e[type=!minecraft:player,x=-133,y=40,z=13687,dx=26,dy=100,dz=26]
fill -133 56 13687 -107 83 13713 minecraft:air
fill -133 84 13687 -107 111 13713 minecraft:air
kill @e[type=!minecraft:player,x=-85,y=40,z=13687,dx=26,dy=100,dz=26]
fill -85 56 13687 -59 83 13713 minecraft:air
fill -85 84 13687 -59 111 13713 minecraft:air
kill @e[type=!minecraft:player,x=-37,y=40,z=13687,dx=24,dy=100,dz=26]
fill -37 56 13687 -13 83 13713 minecraft:air
fill -37 84 13687 -13 111 13713 minecraft:air
kill @e[type=!minecraft:player,x=13,y=40,z=13687,dx=24,dy=100,dz=26]
fill 13 56 13687 37 83 13713 minecraft:air
fill 13 84 13687 37 111 13713 minecraft:air
kill @e[type=!minecraft:player,x=59,y=40,z=13687,dx=26,dy=100,dz=26]
fill 59 56 13687 85 83 13713 minecraft:air
fill 59 84 13687 85 111 13713 minecraft:air
kill @e[type=!minecraft:player,x=107,y=40,z=13687,dx=26,dy=100,dz=26]
fill 107 56 13687 133 83 13713 minecraft:air
fill 107 84 13687 133 111 13713 minecraft:air
kill @e[type=!minecraft:player,x=-133,y=40,z=13735,dx=26,dy=100,dz=26]
fill -133 56 13735 -107 83 13761 minecraft:air
fill -133 84 13735 -107 111 13761 minecraft:air
kill @e[type=!minecraft:player,x=-85,y=40,z=13735,dx=26,dy=100,dz=26]
fill -85 56 13735 -59 83 13761 minecraft:air
fill -85 84 13735 -59 111 13761 minecraft:air
kill @e[type=!minecraft:player,x=-37,y=40,z=13735,dx=26,dy=100,dz=26]
fill -37 56 13735 -11 83 13761 minecraft:air
fill -37 84 13735 -11 111 13761 minecraft:air
kill @e[type=!minecraft:player,x=11,y=40,z=13735,dx=26,dy=100,dz=26]
fill 11 56 13735 37 83 13761 minecraft:air
fill 11 84 13735 37 111 13761 minecraft:air
kill @e[type=!minecraft:player,x=59,y=40,z=13735,dx=26,dy=100,dz=26]
fill 59 56 13735 85 83 13761 minecraft:air
fill 59 84 13735 85 111 13761 minecraft:air
kill @e[type=!minecraft:player,x=107,y=40,z=13735,dx=26,dy=100,dz=26]
fill 107 56 13735 133 83 13761 minecraft:air
fill 107 84 13735 133 111 13761 minecraft:air
# Libère la zone (core/forceloads retire l'ancienne zone et remet les zones actuelles, dont la parcelle 0)
function mg:core/forceloads
tellraw @a[tag=mg.admin] [{"text":"✔ Anciennes parcelles Build Battle supprimées.","color":"green"}]
