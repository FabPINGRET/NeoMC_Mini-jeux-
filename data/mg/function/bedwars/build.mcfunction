# Bedwars — construction des îles (centre 0 ~ 1200)

# --- Île ROUGE (ouest) ---
fill -37 63 1195 -27 63 1205 minecraft:smooth_stone
fill -37 63 1195 -27 63 1195 minecraft:red_wool
fill -37 63 1205 -27 63 1205 minecraft:red_wool
fill -37 63 1195 -37 63 1205 minecraft:red_wool
fill -27 63 1195 -27 63 1205 minecraft:red_wool
setblock -28 63 1200 minecraft:gold_block
setblock -35 64 1200 minecraft:red_bed[facing=west,part=foot] strict
setblock -36 64 1200 minecraft:red_bed[facing=west,part=head] strict

# --- Île BLEUE (est) ---
fill 27 63 1195 37 63 1205 minecraft:smooth_stone
fill 27 63 1195 37 63 1195 minecraft:blue_wool
fill 27 63 1205 37 63 1205 minecraft:blue_wool
fill 37 63 1195 37 63 1205 minecraft:blue_wool
fill 27 63 1195 27 63 1205 minecraft:blue_wool
setblock 28 63 1200 minecraft:gold_block
setblock 35 64 1200 minecraft:blue_bed[facing=east,part=foot] strict
setblock 36 64 1200 minecraft:blue_bed[facing=east,part=head] strict

# --- Île VERTE (nord) ---
fill -5 63 1163 5 63 1173 minecraft:smooth_stone
fill -5 63 1163 5 63 1163 minecraft:green_wool
fill -5 63 1173 5 63 1173 minecraft:green_wool
fill -5 63 1163 -5 63 1173 minecraft:green_wool
fill 5 63 1163 5 63 1173 minecraft:green_wool
setblock 0 63 1172 minecraft:gold_block
setblock 0 64 1164 minecraft:green_bed[facing=north,part=foot] strict
setblock 0 64 1163 minecraft:green_bed[facing=north,part=head] strict

# --- Île JAUNE (sud) ---
fill -5 63 1227 5 63 1237 minecraft:smooth_stone
fill -5 63 1227 5 63 1227 minecraft:yellow_wool
fill -5 63 1237 5 63 1237 minecraft:yellow_wool
fill -5 63 1227 -5 63 1237 minecraft:yellow_wool
fill 5 63 1227 5 63 1237 minecraft:yellow_wool
setblock 0 63 1228 minecraft:gold_block
setblock 0 64 1236 minecraft:yellow_bed[facing=south,part=foot] strict
setblock 0 64 1237 minecraft:yellow_bed[facing=south,part=head] strict

# --- Île CENTRALE (diamants) ---
fill -4 63 1196 4 63 1204 minecraft:smooth_stone
fill -4 63 1196 4 63 1196 minecraft:polished_andesite
fill -4 63 1204 4 63 1204 minecraft:polished_andesite
fill -4 63 1196 -4 63 1204 minecraft:polished_andesite
fill 4 63 1196 4 63 1204 minecraft:polished_andesite
setblock 0 63 1200 minecraft:diamond_block
