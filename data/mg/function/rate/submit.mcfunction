# @s a envoyé sa note : mg.rt = 1 abc (a mode, b carte, c fun, 0 = pas d'avis). Généré.
scoreboard players operation $rv mg.st = @s mg.rt
scoreboard players reset @s mg.rt
execute unless entity @s[tag=mg.rate] run return run tellraw @s {"text":"⭐ Plus de partie à noter.","color":"gray"}
execute unless score $rv mg.st matches 1000..1555 run return 0
tag @s remove mg.rate
scoreboard players remove $rv mg.st 1000
scoreboard players operation $ra1 mg.st = $rv mg.st
scoreboard players operation $ra1 mg.st /= #100 mg.st
scoreboard players operation $rb1 mg.st = $rv mg.st
scoreboard players operation $rb1 mg.st /= #10 mg.st
scoreboard players operation $rb1 mg.st %= #10 mg.st
scoreboard players operation $rc1 mg.st = $rv mg.st
scoreboard players operation $rc1 mg.st %= #10 mg.st
execute if score $ra1 mg.st matches 6.. run scoreboard players set $ra1 mg.st 0
execute if score $rb1 mg.st matches 6.. run scoreboard players set $rb1 mg.st 0
execute if score $rc1 mg.st matches 6.. run scoreboard players set $rc1 mg.st 0
function mg:rate/add with storage mg:rate key
function mg:rate/thanks
execute at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.6 1.2
