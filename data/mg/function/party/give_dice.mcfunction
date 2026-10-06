# Donne le dé à @s (clic droit = lancer) + lien cliquable de secours
item replace entity @s hotbar.0 with minecraft:echo_shard[custom_name=[{"text":"🎲 DÉ : clic droit pour lancer","color":"gold","italic":false,"bold":true}],enchantment_glint_override=true,consumable={consume_seconds:0.05,animation:"none",sound:"minecraft:block.note_block.hat",has_consume_particles:false}]
title @s title [{"text":"À toi !","color":"gold","bold":true}]
title @s subtitle [{"text":"Clic droit avec le dé (case 1 de la barre)","color":"yellow"}]
tellraw @s [{"text":"🎲 ","color":"gold"},{"text":"[LANCER LE DÉ]","color":"green","bold":true,"click_event":{"action":"run_command","command":"trigger mg.dice"},"hover_event":{"action":"show_text","value":"Lancer le dé"}},{"text":" (lancé automatiquement dans 20 s)","color":"gray"}]
execute at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.2
