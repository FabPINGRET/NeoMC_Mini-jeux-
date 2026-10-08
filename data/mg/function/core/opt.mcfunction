# Options du menu (@s = joueur, mg.opt = valeur)
execute if score @s mg.opt matches 7..8 unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Menus de lancement réservés aux admins. ","color":"red"},{"text":"Vote plutôt pour un jeu : fenêtre ☑ VOTES ou /trigger mg.vote","color":"gray"}]
execute if score @s mg.opt matches 10 unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Menus de lancement réservés aux admins. ","color":"red"},{"text":"Vote plutôt pour un jeu : fenêtre ☑ VOTES ou /trigger mg.vote","color":"gray"}]
execute if score @s mg.opt matches 14 unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Menus de lancement réservés aux admins. ","color":"red"},{"text":"Vote plutôt pour un jeu : fenêtre ☑ VOTES ou /trigger mg.vote","color":"gray"}]
execute if score @s mg.opt matches 29..31 unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Menus de lancement réservés aux admins. ","color":"red"},{"text":"Vote plutôt pour un jeu : fenêtre ☑ VOTES ou /trigger mg.vote","color":"gray"}]
execute if score @s mg.opt matches 16..24 unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Menus de lancement réservés aux admins. ","color":"red"},{"text":"Vote plutôt pour un jeu : fenêtre ☑ VOTES ou /trigger mg.vote","color":"gray"}]
execute if score @s mg.opt matches 28 unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Menus de lancement réservés aux admins. ","color":"red"},{"text":"Vote plutôt pour un jeu : fenêtre ☑ VOTES ou /trigger mg.vote","color":"gray"}]
execute if score @s mg.opt matches 32..43 unless entity @s[tag=mg.admin] run tellraw @s {"text":"⚠ Menus de lancement réservés aux admins : vote plutôt (≡ → ☑ Votes).","color":"red"}
execute if score @s mg.opt matches 32..43 if entity @s[tag=mg.admin] run function mg:var/menu/open
execute if score @s mg.opt matches 44..45 unless entity @s[tag=mg.admin] run function mg:var/menu/open
execute if score @s mg.opt matches 46..47 unless entity @s[tag=mg.admin] run tellraw @s {"text":"⚠ Menus de lancement réservés aux admins : vote plutôt (≡ → ☑ Votes).","color":"red"}
execute if score @s mg.opt matches 44..47 if entity @s[tag=mg.admin] run function mg:var/menu/open
execute if score @s mg.opt matches 1 run function mg:core/opt_spec
execute if score @s mg.opt matches 2 run function mg:core/opt_sidebar
execute if score @s mg.opt matches 11 run function mg:parkour/quit
execute if score @s mg.opt matches 25 run function mg:core/stats
execute if score @s mg.opt matches 27 run function mg:lobkart/exit
execute if score @s mg.opt matches 26 if entity @s[tag=mg.play] if score $game mg.st matches 61 run tag @s add mg.kstuck
execute if score @s mg.opt matches 26 if entity @s[tag=mg.lk] run tag @s add mg.kstuck
execute if score @s mg.opt matches 7 if entity @s[tag=mg.admin] run function mg:core/menu_mob
execute if score @s mg.opt matches 8 if entity @s[tag=mg.admin] run function mg:core/menu_sheep
execute if score @s mg.opt matches 16 if entity @s[tag=mg.admin] run function mg:core/sub/party
execute if score @s mg.opt matches 17 if entity @s[tag=mg.admin] run function mg:core/sub/splegg
execute if score @s mg.opt matches 18 if entity @s[tag=mg.admin] run function mg:core/sub/sumo
execute if score @s mg.opt matches 19 if entity @s[tag=mg.admin] run function mg:core/sub/dropper
execute if score @s mg.opt matches 20 if entity @s[tag=mg.admin] run function mg:core/sub/anvil
execute if score @s mg.opt matches 21 if entity @s[tag=mg.admin] run function mg:core/sub/paint
execute if score @s mg.opt matches 22 if entity @s[tag=mg.admin] run function mg:core/sub/bb
execute if score @s mg.opt matches 23 if entity @s[tag=mg.admin] run function mg:core/sub/pvparena
execute if score @s mg.opt matches 24 if entity @s[tag=mg.admin] run function mg:core/sub/oitc
execute if score @s mg.opt matches 28 if entity @s[tag=mg.admin] run function mg:core/sub/elyrace
execute if score @s mg.opt matches 29 if entity @s[tag=mg.admin] run function mg:core/sub/tnttag
execute if score @s mg.opt matches 30 if entity @s[tag=mg.admin] run function mg:core/sub/bedwars
execute if score @s mg.opt matches 31 if entity @s[tag=mg.admin] run function mg:core/sub/elytra
execute if score @s mg.opt matches 14 if entity @s[tag=mg.admin] run function mg:core/menu_pvp
execute if score @s mg.opt matches 10 if entity @s[tag=mg.admin] run function mg:core/menu_quake
execute if score @s mg.opt matches 9 unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Seul un admin peut arrêter la partie.","color":"red"}]
execute if score @s mg.opt matches 9 if entity @s[tag=mg.admin] if score $state mg.st matches 1..2 run function mg:core/abort
execute if score @s mg.opt matches 12 unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Seul un admin peut lancer le jeu le plus voté.","color":"red"}]
execute if score @s mg.opt matches 12 if entity @s[tag=mg.admin] run function mg:vote/launch
execute if score @s mg.opt matches 13 if entity @s[tag=mg.admin] run function mg:vote/reset
scoreboard players reset @s mg.opt
