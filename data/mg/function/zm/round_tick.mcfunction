# Manche en cours : apparitions, fin de manche
scoreboard players add $zsc mg.st 1
execute store result score $zal mg.st if entity @e[type=minecraft:zombie,tag=mg.zz]
execute if score $zsc mg.st >= $zsj mg.st if score $zleft mg.st matches 1.. if score $zal mg.st matches ..23 run function mg:zm/spawn
execute if score $zleft mg.st matches ..0 if score $zal mg.st matches 0 run function mg:zm/round_end
