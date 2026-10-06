# @s = joueur : progression en % (tours * 10 + points de passage) sur 30
scoreboard players operation @s mg.rp = @s mg.lp
scoreboard players operation @s mg.rp *= $rc1 mg.st
scoreboard players operation @s mg.rp += @s mg.cp
scoreboard players operation @s mg.rp *= $rc2 mg.st
scoreboard players operation @s mg.rp /= $rc3 mg.st
