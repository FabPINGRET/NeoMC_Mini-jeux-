# Attente du choix de route (trigger mg.dice 11 / 12), puis reprise du déplacement
scoreboard players remove $mpw mg.st 1
execute if entity @a[tag=mg.mpcur,scores={mg.dice=11}] run scoreboard players set $mpch mg.st 1
execute if entity @a[tag=mg.mpcur,scores={mg.dice=12}] run scoreboard players set $mpch mg.st 2
execute if score $mpch mg.st matches 0 if score $mpw mg.st matches ..0 store result score $mpch mg.st run random value 1..2
execute unless entity @a[tag=mg.mpcur] run scoreboard players set $mpch mg.st 1
execute if score $mpch mg.st matches 1..2 as @a[tag=mg.mpcur] run function mg:party/fork_msg
execute if score $mpch mg.st matches 1..2 run scoreboard players set $mpw mg.st 10
execute if score $mpch mg.st matches 1..2 run scoreboard players set $mph mg.st 3
