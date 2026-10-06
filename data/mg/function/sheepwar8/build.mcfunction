# Sheep War 8 « Nuages voxel » (centre 0 ~ 3900) — plateformes flottantes en gros pavés de laine, béton et quartz :
# la laine est fragile, les tirs de destruction sont spectaculaires.

# Nettoyage
fill -46 72 3880 -23 100 3920 minecraft:air
fill -22 72 3880 0 100 3920 minecraft:air
fill 1 72 3880 23 100 3920 minecraft:air
fill 24 72 3880 46 100 3920 minecraft:air
# --- Nuage RED ---
fill -40 78 3885 -18 83 3915 minecraft:white_wool
fill -38 84 3890 -26 89 3910 minecraft:white_concrete
fill -34 90 3897 -30 95 3903 minecraft:quartz_block
fill -24 84 3885 -18 86 3892 minecraft:white_wool
fill -24 84 3908 -18 86 3915 minecraft:white_wool
fill -19 83 3885 -18 83 3915 minecraft:red_concrete
# --- Nuage BLUE ---
fill 18 78 3885 40 83 3915 minecraft:white_wool
fill 26 84 3890 38 89 3910 minecraft:white_concrete
fill 30 90 3897 34 95 3903 minecraft:quartz_block
fill 18 84 3885 24 86 3892 minecraft:white_wool
fill 18 84 3908 24 86 3915 minecraft:white_wool
fill 18 83 3885 19 83 3915 minecraft:blue_concrete
# --- Petits nuages flottants au centre ---
fill -8 82 3892 -3 85 3897 minecraft:white_wool
fill 3 80 3903 8 83 3908 minecraft:white_wool
fill -3 86 3898 3 88 3902 minecraft:quartz_block
# Murs invisibles tout autour (anti-moutons perdus)
data modify storage mg:wl w set value {x:48,z0:3878,z1:3922}
function mg:sheepwar/walls with storage mg:wl w
