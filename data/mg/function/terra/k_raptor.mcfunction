# @s a abattu mg.tvkr slasher(s) : 12 ₵ chacun, progression de la chasse
function mg:terra/rpg/k_raptor
scoreboard players operation $tvk2 mg.st = @s mg.tvkr
scoreboard players operation $tvk2 mg.st *= #12 mg.st
scoreboard players operation @s mg.tvc += $tvk2 mg.st
scoreboard players set @s mg.tval 30
title @s actionbar [{"text":"+","color":"green","bold":true},{"score":{"name":"$tvk2","objective":"mg.st"},"color":"green","bold":true},{"text":" ₵ ","color":"green","bold":true},{"text":"slasher abattu","color":"gray"}]
execute if score @s mg.tvm matches 3 run scoreboard players operation @s mg.tvmp += @s mg.tvkr
execute if score @s mg.tvm matches 3 if score @s mg.tvmp matches ..4 run tellraw @s [{"text":"🦖 Chasse : ","color":"green"},{"score":{"name":"@s","objective":"mg.tvmp"},"color":"yellow","bold":true},{"text":" / 5","color":"yellow"}]
scoreboard players set @s mg.tvkr 0
execute if score @s mg.tvm matches 3 if score @s mg.tvmp matches 5.. run function mg:terra/m3_done
