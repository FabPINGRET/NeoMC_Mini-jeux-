# Mini-jeu de la Mini Party en cours (core/game_tick) : format court (limite de temps, mort subite au Bedwars)
execute if score $game mg.st matches 59 run return 0
scoreboard players add $mpgt mg.st 1
execute if score $game mg.st matches 4 if score $mpgt mg.st matches 2400 run tellraw @a[tag=!mg.surv] [{"text":"⚠ MORT SUBITE dans 30 s : ","color":"red","bold":true},{"text":"tous les lits vont être détruits !","color":"gray"}]
execute if score $game mg.st matches 4 if score $mpgt mg.st matches 3000 run function mg:party/bw_sudden
scoreboard players operation $mprest mg.st = $mplim mg.st
scoreboard players operation $mprest mg.st -= $mpgt mg.st
execute if score $mprest mg.st matches 1200 run tellraw @a[tag=!mg.surv] [{"text":"⏱ ","color":"gold"},{"text":"Plus qu’une minute pour ce mini-jeu !","color":"yellow"}]
execute if score $mplim mg.st matches 1.. if score $mpgt mg.st = $mplim mg.st run function mg:party/watch_end
