# @s : joueur — point d'impact selon son regard horizontal (balle en $tnbx/$tnbz, profondeur $tndepth)
execute rotated as @s rotated ~ 0 positioned 0.0 64 35400.0 run tp @e[type=minecraft:marker,tag=mg.tndir,limit=1] ^ ^ ^1
execute store result score $tnax mg.st run data get entity @e[type=minecraft:marker,tag=mg.tndir,limit=1] Pos[0] 1000
execute store result score $tnaz mg.st run data get entity @e[type=minecraft:marker,tag=mg.tndir,limit=1] Pos[2] 1000
scoreboard players remove $tnaz mg.st 35400000
execute if score $tnside mg.st matches 2 run scoreboard players operation $tnaz mg.st *= #tnm1 mg.st
execute if score $tnaz mg.st matches ..599 run scoreboard players set $tnaz mg.st 600
execute if score $tnax mg.st matches ..-801 run scoreboard players set $tnax mg.st -800
execute if score $tnax mg.st matches 801.. run scoreboard players set $tnax mg.st 800
function mg:tennis/lz
scoreboard players operation $tnd mg.st = $tnlz mg.st
scoreboard players operation $tnd mg.st -= $tnbz mg.st
execute if score $tnside mg.st matches 2 run scoreboard players operation $tnd mg.st *= #tnm1 mg.st
scoreboard players operation $tnlx mg.st = $tnax mg.st
scoreboard players operation $tnlx mg.st *= $tnd mg.st
scoreboard players operation $tnlx mg.st /= $tnaz mg.st
scoreboard players operation $tnlx mg.st /= #tn2 mg.st
scoreboard players operation $tnlx mg.st += $tnbx mg.st
execute if score $tnlx mg.st matches ..-7501 run scoreboard players set $tnlx mg.st -7500
execute if score $tnlx mg.st matches 7501.. run scoreboard players set $tnlx mg.st 7500
