# Court $tnk : tag mg.tnk sur ses entités et ses joueurs, $tncx = x de son centre (×1000)
tag @e[tag=mg.tnk] remove mg.tnk
execute as @e[tag=mg.tent] if score @s mg.tnc = $tnk mg.st run tag @s add mg.tnk
execute as @a[tag=mg.play] if score @s mg.tnc = $tnk mg.st run tag @s add mg.tnk
scoreboard players operation $tncx mg.st = $tnk mg.st
scoreboard players operation $tncx mg.st *= #tn40000 mg.st
scoreboard players remove $tncx mg.st 99500
