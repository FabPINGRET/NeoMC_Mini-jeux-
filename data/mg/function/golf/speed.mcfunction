# $gfsp = |vx| + |vz| de @s
scoreboard players operation $gfsp mg.st = @s mg.gfu
execute if score $gfsp mg.st matches ..-1 run scoreboard players operation $gfsp mg.st *= #gfm1 mg.st
scoreboard players operation $gfs2 mg.st = @s mg.gfw
execute if score $gfs2 mg.st matches ..-1 run scoreboard players operation $gfs2 mg.st *= #gfm1 mg.st
scoreboard players operation $gfsp mg.st += $gfs2 mg.st
