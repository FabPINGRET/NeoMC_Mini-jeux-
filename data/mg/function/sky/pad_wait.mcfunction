# Attend le chargement de la plateforme du mode puis y place les joueurs
execute unless score $game mg.st matches 75 run return 0
execute unless score $state mg.st matches 1..2 run return 0
execute if score $elm mg.st matches 1..2 if function mg:sky/pad1_ld run return run function mg:sky/pad_place
execute if score $elm mg.st matches 3 if function mg:sky/pad3_ld run return run function mg:sky/pad_place
scoreboard players add $skpw mg.st 1
execute if score $skpw mg.st matches 60.. run return run function mg:sky/pad_place
schedule function mg:sky/pad_wait 2t
