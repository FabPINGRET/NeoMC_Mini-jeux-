# Passe à la construction suivante (ou aux résultats)
scoreboard players add $bbk mg.st 1
execute if score $bbk mg.st >= $bbn mg.st run return run function mg:bb/results
scoreboard players set $bbow mg.st 0
execute as @a[tag=mg.play] if score @s mg.bi = $bbk mg.st run scoreboard players set $bbow mg.st 1
execute if score $bbow mg.st matches 0 run return run function mg:bb/vote_next
scoreboard players set $bbt mg.st 0
scoreboard players set $bbcs mg.st 0
scoreboard players set $bbcv mg.st 0
scoreboard players set @a[tag=mg.play] mg.br 0
scoreboard players operation $bbd mg.st = $bbk mg.st
scoreboard players add $bbd mg.st 1
function mg:bb/vote_view
title @a[tag=mg.play] title [{"text":"Construction n°","color":"gold"},{"score":{"name":"$bbd","objective":"mg.st"},"color":"yellow","bold":true}]
title @a[tag=mg.play] subtitle [{"text":"Thème : ","color":"gray"},{"nbt":"word","storage":"mg:bb","color":"white"}]
execute as @a[tag=mg.play] unless score @s mg.bi = $bbk mg.st run function mg:bb/rate_chat
execute if score $bbs mg.st matches 1 as @a[tag=mg.play] run function mg:bb/rate_chat
execute as @a[tag=mg.play] if score @s mg.bi = $bbk mg.st unless score $bbs mg.st matches 1 run tellraw @s [{"text":"★ C'est ta construction ! Tu ne la notes pas.","color":"gold"}]
execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1.3
