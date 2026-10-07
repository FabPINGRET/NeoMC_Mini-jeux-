# Choix du kart de @s (/trigger mg.kch : 1..4 = modèle, 11..18 = couleur, 19 = couleur auto, 20 = valider, 30 = fenêtre des modèles)
execute if score @s mg.kch matches 30 run function mg:kart/show_models
execute if score @s mg.kch matches 30 run return run function mg:kart/choose_end
execute if score @s mg.kch matches 1..4 run scoreboard players operation @s mg.kty = @s mg.kch
execute if score @s mg.kch matches 11..18 run scoreboard players operation @s mg.kcol = @s mg.kch
execute if score @s mg.kch matches 11..18 run scoreboard players remove @s mg.kcol 10
execute if score @s mg.kch matches 19 run scoreboard players set @s mg.kcol 0
execute if score @s mg.kch matches 19..20 run tag @s add mg.kok
execute if score @s mg.kch matches 11..18 run function mg:kart/show_colors
execute if score @s mg.kch matches 19..20 run title @s actionbar [{"text":"✔ Prêt ! ","color":"green","bold":true},{"text":"En attente des autres pilotes...","color":"gray"}]
execute if score @s mg.kch matches 1..4 run function mg:kart/show_colors
execute if score @s mg.kch matches 1 run title @s actionbar [{"text":"🏎 Kart ","color":"gray"},{"text":"Standard","color":"white","bold":true},{"text":" : Équilibré en tout.","color":"gray"}]
execute if score @s mg.kch matches 2 run title @s actionbar [{"text":"🏎 Kart ","color":"gray"},{"text":"Bolide","color":"red","bold":true},{"text":" : Vitesse max +10 %, mais accélère et tourne moins bien.","color":"gray"}]
execute if score @s mg.kch matches 3 run title @s actionbar [{"text":"🏎 Kart ","color":"gray"},{"text":"Mini","color":"green","bold":true},{"text":" : Accélère fort et tourne serré, vitesse max -7 %, moins freiné dans l'herbe.","color":"gray"}]
execute if score @s mg.kch matches 4 run title @s actionbar [{"text":"🏎 Kart ","color":"gray"},{"text":"Costaud","color":"gold","bold":true},{"text":" : Vitesse max +4 %, accélère lentement, peu freiné hors piste, tête-à-queue plus courts.","color":"gray"}]
function mg:kart/kk
scoreboard players operation @e[type=minecraft:block_display,tag=mg.kk,limit=1] mg.kty = @s mg.kty
execute if score @s mg.kcol matches 1..8 run scoreboard players operation @e[type=minecraft:block_display,tag=mg.kk,limit=1] mg.kcol = @s mg.kcol
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s run function mg:kart/kart_paint
execute if score $kbat mg.st matches 1 run function mg:kart/bat_balloons
tag @e[tag=mg.kk] remove mg.kk
execute at @s run playsound minecraft:ui.button.click master @s ~ ~ ~ 0.6 1.2
function mg:kart/choose_end
