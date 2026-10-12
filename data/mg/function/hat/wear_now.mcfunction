# @s : chapeau posé tout de suite si la tête est libre (sinon : présentoir au prochain tick)
execute unless items entity @s armor.head * run function mg:hat/wear
