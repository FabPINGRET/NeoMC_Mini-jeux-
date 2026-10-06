# Boutique (@s) : arrêt du déplacement, fenêtre d'achat (15 s)
scoreboard players operation $tmp mg.st = @s mg.mid
scoreboard players operation $tmp mg.st += @s mg.mit
scoreboard players operation $tmp mg.st += @s mg.mip
execute if score $tmp mg.st matches 3.. run tellraw @s [{"text":"🛒 Boutique : ton sac est plein (3 objets).","color":"gray"}]
execute if score $tmp mg.st matches 3.. run return run function mg:party/shop_close
scoreboard players set $mph mg.st 8
scoreboard players set $mpw mg.st 300
title @s title [{"text":"🛒 BOUTIQUE","color":"light_purple","bold":true}]
title @s subtitle [{"text":"Choisis un objet","color":"yellow"}]
tellraw @s [{"text":"🛒 Tu as ","color":"light_purple"},{"score":{"name":"@s","objective":"mg.mpm"},"color":"gold","bold":true},{"text":" pièces.  ","color":"light_purple"},{"text":"[🎲🎲 10]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.dice set 31"},"hover_event":{"action":"show_text","value":"Dé double"}},{"text":" ","color":"gray"},{"text":"[🎲🎲🎲 18]","color":"light_purple","click_event":{"action":"run_command","command":"trigger mg.dice set 32"},"hover_event":{"action":"show_text","value":"Dé triple"}},{"text":" ","color":"gray"},{"text":"[🔀 15]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.dice set 33"},"hover_event":{"action":"show_text","value":"Tuyau"}},{"text":" ","color":"gray"},{"text":"[partir]","color":"gray","click_event":{"action":"run_command","command":"trigger mg.dice set 39"},"hover_event":{"action":"show_text","value":"Reprendre la route"}}]
function mg:party/hud_bar
dialog show @s mg:party_shop
execute at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1.5
