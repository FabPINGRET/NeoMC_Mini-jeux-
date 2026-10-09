# @s : annonce du lancer (#ev : 1 strike, 2 spare, 4 zéro) — titre, sons, particules
scoreboard players operation #ln mg.st = @s mg.bln
execute if score #ev mg.st matches 1 if score @s mg.bxs matches 3.. run return run function mg:bowl/fx_turkey
execute if score #ev mg.st matches 1 run return run function mg:bowl/fx_strike
execute if score #ev mg.st matches 2 run return run function mg:bowl/fx_spare
execute if score #ev mg.st matches 4 run title @s actionbar {"text":"🎳 Aucune quille…","color":"gray"}
execute if score #ev mg.st matches 4 run return run playsound minecraft:entity.villager.no master @s ~ ~ ~ 0.8 1
title @s actionbar [{"text":"🎳 ","color":"gray"},{"score":{"name":"#k","objective":"mg.st"},"color":"white","bold":true},{"text":" quille(s) — total ","color":"gray"},{"score":{"name":"@s","objective":"mg.bsc"},"color":"gold"}]
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.6 1
