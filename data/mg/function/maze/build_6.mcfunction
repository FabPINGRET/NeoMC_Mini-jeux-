# Marqueurs, panneau de sortie ; ouverture du sas si la partie a déjà commencé
execute if score $jv mg.st matches 1 run function mg:maze/ents_1
execute if score $jv mg.st matches 2 run function mg:maze/ents_2
execute if score $jv mg.st matches 3 run function mg:maze/ents_3
scoreboard players set $jg mg.st 0
scoreboard players set $jok mg.st 1
summon minecraft:text_display 53 67.5 41100 {Tags:["mg.jent"],billboard:"center",text:{"text":"🏆 SORTIE","color":"gold","bold":true}}
execute if score $state mg.st matches 2 run function mg:maze/open
