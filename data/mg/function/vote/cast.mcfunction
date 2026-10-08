# @s = joueur ayant utilisé /trigger mg.vote
execute if score @s mg.vote matches 1..21 run function mg:vote/choose
execute if score @s mg.vote matches 90 run function mg:vote/pvp_open
execute if score @s mg.vote matches 97 run function mg:vote/open
execute if score @s mg.vote matches 98 run function mg:vote/show
execute if score @s mg.vote matches 99 run function mg:vote/unvote
scoreboard players reset @s mg.vote
