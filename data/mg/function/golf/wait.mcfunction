# Attend le chargement de la zone puis construit (si le bloc témoin manque) ou passe directement à golf/ready
execute unless score $game mg.st matches 215 run return 0
execute unless score $state mg.st matches 1..2 run return 0
scoreboard players add $gfwait mg.st 1
execute if score $gfwait mg.st matches 60.. run return run tellraw @a[tag=mg.admin] {"text":"[Mini-Jeux] Golf : zone pas chargée.","color":"red"}
execute unless loaded 200 64 34500 run return run schedule function mg:golf/wait 10t
execute unless loaded 400 64 34500 run return run schedule function mg:golf/wait 10t
execute unless loaded 200 64 34700 run return run schedule function mg:golf/wait 10t
execute unless loaded 400 64 34700 run return run schedule function mg:golf/wait 10t
execute unless loaded 300 64 34600 run return run schedule function mg:golf/wait 10t
execute unless block 300 55 34602 minecraft:lodestone run return run function mg:golf/build
function mg:golf/ready
