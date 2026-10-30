# @s est dans mg:floaty sans y être inscrit : lobby (sauf partie en cours : ses tags de partie priment)
execute unless entity @s[tag=mg.play] unless entity @s[tag=mg.out] in minecraft:overworld run function mg:core/reset_player
