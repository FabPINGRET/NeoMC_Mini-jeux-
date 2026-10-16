# @s (étape 55) : a-t-il scanné tricératops, stégosaure et ankylosaure ?
scoreboard players set $hc mg.st 0
scoreboard players operation $b mg.st = @s mg.trbs
scoreboard players operation $b mg.st /= #p5 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
scoreboard players operation $hc mg.st += $b mg.st
scoreboard players operation $b mg.st = @s mg.trbs
scoreboard players operation $b mg.st /= #p6 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
scoreboard players operation $hc mg.st += $b mg.st
scoreboard players operation $b mg.st = @s mg.trbs
scoreboard players operation $b mg.st /= #p7 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
scoreboard players operation $hc mg.st += $b mg.st
execute if score $hc mg.st matches 3 run function mg:terra/rpg/ch {n:58}
