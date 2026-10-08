# Recompte les votes et met à jour le tableau latéral
execute store result score Spleef mg.vb if entity @a[scores={mg.vc=1}]
execute if score Spleef mg.vb matches 0 run scoreboard players reset Spleef mg.vb
execute store result score TNT-Run mg.vb if entity @a[scores={mg.vc=2}]
execute if score TNT-Run mg.vb matches 0 run scoreboard players reset TNT-Run mg.vb
execute store result score PvP mg.vb if entity @a[scores={mg.vc=3}]
execute if score PvP mg.vb matches 0 run scoreboard players reset PvP mg.vb
execute store result score PvP-classes mg.vb if entity @a[scores={mg.vc=4}]
execute if score PvP-classes mg.vb matches 0 run scoreboard players reset PvP-classes mg.vb
execute store result score Bedwars mg.vb if entity @a[scores={mg.vc=5}]
execute if score Bedwars mg.vb matches 0 run scoreboard players reset Bedwars mg.vb
execute store result score Sheep-War mg.vb if entity @a[scores={mg.vc=6}]
execute if score Sheep-War mg.vb matches 0 run scoreboard players reset Sheep-War mg.vb
execute store result score Mob-Arena mg.vb if entity @a[scores={mg.vc=7}]
execute if score Mob-Arena mg.vb matches 0 run scoreboard players reset Mob-Arena mg.vb
execute store result score Splegg mg.vb if entity @a[scores={mg.vc=8}]
execute if score Splegg mg.vb matches 0 run scoreboard players reset Splegg mg.vb
execute store result score Sumo mg.vb if entity @a[scores={mg.vc=9}]
execute if score Sumo mg.vb matches 0 run scoreboard players reset Sumo mg.vb
execute store result score Dropper mg.vb if entity @a[scores={mg.vc=10}]
execute if score Dropper mg.vb matches 0 run scoreboard players reset Dropper mg.vb
execute store result score TNT-Tag mg.vb if entity @a[scores={mg.vc=11}]
execute if score TNT-Tag mg.vb matches 0 run scoreboard players reset TNT-Tag mg.vb
execute store result score Block-Party mg.vb if entity @a[scores={mg.vc=12}]
execute if score Block-Party mg.vb matches 0 run scoreboard players reset Block-Party mg.vb
execute store result score Enclumes mg.vb if entity @a[scores={mg.vc=13}]
execute if score Enclumes mg.vb matches 0 run scoreboard players reset Enclumes mg.vb
execute store result score Turf-Wars mg.vb if entity @a[scores={mg.vc=14}]
execute if score Turf-Wars mg.vb matches 0 run scoreboard players reset Turf-Wars mg.vb
execute store result score Quakecraft mg.vb if entity @a[scores={mg.vc=15}]
execute if score Quakecraft mg.vb matches 0 run scoreboard players reset Quakecraft mg.vb
execute store result score Paintball mg.vb if entity @a[scores={mg.vc=16}]
execute if score Paintball mg.vb matches 0 run scoreboard players reset Paintball mg.vb
execute store result score One-in-Chamber mg.vb if entity @a[scores={mg.vc=17}]
execute if score One-in-Chamber mg.vb matches 0 run scoreboard players reset One-in-Chamber mg.vb
execute store result score Course-glace mg.vb if entity @a[scores={mg.vc=18}]
execute if score Course-glace mg.vb matches 0 run scoreboard players reset Course-glace mg.vb
execute store result score Build-mots mg.vb if entity @a[scores={mg.vc=19}]
execute if score Build-mots mg.vb matches 0 run scoreboard players reset Build-mots mg.vb
execute store result score Build-maitre mg.vb if entity @a[scores={mg.vc=20}]
execute if score Build-maitre mg.vb matches 0 run scoreboard players reset Build-maitre mg.vb
execute store result score Elytra mg.vb if entity @a[scores={mg.vc=21}]
execute if score Elytra mg.vb matches 0 run scoreboard players reset Elytra mg.vb
function mg:vote/sidebar
