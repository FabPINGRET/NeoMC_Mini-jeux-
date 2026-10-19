# bit $(b) déjà pris ?
$execute store result score $m mg.st run function mg:ombre/q/pow2 {b:$(b)}
scoreboard players operation $t mg.st = @s mg.olqp
scoreboard players operation $t mg.st /= $m mg.st
scoreboard players operation $t mg.st %= #2 mg.st
execute if score $t mg.st matches 1 run return run title @s actionbar {"text":"✔ Déjà ramassé","color":"gray"}
scoreboard players add @s mg.olpk 1
execute if score @s mg.olpk matches ..5 run title @s actionbar {"text":"✋ Ramassage…","color":"yellow"}
execute if score @s mg.olpk matches ..5 run return 0
scoreboard players set @s mg.olpk 0
scoreboard players operation @s mg.olqp += $m mg.st
title @s actionbar {"text":"✔ Ramassé !","color":"green","bold":true}
execute at @s run playsound minecraft:entity.item.pickup player @s ~ ~ ~ 1 0.8
function mg:ombre/xp {n:40}
$execute if score @s mg.olqp matches $(f).. run function mg:ombre/q/adv
