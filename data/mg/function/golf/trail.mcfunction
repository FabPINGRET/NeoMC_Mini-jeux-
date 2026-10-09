# Trace de particules (couleur du joueur)
scoreboard players operation $gfcol mg.st = @s mg.gfi
scoreboard players operation $gfcol mg.st %= #gf8 mg.st
execute if score $gfcol mg.st matches 0 run particle minecraft:dust{color:[1.0,1.0,1.0],scale:1.2} ~ ~0.15 ~ 0 0 0 0 1 force @a[tag=!mg.surv]
execute if score $gfcol mg.st matches 1 run particle minecraft:dust{color:[1.0,0.33,0.33],scale:1.2} ~ ~0.15 ~ 0 0 0 0 1 force @a[tag=!mg.surv]
execute if score $gfcol mg.st matches 2 run particle minecraft:dust{color:[0.33,0.33,1.0],scale:1.2} ~ ~0.15 ~ 0 0 0 0 1 force @a[tag=!mg.surv]
execute if score $gfcol mg.st matches 3 run particle minecraft:dust{color:[0.33,1.0,0.33],scale:1.2} ~ ~0.15 ~ 0 0 0 0 1 force @a[tag=!mg.surv]
execute if score $gfcol mg.st matches 4 run particle minecraft:dust{color:[1.0,1.0,0.33],scale:1.2} ~ ~0.15 ~ 0 0 0 0 1 force @a[tag=!mg.surv]
execute if score $gfcol mg.st matches 5 run particle minecraft:dust{color:[1.0,0.33,1.0],scale:1.2} ~ ~0.15 ~ 0 0 0 0 1 force @a[tag=!mg.surv]
execute if score $gfcol mg.st matches 6 run particle minecraft:dust{color:[0.33,1.0,1.0],scale:1.2} ~ ~0.15 ~ 0 0 0 0 1 force @a[tag=!mg.surv]
execute if score $gfcol mg.st matches 7 run particle minecraft:dust{color:[1.0,0.67,0.0],scale:1.2} ~ ~0.15 ~ 0 0 0 0 1 force @a[tag=!mg.surv]
