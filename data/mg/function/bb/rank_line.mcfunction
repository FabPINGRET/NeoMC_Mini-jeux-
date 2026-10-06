# @s = constructeur à afficher (rang $bbrk)
tag @s add mg.brk
scoreboard players add $bbrt mg.st 1
scoreboard players operation $bbt1 mg.st = @s mg.ba
scoreboard players operation $bbt1 mg.st /= $bbc100 mg.st
scoreboard players operation $bbt2 mg.st = @s mg.ba
scoreboard players operation $bbt2 mg.st %= $bbc100 mg.st
scoreboard players operation $bbt2 mg.st /= $bbc10 mg.st
execute if score $bbrk mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":" ★ 1er : ","color":"gold","bold":true},{"selector":"@s","color":"yellow","bold":true},{"text":" — ","color":"gray"},{"score":{"name":"$bbt1","objective":"mg.st"},"color":"gold","bold":true},{"text":".","color":"gold","bold":true},{"score":{"name":"$bbt2","objective":"mg.st"},"color":"gold","bold":true},{"text":"/5","color":"gray"}]
execute unless score $bbrk mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":" #","color":"gray"},{"score":{"name":"$bbrk","objective":"mg.st"},"color":"gray"},{"text":" ","color":"gray"},{"selector":"@s","color":"white"},{"text":" — ","color":"gray"},{"score":{"name":"$bbt1","objective":"mg.st"},"color":"white"},{"text":".","color":"white"},{"score":{"name":"$bbt2","objective":"mg.st"},"color":"white"},{"text":"/5","color":"gray"}]
