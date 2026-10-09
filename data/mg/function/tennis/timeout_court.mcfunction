# @s : marqueur d'un court pas fini
scoreboard players operation $tnk mg.st = @s mg.tnc
function mg:tennis/tagk
scoreboard players set $tnw mg.st 0
execute if score @s mg.tnp1 > @s mg.tnp2 run scoreboard players set $tnw mg.st 1
execute if score @s mg.tnp2 > @s mg.tnp1 run scoreboard players set $tnw mg.st 2
execute if score @s mg.tng1 > @s mg.tng2 run scoreboard players set $tnw mg.st 1
execute if score @s mg.tng2 > @s mg.tng1 run scoreboard players set $tnw mg.st 2
execute if score $tnw mg.st matches 1..2 run function mg:tennis/court_win
function mg:tennis/court_end
