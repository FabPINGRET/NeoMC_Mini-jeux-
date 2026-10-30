execute if score icelorn_overdrive bool matches 0 run item replace entity @s armor.head from block -10056 105 188 container.9
execute if score icelorn_overdrive bool matches 0 run data modify entity @s equipment.chest.components."minecraft:trim".material set value diamond
execute if score icelorn_overdrive bool matches 0 run data modify entity @s equipment.legs.components."minecraft:trim".material set value diamond
execute if score icelorn_overdrive bool matches 0 run data modify entity @s equipment.feet.components."minecraft:trim".material set value diamond

execute if score icelorn_overdrive bool matches 1 run item replace entity @s armor.head from block -10056 105 188 container.18
execute if score icelorn_overdrive bool matches 1 run data modify entity @s equipment.chest.components."minecraft:trim".material set value redstone
execute if score icelorn_overdrive bool matches 1 run data modify entity @s equipment.legs.components."minecraft:trim".material set value redstone
execute if score icelorn_overdrive bool matches 1 run data modify entity @s equipment.feet.components."minecraft:trim".material set value redstone
