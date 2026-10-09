# @s : balle lancée au sommet de sa course — frappe automatique du service (visée du serveur)
scoreboard players operation $tnside mg.st = @s mg.tnl
scoreboard players operation $tnbx mg.st = @s mg.tnx
scoreboard players operation $tnbz mg.st = @s mg.tnz
scoreboard players set $tnT mg.st 30
scoreboard players set $tndepth mg.st 8500
scoreboard players operation $tnlx mg.st = $tnbx mg.st
function mg:tennis/lz
execute as @a[tag=mg.tnk] if score @s mg.tns = $tnside mg.st run function mg:tennis/aim_target
execute as @e[type=minecraft:mannequin,tag=mg.tnrob,tag=mg.tnk] if score @s mg.tns = $tnside mg.st run function mg:tennis/robot_pick
function mg:tennis/shoot
scoreboard players set @e[type=minecraft:marker,tag=mg.tncm,tag=mg.tnk,limit=1] mg.tnph 2
