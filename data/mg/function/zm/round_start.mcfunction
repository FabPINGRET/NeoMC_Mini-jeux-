# Nouvelle manche : nombre, vie et vitesse des zombies
scoreboard players add $zr mg.st 1
scoreboard players set $zph mg.st 1
scoreboard players set $zsc mg.st 0
scoreboard players operation $zleft mg.st = $zr mg.st
scoreboard players set #3 mg.st 3
scoreboard players operation $zleft mg.st *= #3 mg.st
scoreboard players add $zleft mg.st 4
execute store result score $zn mg.st if entity @a[tag=mg.play]
scoreboard players add $zn mg.st 1
scoreboard players operation $zleft mg.st *= $zn mg.st
scoreboard players operation $zleft mg.st /= #2 mg.st
execute if score $zleft mg.st matches 61.. run scoreboard players set $zleft mg.st 60
scoreboard players operation $zhp mg.st = $zr mg.st
scoreboard players set #8 mg.st 8
scoreboard players operation $zhp mg.st *= #8 mg.st
scoreboard players add $zhp mg.st 8
execute if score $zhp mg.st matches 151.. run scoreboard players set $zhp mg.st 150
scoreboard players set $zsp mg.st 23
execute if score $zr mg.st matches 4.. run scoreboard players set $zsp mg.st 27
execute if score $zr mg.st matches 7.. run scoreboard players set $zsp mg.st 32
scoreboard players operation $zsi mg.st = $zr mg.st
scoreboard players operation $zsi mg.st *= #2 mg.st
scoreboard players set $zsj mg.st 22
scoreboard players operation $zsj mg.st -= $zsi mg.st
execute if score $zsj mg.st matches ..7 run scoreboard players set $zsj mg.st 8
execute store result storage mg:zm hp int 1 run scoreboard players get $zhp mg.st
execute store result storage mg:zm sp double 0.01 run scoreboard players get $zsp mg.st
title @a[tag=mg.play] title [{"text":"Manche ","color":"dark_red","bold":true},{"score":{"name":"$zr","objective":"mg.st"},"color":"red","bold":true}]
title @a[tag=mg.play] subtitle [{"score":{"name":"$zleft","objective":"mg.st"},"color":"yellow"},{"text":" zombies","color":"gray"}]
execute as @a[tag=mg.play] at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.3 0.6
