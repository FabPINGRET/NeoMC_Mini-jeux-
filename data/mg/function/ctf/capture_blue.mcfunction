# @s (BLEU) ramène le drapeau ROUGE chez lui : +1
scoreboard players add Bleu mg.cf 1
scoreboard players add @s mg.cf 1
function mg:ctf/home_red
effect clear @s minecraft:glowing
function mg:ctf/kit
tellraw @a[tag=mg.play] [{"text":"🚩 ","color":"blue"},{"selector":"@s","color":"blue"},{"text":" CAPTURE ! ","color":"gold","bold":true},{"text":"Rouge ","color":"red"},{"score":{"name":"Rouge","objective":"mg.cf"},"color":"red"},{"text":" – ","color":"gray"},{"score":{"name":"Bleu","objective":"mg.cf"},"color":"blue"},{"text":" Bleu","color":"blue"}]
title @a[tag=mg.play] title {"text":"🚩 Capture BLEU !","color":"blue","bold":true}
execute as @a[tag=mg.play] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.8 1.2
execute if score $state mg.st matches 2 if score Bleu mg.cf matches 3.. run function mg:core/win_blue
