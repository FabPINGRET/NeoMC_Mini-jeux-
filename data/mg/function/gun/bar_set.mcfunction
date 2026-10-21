# @s tient une arme : barre de durabilité = progression ($gbt = durée totale, $gbr = ticks restants)
execute unless score $gbt mg.st matches 1.. run return 0
scoreboard players operation $gbar mg.st = $gbt mg.st
scoreboard players operation $gbar mg.st -= $gbr mg.st
scoreboard players set #1000 mg.st 1000
scoreboard players operation $gbar mg.st *= #1000 mg.st
scoreboard players operation $gbar mg.st /= $gbt mg.st
execute if score $gbar mg.st matches ..0 run scoreboard players set $gbar mg.st 1
execute if score $gbar mg.st matches 1000.. run scoreboard players set $gbar mg.st 999
item modify entity @s weapon.mainhand [{function:"minecraft:set_components",components:{"!minecraft:unbreakable":{}}},{function:"minecraft:set_damage",damage:{type:"minecraft:score",target:{type:"minecraft:fixed",name:"$gbar"},score:"mg.st",scale:0.001}}]
