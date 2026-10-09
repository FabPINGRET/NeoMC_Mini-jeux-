# @s : balle en jeu qui touche le sol — mg.tnl = frappeur, mg.tnb = rebonds chez le receveur
scoreboard players set $tnbs mg.st 1
execute if score @s mg.tnz matches 0.. run scoreboard players set $tnbs mg.st 2
scoreboard players set $tnin mg.st 0
execute if score @s mg.tnx matches -5500..5500 if score @s mg.tnz matches -12500..12500 run scoreboard players set $tnin mg.st 1
execute if score $tnbs mg.st = @s mg.tnl run scoreboard players set $tnwhy mg.st 4
execute if score $tnbs mg.st = @s mg.tnl run return run function mg:tennis/pt_recv
execute if score @s mg.tnb matches 1.. run scoreboard players set $tnwhy mg.st 3
execute if score @s mg.tnb matches 1.. run return run function mg:tennis/pt_hitter
execute if score $tnin mg.st matches 0 run scoreboard players set $tnwhy mg.st 2
execute if score $tnin mg.st matches 0 run return run function mg:tennis/pt_recv
scoreboard players set @s mg.tnb 1
