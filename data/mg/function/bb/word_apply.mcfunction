# Le thème est choisi (mg:bb word) → début de la construction
scoreboard players set $bbp mg.st 1
scoreboard players set $bbt mg.st 0
clear @a[tag=mg.bm] minecraft:writable_book
title @a[tag=mg.play] title [{"text":"✎ ","color":"gold"},{"nbt":"word","storage":"mg:bb","color":"yellow","bold":true}]
title @a[tag=mg.play] subtitle [{"text":"Construis-le en 4 minutes !","color":"gray"}]
tellraw @a[tag=mg.play] [{"text":"\n✎ THÈME : ","color":"gold","bold":true},{"nbt":"word","storage":"mg:bb","color":"yellow","bold":true}]
tellraw @a[tag=mg.play] [{"text":"Reste sur ta parcelle (25×25) : 4 minutes pour construire. Ensuite, chacun note les constructions des autres !","color":"gray"}]
gamemode creative @a[tag=mg.play,scores={mg.bi=0..}]
gamemode spectator @a[tag=mg.play,scores={mg.bi=-1}]
execute as @a[tag=mg.play] at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1
