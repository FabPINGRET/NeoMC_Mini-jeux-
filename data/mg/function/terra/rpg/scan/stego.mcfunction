# @s scanne : Stégosaure
scoreboard players operation $b mg.st = @s mg.trbs
scoreboard players operation $b mg.st /= #p6 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return run title @s actionbar [{"text":"🔬 Stégosaure","color":"aqua"},{"text":" : déjà au bestiaire","color":"gray"}]
scoreboard players set @s mg.tval 60
scoreboard players operation @s mg.trbs += #p6 mg.st
title @s actionbar [{"text":"🔬 Nouvelle espèce : ","color":"aqua","bold":true},{"text":"Stégosaure","color":"yellow","bold":true}]
tellraw @s [{"text":"📖 ","color":"aqua"},{"text":"Stégosaure","color":"yellow","bold":true},{"text":" — Les pointes de sa queue fauchent quiconque s'approche de trop près.","color":"gray"}]
execute at @s run playsound minecraft:entity.villager.work_cartographer player @s ~ ~ ~ 0.8 1.4
function mg:terra/rpg/xp {n:40}
execute if score @s mg.trcl matches 3 run function mg:terra/rpg/xp {n:20}
execute if score @s mg.trch matches 25 run scoreboard players add @s mg.trqp 1
execute if score @s mg.trch matches 25 if score @s mg.trqp matches 2.. run function mg:terra/rpg/ch {n:28}
execute if score @s mg.trch matches 55 run function mg:terra/rpg/herd_chk
execute if score @s mg.trbs matches 8191 run function mg:terra/rpg/best_done
