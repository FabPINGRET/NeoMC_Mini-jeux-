# @s = nouveau porteur de la bombe
item replace entity @s armor.head with minecraft:tnt[custom_name=[{"text":"BOMBE","color":"red","bold":true,"italic":false}]]
effect give @s minecraft:speed infinite 0 true
effect give @s minecraft:glowing infinite 0 true
title @s title [{"text":"✹ TU AS LA BOMBE !","color":"red","bold":true}]
title @s subtitle [{"text":"Frappe quelqu'un pour la lui passer","color":"gray"}]
execute at @s run playsound minecraft:entity.tnt.primed master @a ~ ~ ~ 1.2 1
