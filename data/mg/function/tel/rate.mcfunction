# @s note (1 à 5 ★) la construction qu'il devine → ch[mg.tc].v1 (étape 2) / v3 (étape 4)
execute unless score $tp mg.st matches 2 unless score $tp mg.st matches 4 run return run scoreboard players reset @s mg.tel
scoreboard players remove @s mg.tel 10
execute store result storage mg:tel p.c int 1 run scoreboard players get @s mg.tc
execute store result storage mg:tel p.v int 1 run scoreboard players get @s mg.tel
execute if score $tp mg.st matches 2 run data modify storage mg:tel p.k set value "v1"
execute if score $tp mg.st matches 4 run data modify storage mg:tel p.k set value "v3"
function mg:tel/rate_m with storage mg:tel p
title @s actionbar [{"text":"★ Note enregistrée : ","color":"gold"},{"score":{"name":"@s","objective":"mg.tel"},"color":"yellow","bold":true},{"text":"/5 (modifiable)","color":"gray"}]
execute at @s run playsound minecraft:ui.button.click master @s ~ ~ ~ 1 1.5
scoreboard players reset @s mg.tel
