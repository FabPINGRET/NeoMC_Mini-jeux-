# Paintball — début de partie
scoreboard players set $tl mg.st 4800
execute if score $pbm mg.st matches 1 run scoreboard players set $tl mg.st 3600
execute if score $pbm mg.st matches 2 run scoreboard players set $tl mg.st 7200
scoreboard players set $c100 mg.st 100
scoreboard players set $c20 mg.st 20
scoreboard players set $pa mg.st 0
scoreboard players set $pb mg.st 0
tag @a remove mg.prot
tag @a remove mg.qsh
scoreboard players reset @a mg.qs
scoreboard players set @a[tag=mg.play] mg.ph 0
scoreboard players set @a[tag=mg.play] mg.pt 0
scoreboard players set @a[tag=mg.play] mg.pi 200
scoreboard players set @a[tag=mg.play] mg.cd 0
scoreboard players set @a[tag=mg.play] mg.deaths 0
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run function mg:paintball/kit
execute as @a[tag=mg.play] run function mg:paintball/fx
scoreboard players set Orange mg.pb 0
scoreboard players set Bleu mg.pb 0
scoreboard players set Temps mg.pb 240
execute if score $pbm mg.st matches 1 run scoreboard players set Temps mg.pb 180
execute if score $pbm mg.st matches 2 run scoreboard players set Temps mg.pb 360
scoreboard objectives setdisplay sidebar mg.pb
tellraw @a[tag=mg.play] [{"text":"▓ PAINTBALL : ","color":"gold","bold":true},{"text":"peins le terrain à ta couleur (clic droit maintenu) ! Ton encre se recharge vite sur ta propre peinture, où tu cours plus vite ; sur la peinture ennemie tu es ralenti. Touche un adversaire 3 fois pour l'éclabousser. Le plus de terrain peint après 4 min gagne !","color":"gray"}]
tellraw @a[team=mg_red,tag=mg.play] [{"text":"Tu es dans l'équipe ","color":"gray"},{"text":"ORANGE","color":"gold","bold":true}]
tellraw @a[team=mg_blue,tag=mg.play] [{"text":"Tu es dans l'équipe ","color":"gray"},{"text":"BLEUE","color":"blue","bold":true}]
