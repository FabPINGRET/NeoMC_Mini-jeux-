# Départ
execute as @a[tag=mg.play] run function mg:convoy/kit
scoreboard players set @a mg.deaths 0
scoreboard players set $cvw mg.st 0
execute if score $cvm mg.st matches 0 run function mg:convoy/round_msg
execute if score $cvm mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":"🚚 CONVOI (coop) : ","color":"gold","bold":true},{"text":"restez près du convoi pour le faire avancer, les monstres le bloquent et l'abîment. Amenez-le aux blocs d'or avant 6 min !","color":"gray"}]
