# Mini-jeu de la Mini Party en cours (core/game_tick) : filet de sécurité sur la durée
execute if score $game mg.st matches 59 run return 0
scoreboard players add $mpgt mg.st 1
execute if score $mplim mg.st matches 1.. if score $mpgt mg.st = $mplim mg.st run function mg:party/watch_end
