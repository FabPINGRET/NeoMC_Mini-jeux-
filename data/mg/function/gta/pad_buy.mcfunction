# @s : achat du contenu du présentoir ($gpt) si assez de dollars (villa : gratuit si déjà acheté)
tag @s add mg.gbuy
scoreboard players set $gpr mg.st 0
execute if score $gpt mg.st matches 31..49 run return run function mg:gta/villa_take
execute if score $gpt mg.st matches 2 run scoreboard players set $gpr mg.st 150
execute if score $gpt mg.st matches 3 run scoreboard players set $gpr mg.st 200
execute if score $gpt mg.st matches 4 run scoreboard players set $gpr mg.st 300
execute if score $gpt mg.st matches 5 run scoreboard players set $gpr mg.st 450
execute if score $gpt mg.st matches 6 run scoreboard players set $gpr mg.st 800
execute if score $gpt mg.st matches 7 run scoreboard players set $gpr mg.st 650
execute if score $gpt mg.st matches 8 run scoreboard players set $gpr mg.st 50
execute if score $gpt mg.st matches 9 run scoreboard players set $gpr mg.st 120
execute if score $gpt mg.st matches 21 run scoreboard players set $gpr mg.st 400
execute if score $gpt mg.st matches 22 run scoreboard players set $gpr mg.st 900
execute if score $gpt mg.st matches 23 run scoreboard players set $gpr mg.st 1800
execute if score $gpt mg.st matches 24 run scoreboard players set $gpr mg.st 3000
execute if score $gpt mg.st matches 25 run scoreboard players set $gpr mg.st 4500
execute if score @s mg.gta < $gpr mg.st run scoreboard players set @s mg.gal 40
execute if score @s mg.gta < $gpr mg.st run playsound minecraft:entity.villager.no player @s ~ ~ ~ 0.8 1
execute if score @s mg.gta < $gpr mg.st run return run title @s actionbar [{"text":"💸 Pas assez d'argent : il faut ","color":"red"},{"score":{"name":"$gpr","objective":"mg.st"},"color":"gold","bold":true},{"text":" $. Braque des passants, des commerces ou la banque !","color":"red"}]
scoreboard players operation @s mg.gta -= $gpr mg.st
scoreboard players set $gok mg.st 1
function mg:gta/unlock
execute if score $gpt mg.st matches 52..57 run scoreboard players remove $gpt mg.st 50
function mg:gta/pad_give
execute if score $gpr mg.st matches 1.. run playsound minecraft:block.note_block.chime player @s ~ ~ ~ 0.8 1.4
