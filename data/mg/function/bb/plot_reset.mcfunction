# Parcelle 25×25 (herbe, bordure en pierre) — position = bloc central, y=64 ; $bbpi = numéro
execute positioned ~-18 ~-8 ~-18 run kill @e[type=!minecraft:player,dx=36,dy=60,dz=36]
fill ~-17 ~-6 ~-17 ~17 ~5 ~17 minecraft:air
fill ~-17 ~6 ~-17 ~17 ~17 ~17 minecraft:air
fill ~-17 ~18 ~-17 ~17 ~29 ~17 minecraft:air
fill ~-17 ~30 ~-17 ~17 ~41 ~17 minecraft:air
fill ~-12 ~-2 ~-12 ~12 ~-1 ~12 minecraft:dirt
fill ~-12 ~ ~-12 ~12 ~ ~12 minecraft:stone_bricks
fill ~-11 ~ ~-11 ~11 ~ ~11 minecraft:grass_block
setblock ~-12 ~ ~-12 minecraft:sea_lantern
setblock ~12 ~ ~-12 minecraft:sea_lantern
setblock ~-12 ~ ~12 minecraft:sea_lantern
setblock ~12 ~ ~12 minecraft:sea_lantern
summon minecraft:marker ~0.5 ~ ~0.5 {Tags:["mg.bpm","mg.bpn"]}
execute as @e[type=minecraft:marker,tag=mg.bpn] run scoreboard players operation @s mg.bi = $bbpi mg.st
tag @e[type=minecraft:marker,tag=mg.bpn] remove mg.bpn
