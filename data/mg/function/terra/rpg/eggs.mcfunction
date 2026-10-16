# @s : quête des œufs d'ambre (Dr Ossei)
scoreboard players set $n mg.st 0
scoreboard players operation $b mg.st = @s mg.treg
scoreboard players operation $b mg.st /= #p0 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
scoreboard players operation $n mg.st += $b mg.st
scoreboard players operation $b mg.st = @s mg.treg
scoreboard players operation $b mg.st /= #p1 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
scoreboard players operation $n mg.st += $b mg.st
scoreboard players operation $b mg.st = @s mg.treg
scoreboard players operation $b mg.st /= #p2 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
scoreboard players operation $n mg.st += $b mg.st
scoreboard players operation $b mg.st = @s mg.treg
scoreboard players operation $b mg.st /= #p3 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
scoreboard players operation $n mg.st += $b mg.st
scoreboard players operation $b mg.st = @s mg.treg
scoreboard players operation $b mg.st /= #p4 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
scoreboard players operation $n mg.st += $b mg.st
scoreboard players operation $b mg.st = @s mg.treg
scoreboard players operation $b mg.st /= #p5 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
scoreboard players operation $n mg.st += $b mg.st
tag @s add mg.tregq
execute if score @s mg.trmt matches 1.. run return run tellraw @s {"text":"🔬 « Ton raptor grandit bien, à ce que je vois ! »","color":"aqua"}
execute if score $n mg.st matches 6.. run return run function mg:terra/rpg/egg_reward
tellraw @s [{"text":"🥚 Œufs d'ambre : ","color":"gold"},{"score":{"name":"$n","objective":"mg.st"},"color":"yellow","bold":true},{"text":" / 6. Ils brillent (accroupi à côté pour le ramasser) : deux dans la vallée, un par région.","color":"gray"}]
