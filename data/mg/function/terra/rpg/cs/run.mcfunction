# @s (en cinématique) : tick suivant, image clé, verrouillage de la caméra
scoreboard players add @s mg.trct 1
scoreboard players operation $own mg.st = @s mg.tvpid
tag @s add mg.trcsme
execute if score @s mg.trcs matches 1 run function mg:terra/rpg/cs/intro/t
execute if score @s mg.trcs matches 6 run function mg:terra/rpg/cs/boss_spino/t
execute if score @s mg.trcs matches 8 run function mg:terra/rpg/cs/boss_varek/t
execute if score @s mg.trcs matches 7 run function mg:terra/rpg/cs/boss_rex/t
execute if score @s mg.trcs matches 9 run function mg:terra/rpg/cs/rift/t
execute if score @s mg.trcs matches 10 run function mg:terra/rpg/cs/finale/t
execute if score @s mg.trcs matches 2 run function mg:terra/rpg/cs/pass_n/t
execute if score @s mg.trcs matches 5 run function mg:terra/rpg/cs/pass_s/t
execute if score @s mg.trcs matches 3 run function mg:terra/rpg/cs/pass_e/t
execute if score @s mg.trcs matches 4 run function mg:terra/rpg/cs/pass_w/t
tag @s remove mg.trcsme
