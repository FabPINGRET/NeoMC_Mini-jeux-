# @s = premier joueur à finir les 3 tours
scoreboard players set @s mg.rp 100
execute if score $state mg.st matches 2 run function mg:core/win_player
