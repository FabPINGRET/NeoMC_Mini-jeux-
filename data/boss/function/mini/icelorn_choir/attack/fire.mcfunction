item replace entity @s armor.head from block -10056 105 188 container.0
data modify entity @s equipment.chest.components."minecraft:trim".material set value netherite
data modify entity @s equipment.legs.components."minecraft:trim".material set value netherite
data modify entity @s equipment.feet.components."minecraft:trim".material set value netherite

execute as @s at @s positioned ~ ~0.8 ~ facing ^ ^ ^1 positioned ^ ^ ^1 run function boss:mini/icelorn_choir/attack/note_ray

playsound minecraft:entity.happy_ghast.ambient hostile @a[tag=mg.flw] ~ ~ ~ 1 2
playsound minecraft:item.ominous_bottle.dispose hostile @a[tag=mg.flw] ~ ~ ~ 1 2
