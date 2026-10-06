# Sheep War 4 « Cubes Voxel » (centre 0 ~ 2700) — deux cubes 20x20x20 suspendus, 3 étages béton, façades en grès,
# grandes ouvertures face à face ; départ au dernier étage. Échelles dans le fond de chaque cube.

# Nettoyage
fill -44 68 2684 -22 100 2716 minecraft:air
fill -21 68 2684 0 100 2716 minecraft:air
fill 1 68 2684 22 100 2716 minecraft:air
fill 23 68 2684 44 100 2716 minecraft:air
# --- Cube RED (20x20x20, face avant en x=+-12) ---
fill -31 72 2690 -12 91 2709 minecraft:cut_red_sandstone hollow
fill -30 72 2691 -13 72 2708 minecraft:red_concrete
fill -30 78 2691 -13 78 2708 minecraft:red_concrete
fill -30 84 2691 -13 84 2708 minecraft:red_concrete
fill -12 73 2693 -12 76 2706 minecraft:air
fill -12 79 2693 -12 82 2706 minecraft:air
fill -12 85 2693 -12 89 2706 minecraft:air
fill -30 73 2694 -30 86 2694 minecraft:ladder[facing=east]
fill -30 73 2705 -30 86 2705 minecraft:ladder[facing=east]
setblock -18 77 2695 minecraft:sea_lantern
setblock -18 77 2704 minecraft:sea_lantern
setblock -26 77 2695 minecraft:sea_lantern
setblock -26 77 2704 minecraft:sea_lantern
setblock -18 83 2695 minecraft:sea_lantern
setblock -18 83 2704 minecraft:sea_lantern
setblock -26 83 2695 minecraft:sea_lantern
setblock -26 83 2704 minecraft:sea_lantern
setblock -18 90 2695 minecraft:sea_lantern
setblock -18 90 2704 minecraft:sea_lantern
setblock -26 90 2695 minecraft:sea_lantern
setblock -26 90 2704 minecraft:sea_lantern
# --- Cube BLUE (20x20x20, face avant en x=+-12) ---
fill 12 72 2690 31 91 2709 minecraft:cut_sandstone hollow
fill 13 72 2691 30 72 2708 minecraft:blue_concrete
fill 13 78 2691 30 78 2708 minecraft:blue_concrete
fill 13 84 2691 30 84 2708 minecraft:blue_concrete
fill 12 73 2693 12 76 2706 minecraft:air
fill 12 79 2693 12 82 2706 minecraft:air
fill 12 85 2693 12 89 2706 minecraft:air
fill 30 73 2694 30 86 2694 minecraft:ladder[facing=west]
fill 30 73 2705 30 86 2705 minecraft:ladder[facing=west]
setblock 18 77 2695 minecraft:sea_lantern
setblock 18 77 2704 minecraft:sea_lantern
setblock 26 77 2695 minecraft:sea_lantern
setblock 26 77 2704 minecraft:sea_lantern
setblock 18 83 2695 minecraft:sea_lantern
setblock 18 83 2704 minecraft:sea_lantern
setblock 26 83 2695 minecraft:sea_lantern
setblock 26 83 2704 minecraft:sea_lantern
setblock 18 90 2695 minecraft:sea_lantern
setblock 18 90 2704 minecraft:sea_lantern
setblock 26 90 2695 minecraft:sea_lantern
setblock 26 90 2704 minecraft:sea_lantern
# Murs invisibles tout autour (anti-moutons perdus)
data modify storage mg:wl w set value {x:46,z0:2682,z1:2718}
function mg:sheepwar/walls with storage mg:wl w
