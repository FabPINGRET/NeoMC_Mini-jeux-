# @s = constructeur de la parcelle $bbk : moyenne ×100 dans mg.ba
scoreboard players operation @s mg.ba = $bbcs mg.st
scoreboard players operation @s mg.ba *= $bbc100 mg.st
execute if score $bbcv mg.st matches 1.. run scoreboard players operation @s mg.ba /= $bbcv mg.st
execute unless score $bbcv mg.st matches 1.. run scoreboard players set @s mg.ba 0
scoreboard players operation $bbt1 mg.st = @s mg.ba
scoreboard players operation $bbt1 mg.st /= $bbc100 mg.st
scoreboard players operation $bbt2 mg.st = @s mg.ba
scoreboard players operation $bbt2 mg.st %= $bbc100 mg.st
scoreboard players operation $bbt2 mg.st /= $bbc10 mg.st
tellraw @a[tag=mg.play] [{"text":" ▸ Construction n°","color":"gray"},{"score":{"name":"$bbd","objective":"mg.st"},"color":"gray"},{"text":" : ","color":"gray"},{"score":{"name":"$bbt1","objective":"mg.st"},"color":"gold","bold":true},{"text":".","color":"gold","bold":true},{"score":{"name":"$bbt2","objective":"mg.st"},"color":"gold","bold":true},{"text":"/5 (","color":"gray"},{"score":{"name":"$bbcv","objective":"mg.st"},"color":"gray"},{"text":" notes)","color":"gray"}]
