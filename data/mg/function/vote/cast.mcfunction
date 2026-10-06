# @s = joueur ayant utilisé /trigger mg.vote
execute if score @s mg.vote matches 1..20 run function mg:vote/choose
execute if score @s mg.vote matches 98 run function mg:vote/show
execute if score @s mg.vote matches 99 run function mg:vote/unvote
scoreboard players reset @s mg.vote
