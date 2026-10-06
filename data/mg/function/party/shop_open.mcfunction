# Boutique (@s) : arrêt du déplacement, fenêtre d'achat (15 s)
scoreboard players operation $tmp mg.st = @s mg.mid
scoreboard players operation $tmp mg.st += @s mg.mit
scoreboard players operation $tmp mg.st += @s mg.mip
execute if score $tmp mg.st matches 3.. run tellraw @s [{"text":"🛒 Boutique : ton sac est plein (3 objets).","color":"gray"}]
execute if score $tmp mg.st matches 3.. run return run function mg:party/shop_close
scoreboard players set $mph mg.st 8
scoreboard players set $mpw mg.st 300
title @s title [{"text":"🛒 BOUTIQUE","color":"light_purple","bold":true}]
title @s subtitle [{"text":"Achète un objet dans la fenêtre","color":"yellow"}]
tellraw @a[tag=mg.mpp,tag=!mg.mpcur] [{"selector":"@s","color":"yellow"},{"text":" s'arrête à la boutique 🛒","color":"gray"}]
tellraw @s [{"text":"🛒 ","color":"light_purple"},{"text":"[🎲🎲 10]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.dice set 31"}},{"text":" "},{"text":"[🎲🎲🎲 18]","color":"light_purple","click_event":{"action":"run_command","command":"trigger mg.dice set 32"}},{"text":" "},{"text":"[🔀 15]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.dice set 33"}},{"text":" "},{"text":"[partir]","color":"gray","click_event":{"action":"run_command","command":"trigger mg.dice set 39"}}]
dialog show @s mg:party_shop
execute at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1.5
