# @s a validé une fenêtre du casino (mg.gcas)
scoreboard players operation $gcc mg.st = @s mg.gcas
scoreboard players reset @s mg.gcas
scoreboard players operation $gcm mg.st = $gcc mg.st
scoreboard players set #10 mg.st 10
scoreboard players operation $gcm mg.st %= #10 mg.st
scoreboard players set $gbet mg.st 0
execute if score $gcm mg.st matches 1 run scoreboard players set $gbet mg.st 10
execute if score $gcm mg.st matches 2 run scoreboard players set $gbet mg.st 50
execute if score $gcm mg.st matches 3 run scoreboard players set $gbet mg.st 100
execute if score $gcm mg.st matches 4 run scoreboard players set $gbet mg.st 500
execute if score $gcm mg.st matches 5 run scoreboard players set $gbet mg.st 1000
execute if score $gbet mg.st matches 0 run return 0
execute if entity @s[tag=mg.gslot] run return 0
execute if score @s mg.gta < $gbet mg.st run scoreboard players set @s mg.gal 40
execute if score @s mg.gta < $gbet mg.st run return run title @s actionbar [{"text":"💸 Pas assez d'argent pour miser ","color":"red"},{"score":{"name":"$gbet","objective":"mg.st"},"color":"gold"},{"text":" $","color":"red"}]
scoreboard players operation @s mg.gta -= $gbet mg.st
scoreboard players set @s mg.gal 60
title @s times 2 40 10
execute if score $gcc mg.st matches 11..15 run return run function mg:gta/cas_slot
execute if score $gcc mg.st matches 211..215 run return run function mg:gta/cas_roul {p:1}
execute if score $gcc mg.st matches 221..225 run return run function mg:gta/cas_roul {p:2}
execute if score $gcc mg.st matches 231..235 run return run function mg:gta/cas_roul {p:3}
execute if score $gcc mg.st matches 31..35 run return run function mg:gta/cas_dice
