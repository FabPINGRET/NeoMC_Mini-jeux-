# Roulette (macro $(p) : 1 rouge, 2 noir, 3 vert) : 37 cases, 0 vert, 1..18 rouge, 19..36 noir
execute store result score $gr mg.st run random value 0..36
scoreboard players set $gok mg.st 0
scoreboard players set #p1 mg.st 0
scoreboard players set #p2 mg.st 0
scoreboard players set #p3 mg.st 0
$scoreboard players set #p$(p) mg.st 1
execute if score $gr mg.st matches 1..18 if score #p1 mg.st matches 1 run scoreboard players set $gok mg.st 2
execute if score $gr mg.st matches 19..36 if score #p2 mg.st matches 1 run scoreboard players set $gok mg.st 2
execute if score $gr mg.st matches 0 if score #p3 mg.st matches 1 run scoreboard players set $gok mg.st 36
execute if score $gr mg.st matches 0 run title @s title [{"text":"🟢 ","color":"green"},{"score":{"name":"$gr","objective":"mg.st"},"color":"green","bold":true}]
execute if score $gr mg.st matches 1..18 run title @s title [{"text":"🔴 ","color":"red"},{"score":{"name":"$gr","objective":"mg.st"},"color":"red","bold":true}]
execute if score $gr mg.st matches 19..36 run title @s title [{"text":"⚫ ","color":"dark_gray"},{"score":{"name":"$gr","objective":"mg.st"},"color":"white","bold":true}]
execute if score $gok mg.st matches 0 run title @s subtitle [{"text":"-","color":"red"},{"score":{"name":"$gbet","objective":"mg.st"},"color":"red"},{"text":" $","color":"red"}]
execute if score $gok mg.st matches 0 at @s run playsound minecraft:block.note_block.bass player @s ~ ~ ~ 1 0.6
execute if score $gok mg.st matches 1.. run scoreboard players operation $gwin mg.st = $gbet mg.st
execute if score $gok mg.st matches 1.. run scoreboard players operation $gwin mg.st *= $gok mg.st
execute if score $gok mg.st matches 1.. run scoreboard players operation @s mg.gta += $gwin mg.st
execute if score $gok mg.st matches 1.. run title @s subtitle [{"text":"+","color":"green"},{"score":{"name":"$gwin","objective":"mg.st"},"color":"green","bold":true},{"text":" $","color":"green"}]
execute if score $gok mg.st matches 1.. at @s run playsound minecraft:entity.player.levelup player @s ~ ~ ~ 1 1.3
execute at @s run playsound minecraft:block.wooden_button.click_on player @s ~ ~ ~ 1 1.8
function mg:gta/cas_reopen {d:"roulette"}
