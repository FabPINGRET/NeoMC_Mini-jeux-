# @s : guide en plus d'une paire au hasard
tag @s add mg.lbx
tag @s add mg.lbg
execute store result score @s mg.lbp run random value 0..999
scoreboard players operation @s mg.lbp %= $lbn mg.st
scoreboard players add @s mg.lbp 1
