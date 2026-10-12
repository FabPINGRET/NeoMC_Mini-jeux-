# @s : piédestal cliqué (mg.st = n° du chapeau, 0 = sans chapeau)
scoreboard players operation $hn mg.st = @s mg.st
execute if data entity @s interaction on target run function mg:hat/pick
execute if data entity @s attack on attacker run function mg:hat/pick
data remove entity @s interaction
data remove entity @s attack
