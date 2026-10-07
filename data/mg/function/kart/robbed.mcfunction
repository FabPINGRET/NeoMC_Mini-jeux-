scoreboard players set @s mg.kit 0
scoreboard players set @s mg.kic 0
scoreboard players operation $me mg.st = @s mg.ri
execute as @e[type=minecraft:item_display,tag=mg.korb] if score @s mg.ri = $me mg.st run kill @s
clear @s minecraft:warped_fungus_on_a_stick
title @s actionbar [{"text":"👻 Boo t'a volé ton objet !","color":"white"}]
