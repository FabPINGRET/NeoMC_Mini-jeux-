# Dés : 2d6 du joueur contre 2d6 du croupier
execute store result score $gd1 mg.st run random value 2..12
execute store result score $gd2 mg.st run random value 2..12
title @s title [{"text":"🎲 ","color":"white"},{"score":{"name":"$gd1","objective":"mg.st"},"color":"aqua","bold":true},{"text":"  contre  ","color":"gray"},{"score":{"name":"$gd2","objective":"mg.st"},"color":"red","bold":true}]
scoreboard players set #2 mg.st 2
execute if score $gd1 mg.st > $gd2 mg.st run scoreboard players operation $gwin mg.st = $gbet mg.st
execute if score $gd1 mg.st > $gd2 mg.st run scoreboard players operation $gwin mg.st *= #2 mg.st
execute if score $gd1 mg.st > $gd2 mg.st run scoreboard players operation @s mg.gta += $gwin mg.st
execute if score $gd1 mg.st > $gd2 mg.st run title @s subtitle [{"text":"+","color":"green"},{"score":{"name":"$gwin","objective":"mg.st"},"color":"green","bold":true},{"text":" $","color":"green"}]
execute if score $gd1 mg.st = $gd2 mg.st run scoreboard players operation @s mg.gta += $gbet mg.st
execute if score $gd1 mg.st = $gd2 mg.st run title @s subtitle {"text":"Égalité : mise rendue","color":"yellow"}
execute if score $gd1 mg.st < $gd2 mg.st run title @s subtitle [{"text":"-","color":"red"},{"score":{"name":"$gbet","objective":"mg.st"},"color":"red"},{"text":" $","color":"red"}]
execute at @s run playsound minecraft:block.note_block.hat player @s ~ ~ ~ 1 1.4
function mg:gta/cas_reopen {d:"dice"}
