# @s = joueur ayant utilisé /trigger mg.bb (note 1 à 5 de la construction affichée)
execute unless score @s mg.bb matches 1..5 run return run scoreboard players reset @s mg.bb
execute unless score $state mg.st matches 2 run return run scoreboard players reset @s mg.bb
execute unless score $game mg.st matches 57..58 run return run scoreboard players reset @s mg.bb
execute unless score $bbp mg.st matches 2 run return run function mg:bb/rate_closed
execute unless entity @s[tag=mg.play] run return run scoreboard players reset @s mg.bb
execute if score @s mg.bi = $bbk mg.st unless score $bbs mg.st matches 1 run return run function mg:bb/rate_own
execute unless score @s mg.br matches 0.. run scoreboard players set @s mg.br 0
scoreboard players operation $bbcs mg.st -= @s mg.br
execute if score @s mg.br matches 0 run scoreboard players add $bbcv mg.st 1
scoreboard players operation @s mg.br = @s mg.bb
scoreboard players operation $bbcs mg.st += @s mg.br
scoreboard players reset @s mg.bb
title @s actionbar [{"text":"★ Note enregistrée : ","color":"gold"},{"score":{"name":"@s","objective":"mg.br"},"color":"yellow","bold":true},{"text":"/5 (modifiable)","color":"gray"}]
execute at @s run playsound minecraft:ui.button.click master @s ~ ~ ~ 1 1.5
