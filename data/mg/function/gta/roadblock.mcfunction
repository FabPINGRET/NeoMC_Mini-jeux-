# Barrage de police (4 ★) à ce carrefour : deux voitures en travers, quatre policiers
execute positioned ~-2 ~ ~ run function mg:gta/car/spawn_5
execute as @e[type=minecraft:horse,tag=mg.gcarh] if score @s mg.gvid = $gvid mg.st run function mg:gta/roadblock_car
execute positioned ~2 ~ ~ run function mg:gta/car/spawn_5
execute as @e[type=minecraft:horse,tag=mg.gcarh] if score @s mg.gvid = $gvid mg.st run function mg:gta/roadblock_car
function mg:gta/cop_spawn
execute positioned ~ ~ ~2 run function mg:gta/cop_spawn
summon minecraft:marker ~ ~ ~ {Tags:["mg.gta","mg.grblk"]}
tellraw @a[tag=mg.gtw,scores={mg.gwl=4..},distance=..80] {"text":"🚧 Barrage de police à proximité !","color":"red","bold":true}
