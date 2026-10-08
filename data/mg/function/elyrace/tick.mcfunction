# Course d'élytres : tick de jeu
scoreboard players add $xt mg.st 1
execute unless score $xc mg.st matches 2.. as @e[type=player,tag=mg.play,scores={mg.xf=0}] run function mg:elyrace/c1/player
execute if score $xc mg.st matches 2 as @e[type=player,tag=mg.play,scores={mg.xf=0}] run function mg:elyrace/c2/player
scoreboard players operation $xm mg.st = $xt mg.st
scoreboard players operation $xm mg.st %= #k10 mg.st
execute if score $xm mg.st matches 0 as @a[tag=mg.play,scores={mg.xf=0}] run function mg:elyrace/hud
# Après le premier arrivé : les autres ont 20 s ; tous arrivés ou partis : fin immédiate
execute if score $xw mg.st matches 1 run scoreboard players remove $xe mg.st 1
execute if score $xw mg.st matches 1 if score $xe mg.st matches ..0 run return run function mg:elyrace/end
execute if score $xw mg.st matches 1 unless entity @a[tag=mg.play,scores={mg.xf=0}] run return run function mg:elyrace/end
execute if score $xt mg.st matches 3000 run tellraw @a[tag=mg.play] [{"text":"🪽 Plus que 30 secondes !","color":"gold"}]
execute if score $xt mg.st matches 3600.. run return run function mg:elyrace/timeout
execute unless entity @a[tag=mg.play] run function mg:core/draw
