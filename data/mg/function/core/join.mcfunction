# Initialisation d'un joueur (@s = le joueur)

tag @s add mg.init
team leave @s
gamemode adventure @s
spawnpoint @s 0 64 0
tp @s 0.5 64 0.5 facing 0.5 64 8.5
effect clear @s
effect give @s minecraft:saturation infinite 0 true
function mg:core/give_menu

tellraw @s [{"text":"\n✦ Bienvenue dans les MINI-JEUX ! ✦","color":"gold","bold":true}]
execute if entity @s[tag=mg.admin] run tellraw @s [{"text":"Tu es admin : clic droit sur ","color":"gray"},{"text":"≡ MENU","color":"gold"},{"text":" pour lancer un jeu (ou ","color":"gray"},{"text":"/trigger mg.menu","color":"yellow"},{"text":").","color":"gray"},{"text":" [ouvrir le menu]","color":"green","click_event":{"action":"run_command","command":"trigger mg.menu"},"hover_event":{"action":"show_text","value":"Ouvrir le menu des mini-jeux"}}]
execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"Un admin lance les jeux — tu seras téléporté automatiquement. ","color":"gray"},{"text":"Vote pour le prochain jeu : clic droit sur ☑ VOTE ","color":"green"},{"text":"[voter]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.menu"},"hover_event":{"action":"show_text","value":"Ouvrir le vote"}},{"text":" — spectateur : ","color":"gray"},{"text":"/trigger mg.opt set 1","color":"yellow"}]
tellraw @s [{"text":"Chacun a son plot de construction autour du spawn : ","color":"gray"},{"text":"[aller sur mon plot]","color":"green","click_event":{"action":"run_command","command":"trigger mg.pl set 1"},"hover_event":{"action":"show_text","value":"/trigger mg.pl set 1"}}]
execute at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.8 1.2
