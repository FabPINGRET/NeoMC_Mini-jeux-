# @s : marqueur — nouveau point (balle retirée, joueurs replacés, service au serveur mg.tnl)
kill @e[type=minecraft:item_display,tag=mg.tnball,tag=mg.tnk]
scoreboard players set @s mg.tnph 0
scoreboard players set @s mg.tnt 0
tag @e[tag=mg.tnk] remove mg.tnsrv
scoreboard players operation $tnside mg.st = @s mg.tnl
execute as @e[tag=mg.tnk] if score @s mg.tns = $tnside mg.st run tag @s add mg.tnsrv
tag @e[type=minecraft:mannequin,tag=mg.tnrob,tag=mg.tnk] remove mg.tnchase
tag @e[type=minecraft:mannequin,tag=mg.tnrob,tag=mg.tnk] remove mg.tnmiss
scoreboard players operation $tnpar mg.st = @s mg.tnp1
scoreboard players operation $tnpar mg.st += @s mg.tnp2
scoreboard players operation $tnpar mg.st %= #tn2 mg.st
function mg:tennis/place
