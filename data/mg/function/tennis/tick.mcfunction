# 🎾 Tennis — tick
scoreboard players add $tntm mg.st 1
execute as @a[tag=mg.play,scores={mg.qs=1..}] at @s run function mg:tennis/swing
scoreboard players reset @a[scores={mg.qs=1..}] mg.qs
scoreboard players remove @a[tag=mg.play,scores={mg.tnt=1..}] mg.tnt 1
scoreboard players remove @e[type=minecraft:mannequin,tag=mg.tnrob,scores={mg.tnt=1..}] mg.tnt 1
scoreboard players operation $tnab mg.st = $tntm mg.st
scoreboard players operation $tnab mg.st %= #tn10 mg.st
execute as @e[type=minecraft:marker,tag=mg.tncm] run function mg:tennis/court
execute if score $tntm mg.st matches 8400 run tellraw @a[tag=mg.play] {"text":"🎾 Plus qu'une minute : ensuite, le meilleur de chaque court gagne !","color":"yellow"}
execute if score $state mg.st matches 2 if score $tntm mg.st matches 9600.. run return run function mg:tennis/timeout
execute if score $state mg.st matches 2 unless entity @e[type=minecraft:marker,tag=mg.tncm,scores={mg.tnph=0..3}] run function mg:tennis/finish
