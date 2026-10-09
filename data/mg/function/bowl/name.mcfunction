# @s : son nom sur le tableau de sa piste (résolu par set_name sur un objet temporaire)
item replace entity @s hotbar.8 with minecraft:paper
item modify entity @s hotbar.8 {function:"minecraft:set_name",entity:"this",target:"custom_name",name:{selector:"@s"}}
data modify storage mg:bowl n set value {text:"?"}
data modify storage mg:bowl n set from entity @s Inventory[{Slot:8b}].components."minecraft:custom_name"
item replace entity @s hotbar.8 with minecraft:air
execute store result storage mg:bowl q.l int 1 run scoreboard players get @s mg.bln
function mg:bowl/name_set with storage mg:bowl q
