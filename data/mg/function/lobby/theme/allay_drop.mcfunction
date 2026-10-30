# Allay du thème qui tient un objet (@s, position = allay) : l'objet retombe au sol
summon minecraft:item ~ ~ ~ {Tags:["mg.thdrop","mg.keep"],Item:{id:"minecraft:stone",count:1},PickupDelay:10s}
data modify entity @e[type=minecraft:item,tag=mg.thdrop,limit=1] Item set from entity @s equipment.mainhand
tag @e[tag=mg.thdrop] remove mg.thdrop
item replace entity @s weapon.mainhand with minecraft:air
