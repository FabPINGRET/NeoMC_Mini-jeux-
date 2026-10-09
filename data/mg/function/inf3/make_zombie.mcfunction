# @s devient zombie
tag @s add mg.inf
tag @s add mg.gtg
team join mg_green @s
clear @s
function mg:gun/reset
scoreboard players set @s mg.deaths 0
item replace entity @s armor.head with minecraft:zombie_head
item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=4227072,unbreakable={}]
item replace entity @s armor.legs with minecraft:leather_leggings[dyed_color=2116640,unbreakable={}]
item replace entity @s armor.feet with minecraft:leather_boots[dyed_color=2116640,unbreakable={}]
effect give @s minecraft:speed infinite 0 true
effect give @s minecraft:strength infinite 1 true
effect give @s minecraft:saturation infinite 0 true
function mg:inf3/zspawn
title @s title {"text":"🧟 Tu es INFECTÉ","color":"dark_green","bold":true}
title @s subtitle {"text":"tue les survivants pour les contaminer","color":"gray"}
tellraw @a[tag=mg.play] [{"text":"🧪 ","color":"dark_green"},{"selector":"@s","color":"green"},{"text":" a été infecté !","color":"gray"}]
execute as @a[tag=mg.play] at @s run playsound minecraft:entity.zombie_villager.converted master @s ~ ~ ~ 0.8 1
