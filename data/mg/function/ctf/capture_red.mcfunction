# @s (ROUGE) ramène le drapeau BLEU chez lui : +1
scoreboard players add Rouge mg.cf 1
scoreboard players add @s mg.cf 1
function mg:ctf/home_blue
effect clear @s minecraft:glowing
function mg:ctf/kit
tellraw @a[tag=mg.play] [{"text":"🚩 ","color":"red"},{"selector":"@s","color":"red"},{"text":" CAPTURE ! ","color":"gold","bold":true},{"text":"Rouge ","color":"red"},{"score":{"name":"Rouge","objective":"mg.cf"},"color":"red"},{"text":" – ","color":"gray"},{"score":{"name":"Bleu","objective":"mg.cf"},"color":"blue"},{"text":" Bleu","color":"blue"}]
title @a[tag=mg.play] title {"text":"🚩 Capture ROUGE !","color":"red","bold":true}
execute as @a[tag=mg.play] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.8 1.2
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score Rouge mg.cf matches 3.. run function mg:core/win_red
