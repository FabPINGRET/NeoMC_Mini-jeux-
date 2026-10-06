# Attente du lancer (objet dé, /trigger mg.dice, ou automatique au bout de 20 s)
scoreboard players remove $mpw mg.st 1
execute if entity @a[tag=mg.mpcur,scores={mg.dz=1..}] run scoreboard players set $mpw mg.st 0
execute if entity @a[tag=mg.mpcur,scores={mg.dice=1}] run scoreboard players set $mpw mg.st 0
execute if entity @a[tag=mg.mpcur,scores={mg.dice=29}] as @a[tag=mg.mpcur] run function mg:party/roll_dialog
execute if entity @a[tag=mg.mpcur,scores={mg.dice=21}] as @a[tag=mg.mpcur] run function mg:party/use_double
execute if entity @a[tag=mg.mpcur,scores={mg.dice=22}] as @a[tag=mg.mpcur] run function mg:party/use_triple
execute if entity @a[tag=mg.mpcur,scores={mg.dice=23}] as @a[tag=mg.mpcur] run function mg:party/use_pipe
execute if score $mpw mg.st matches 100 run tellraw @a[tag=mg.mpcur] [{"text":"Plus que 5 s avant le lancer automatique !","color":"red"}]
execute if score $mpw mg.st matches ..0 run function mg:party/roll_start
