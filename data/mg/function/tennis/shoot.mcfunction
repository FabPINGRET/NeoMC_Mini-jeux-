# @s : balle — frappe par le côté $tnside vers ($tnlx, $tnlz) en $tnT ticks
scoreboard players operation @s mg.tnvx = $tnlx mg.st
scoreboard players operation @s mg.tnvx -= @s mg.tnx
scoreboard players operation @s mg.tnvx /= $tnT mg.st
scoreboard players operation @s mg.tnvz = $tnlz mg.st
scoreboard players operation @s mg.tnvz -= @s mg.tnz
scoreboard players operation @s mg.tnvz /= $tnT mg.st
scoreboard players set @s mg.tnvy 65100
scoreboard players operation @s mg.tnvy -= @s mg.tny
scoreboard players operation @s mg.tnvy /= $tnT mg.st
scoreboard players operation $tnq mg.st = $tnT mg.st
scoreboard players operation $tnq mg.st *= #tng mg.st
scoreboard players operation $tnq mg.st /= #tn2 mg.st
scoreboard players operation @s mg.tnvy += $tnq mg.st
scoreboard players set @s mg.tnb 0
scoreboard players operation @s mg.tnl = $tnside mg.st
tag @s remove mg.tntoss
tag @s add mg.tnlive
execute at @s run playsound minecraft:entity.player.attack.strong master @a[tag=!mg.surv,distance=..40] ~ ~ ~ 1 1.6
execute at @s run particle minecraft:crit ~ ~ ~ 0.1 0.1 0.1 0.2 6
scoreboard players operation $tnvx mg.st = @s mg.tnvx
scoreboard players operation $tnvz mg.st = @s mg.tnvz
execute as @e[type=minecraft:mannequin,tag=mg.tnrob,tag=mg.tnk] unless score @s mg.tns = $tnside mg.st run function mg:tennis/robot_aim
tag @e[type=minecraft:mannequin,tag=mg.tnrob,tag=mg.tnk] remove mg.tnchase
execute as @e[type=minecraft:mannequin,tag=mg.tnrob,tag=mg.tnk] unless score @s mg.tns = $tnside mg.st run tag @s add mg.tnchase
