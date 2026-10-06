# Début du tour du joueur n° $mpt (absent ou spectateur : on passe au suivant)
tag @a remove mg.mpcur
execute as @a[tag=mg.mpp,tag=mg.mpview] if score @s mg.mpo = $mpt mg.st run function mg:party/view_end
execute as @a[tag=mg.mpp,tag=mg.play] if score @s mg.mpo = $mpt mg.st run tag @s add mg.mpcur
execute unless entity @a[tag=mg.mpcur] run return run function mg:party/next_turn

scoreboard players set $mph mg.st 1
scoreboard players set $mpw mg.st 400
scoreboard players set $mpch mg.st 0
data modify entity @e[type=minecraft:text_display,tag=mg.mpdice,limit=1] text set value [{"text":"?","color":"white","bold":true}]
execute as @a[tag=mg.mpcur] run function mg:party/give_dice
tellraw @a[tag=mg.mpp] [{"text":"➤ Au tour de ","color":"gray"},{"selector":"@a[tag=mg.mpcur]","color":"yellow","bold":true},{"text":" ! ","color":"gray"},{"text":"[🗺 voir la carte]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.dice set 3"},"hover_event":{"action":"show_text","value":"Vue du ciel pendant 6 s"}}]
