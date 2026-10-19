# @s active l'objet $(b) de son étape
$execute store result score $m mg.st run function mg:ombre/q/pow2 {b:$(b)}
scoreboard players operation $t mg.st = @s mg.olqp
scoreboard players operation $t mg.st /= $m mg.st
scoreboard players operation $t mg.st %= #2 mg.st
execute if score $t mg.st matches 1 run return run title @s actionbar {"text":"✔ Déjà fait","color":"gray"}
scoreboard players operation @s mg.olqp += $m mg.st
function mg:ombre/xp {n:60}
$execute positioned $(x) $(y) $(z) run particle minecraft:explosion ~0.5 ~1 ~0.5 0.4 0.6 0.4 0 3 force
$execute positioned $(x) $(y) $(z) run particle minecraft:end_rod ~0.5 ~1.5 ~0.5 0.3 1 0.3 0.1 40 force
execute at @s run playsound minecraft:block.respawn_anchor.deplete player @a ~ ~ ~ 1 1.2
title @s actionbar {"text":"✦ Fait !","color":"gold","bold":true}
scoreboard players set @s mg.olal 30
$execute if score @s mg.olqp matches $(f).. run function mg:ombre/q/actdone_any
