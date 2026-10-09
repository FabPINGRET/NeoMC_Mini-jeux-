# @s : marqueur d'un court — score à zéro, premier serveur au hasard
scoreboard players operation $tnk mg.st = @s mg.tnc
function mg:tennis/tagk
scoreboard players set @s mg.tnp1 0
scoreboard players set @s mg.tnp2 0
scoreboard players set @s mg.tng1 0
scoreboard players set @s mg.tng2 0
execute store result score @s mg.tnl run random value 1..2
function mg:tennis/labels
function mg:tennis/point_setup
