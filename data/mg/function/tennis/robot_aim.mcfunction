# @s : robot — la balle arrive ($tnlx/$tnlz impact, $tnvx/$tnvz vitesse) : il vise un peu après le rebond
scoreboard players operation $tnq mg.st = $tnvx mg.st
scoreboard players operation $tnq mg.st *= #tn3 mg.st
scoreboard players operation @s mg.tnx = $tnq mg.st
scoreboard players operation @s mg.tnx *= #tn2 mg.st
scoreboard players operation @s mg.tnx += $tnlx mg.st
scoreboard players operation $tnq mg.st = $tnvz mg.st
scoreboard players operation $tnq mg.st *= #tn3 mg.st
scoreboard players operation @s mg.tnz = $tnq mg.st
scoreboard players operation @s mg.tnz *= #tn2 mg.st
scoreboard players operation @s mg.tnz += $tnlz mg.st
execute store result score $tnq mg.st run random value -1000..1000
scoreboard players operation @s mg.tnx += $tnq mg.st
execute if score @s mg.tnx matches ..-9001 run scoreboard players set @s mg.tnx -9000
execute if score @s mg.tnx matches 9001.. run scoreboard players set @s mg.tnx 9000
execute if score @s mg.tns matches 2 if score @s mg.tnz matches ..3999 run scoreboard players set @s mg.tnz 4000
execute if score @s mg.tns matches 2 if score @s mg.tnz matches 17501.. run scoreboard players set @s mg.tnz 17500
execute if score @s mg.tns matches 1 if score @s mg.tnz matches -3999.. run scoreboard players set @s mg.tnz -4000
execute if score @s mg.tns matches 1 if score @s mg.tnz matches ..-17501 run scoreboard players set @s mg.tnz -17500
tag @s remove mg.tnmiss
execute store result score $tnq mg.st run random value 1..100
execute if score $tnq mg.st matches ..10 run tag @s add mg.tnmiss
