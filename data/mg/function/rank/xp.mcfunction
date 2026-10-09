# @s (au lobby) : barre d'XP = niveau général, remplie selon la progression vers le suivant
scoreboard players operation $rp mg.st = @s mg.lvl
scoreboard players operation $rq mg.st = @s mg.lvl
scoreboard players add $rq mg.st 1
scoreboard players operation $rp mg.st *= $rq mg.st
scoreboard players operation $rp mg.st *= #25 mg.st
scoreboard players operation $rd mg.st = @s mg.gen
scoreboard players operation $rd mg.st -= $rp mg.st
scoreboard players operation $rq mg.st *= #50 mg.st
scoreboard players operation $rc mg.st = @s mg.lvl
scoreboard players operation $rc mg.st *= #2 mg.st
scoreboard players add $rc mg.st 7
execute if score @s mg.lvl matches 16..30 run scoreboard players operation $rc mg.st = @s mg.lvl
scoreboard players set #5 mg.st 5
scoreboard players set #9 mg.st 9
execute if score @s mg.lvl matches 16..30 run scoreboard players operation $rc mg.st *= #5 mg.st
execute if score @s mg.lvl matches 16..30 run scoreboard players remove $rc mg.st 38
execute if score @s mg.lvl matches 31.. run scoreboard players operation $rc mg.st = @s mg.lvl
execute if score @s mg.lvl matches 31.. run scoreboard players operation $rc mg.st *= #9 mg.st
execute if score @s mg.lvl matches 31.. run scoreboard players remove $rc mg.st 158
scoreboard players operation $rd mg.st *= $rc mg.st
scoreboard players operation $rd mg.st /= $rq mg.st
execute if score $rd mg.st >= $rc mg.st run scoreboard players operation $rd mg.st = $rc mg.st
execute if score $rd mg.st >= $rc mg.st run scoreboard players remove $rd mg.st 1
execute store result storage mg:rank x.l int 1 run scoreboard players get @s mg.lvl
execute store result storage mg:rank x.p int 1 run scoreboard players get $rd mg.st
function mg:rank/xp_set with storage mg:rank x
tag @s add mg.xpok
