# Toutes les 5 s, @s : succès débloqués
execute if score @s mg.trkt matches 1.. run function mg:terra/rpg/ach/0
execute if score @s mg.trkt matches 50.. run function mg:terra/rpg/ach/1
execute if score @s mg.trkt matches 250.. run function mg:terra/rpg/ach/2
execute if score @s mg.trel matches 10.. run function mg:terra/rpg/ach/3
execute if score @s mg.trch matches 45.. run function mg:terra/rpg/ach/4
execute if score @s mg.trch matches 64.. run function mg:terra/rpg/ach/5
execute if score @s mg.trch matches 85.. run function mg:terra/rpg/ach/6
execute if score @s mg.trbs matches 8191 run function mg:terra/rpg/ach/7
execute if score @s mg.trdg matches 15 run function mg:terra/rpg/ach/8
execute if score @s mg.trtc matches 32767 run function mg:terra/rpg/ach/9
execute if score @s mg.trlv matches 20.. run function mg:terra/rpg/ach/10
execute if score @s mg.tvc matches 5000.. run function mg:terra/rpg/ach/11
