# Compte à rebours du kart retenu (vrai) tant que tous les pilotes n'ont pas choisi leur kart, 1 minute au plus
execute if score $timer mg.st matches 61 as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.bit master @s ~ ~ ~ 1 0.7
execute if score $timer mg.st matches 41 as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.bit master @s ~ ~ ~ 1 0.7
execute if score $timer mg.st matches 21 as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.bit master @s ~ ~ ~ 1 0.7
execute if score $timer mg.st matches 101 run title @a[tag=mg.play] subtitle [{"text":"🎥 Appuie sur ","color":"gray"},{"text":"F5","color":"yellow","bold":true},{"text":" pour voir ton kart en 3e personne","color":"gray"}]
execute unless entity @a[tag=mg.play,tag=!mg.kok] run return fail
execute if score $kwait mg.st matches 1200.. run return fail
scoreboard players add $kwait mg.st 1
scoreboard players enable @a[tag=mg.play] mg.kch
execute as @a[tag=mg.play] if score @s mg.kch matches 1.. run function mg:kart/choose
execute store result score $knr mg.st if entity @a[tag=mg.play,tag=!mg.kok]
scoreboard players set $kws mg.st 1200
scoreboard players operation $kws mg.st -= $kwait mg.st
scoreboard players operation $kws mg.st /= #k20 mg.st
scoreboard players operation $kwm mg.st = $kwait mg.st
scoreboard players operation $kwm mg.st %= #k10 mg.st
execute if score $kwm mg.st matches 0 run title @a[tag=mg.play,tag=mg.kok] actionbar [{"text":"⏳ En attente de ","color":"gray"},{"score":{"name":"$knr","objective":"mg.st"},"color":"yellow","bold":true},{"text":" pilote(s) qui choisissent leur kart... ","color":"gray"},{"score":{"name":"$kws","objective":"mg.st"},"color":"gold"},{"text":" s","color":"gold"}]
execute if score $kwm mg.st matches 0 run title @a[tag=mg.play,tag=!mg.kok] actionbar [{"text":"🏎 Choisis ton kart ! ","color":"gold","bold":true},{"text":"Départ dans ","color":"gray"},{"score":{"name":"$kws","objective":"mg.st"},"color":"yellow"},{"text":" s au plus","color":"gray"}]
execute if score $kwm mg.st matches 0 as @a[tag=mg.play] run function mg:kart/place_seat
execute if score $kwait mg.st matches 200 run tellraw @a[tag=mg.play,tag=!mg.kok] [{"text":"🏎 ","color":"gold"},{"text":"[Choisir mon kart]","color":"yellow","bold":true,"click_event":{"action":"run_command","command":"trigger mg.kch set 30"}},{"text":" : la course attend ton choix.","color":"gray"}]
execute if score $kwait mg.st matches 800 run tellraw @a[tag=mg.play,tag=!mg.kok] [{"text":"🏎 ","color":"gold"},{"text":"[Choisir mon kart]","color":"yellow","bold":true,"click_event":{"action":"run_command","command":"trigger mg.kch set 30"}},{"text":" : départ dans 20 secondes !","color":"gray"}]
return 1
