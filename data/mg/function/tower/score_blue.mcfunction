# @s (Bleu) est tombé dans le puits adverse
scoreboard players add Bleu mg.tw 1
scoreboard players add @s mg.tw 1
tellraw @a[tag=mg.play] [{"text":"🏰 ","color":"blue"},{"selector":"@s","color":"blue"},{"text":" marque dans le puits adverse ! ","color":"gray"},{"text":"Rouge ","color":"red"},{"score":{"name":"Rouge","objective":"mg.tw"},"color":"red"},{"text":" – ","color":"gray"},{"score":{"name":"Bleu","objective":"mg.tw"},"color":"blue"},{"text":" Bleu","color":"blue"}]
execute as @a[tag=mg.play] at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.4
function mg:tower/spawn
effect give @s minecraft:instant_health 1 4 true
execute if score $state mg.st matches 2 if score Bleu mg.tw matches 5.. run function mg:core/win_blue
