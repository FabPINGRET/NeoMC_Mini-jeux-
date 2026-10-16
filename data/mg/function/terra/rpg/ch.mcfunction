# @s passe à l'étape $(n) de la campagne
$scoreboard players set @s mg.trch $(n)
scoreboard players set @s mg.trqp 0
execute if score @s mg.trch matches 30 run function mg:terra/rpg/cs/pass_n
execute if score @s mg.trch matches 50 run function mg:terra/rpg/cs/pass_e
execute if score @s mg.trch matches 60 run function mg:terra/rpg/cs/pass_w
execute if score @s mg.trch matches 72 run function mg:terra/rpg/cs/pass_s
function mg:terra/rpg/obj_say
function mg:terra/rpg/qloc
execute at @s run playsound minecraft:block.note_block.bell player @s ~ ~ ~ 0.8 0.9
