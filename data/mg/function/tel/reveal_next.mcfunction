scoreboard players set $tt mg.st 0
scoreboard players add $rs mg.st 1
execute if score $rs mg.st matches 5.. run scoreboard players add $rc mg.st 1
execute if score $rs mg.st matches 5.. run scoreboard players set $rs mg.st 0
execute if score $rc mg.st >= $tn mg.st run return run function mg:tel/finish
scoreboard players operation $ra mg.st = $rc mg.st
scoreboard players operation $ra mg.st -= $rs mg.st
scoreboard players operation $ra mg.st += $tn mg.st
scoreboard players operation $ra mg.st %= $tn mg.st
scoreboard players operation $rb mg.st = $ra mg.st
scoreboard players operation $rb mg.st += $tn mg.st
scoreboard players remove $rb mg.st 1
scoreboard players operation $rb mg.st %= $tn mg.st
execute store result storage mg:tel r.c int 1 run scoreboard players get $rc mg.st
scoreboard players operation $rcn mg.st = $rc mg.st
scoreboard players add $rcn mg.st 1
execute store result storage mg:tel r.n int 1 run scoreboard players get $rc mg.st
execute store result storage mg:tel r.a int 1 run scoreboard players get $ra mg.st
execute store result storage mg:tel r.b int 1 run scoreboard players get $rb mg.st
scoreboard players set #64 mg.st 64
scoreboard players operation $rx mg.st = $rc mg.st
scoreboard players operation $rx mg.st *= #64 mg.st
scoreboard players remove $rx mg.st 352
execute store result storage mg:tel r.x int 1 run scoreboard players get $rx mg.st
execute if score $rs mg.st matches 0 run scoreboard players set $tlim mg.st 100
execute if score $rs mg.st matches 1 run scoreboard players set $tlim mg.st 200
execute if score $rs mg.st matches 2 run scoreboard players set $tlim mg.st 100
execute if score $rs mg.st matches 3 run scoreboard players set $tlim mg.st 200
execute if score $rs mg.st matches 4 run scoreboard players set $tlim mg.st 140
function mg:tel/reveal_show with storage mg:tel r
