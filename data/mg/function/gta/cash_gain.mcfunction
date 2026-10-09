# @s ramasse $gcv dollars
scoreboard players operation @s mg.gta += $gcv mg.st
scoreboard players set @s mg.gal 40
title @s actionbar [{"text":"+","color":"green","bold":true},{"score":{"name":"$gcv","objective":"mg.st"},"color":"green","bold":true},{"text":" $ ","color":"green","bold":true},{"text":"billets ramassés","color":"gray"}]
