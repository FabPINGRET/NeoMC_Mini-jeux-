# @s : barre d'XP = mana (niveau affiché = mana, remplissage = mana / max)
execute store result storage mg:ombre mb.l int 1 run scoreboard players get @s mg.olmp
# points du niveau L : 2L+7 (L ≤ 15), 5L-38 (L ≤ 30), 9L-158 au-delà
scoreboard players operation $L mg.st = @s mg.olmp
scoreboard players operation $need mg.st = $L mg.st
scoreboard players operation $need mg.st *= #2 mg.st
scoreboard players add $need mg.st 7
execute if score $L mg.st matches 16..30 run scoreboard players operation $need mg.st = $L mg.st
execute if score $L mg.st matches 16..30 run scoreboard players operation $need mg.st *= #5 mg.st
execute if score $L mg.st matches 16..30 run scoreboard players remove $need mg.st 38
execute if score $L mg.st matches 31.. run scoreboard players operation $need mg.st = $L mg.st
execute if score $L mg.st matches 31.. run scoreboard players operation $t mg.st = #4 mg.st
execute if score $L mg.st matches 31.. run scoreboard players operation $need mg.st *= #8 mg.st
execute if score $L mg.st matches 31.. run scoreboard players operation $need mg.st += $L mg.st
execute if score $L mg.st matches 31.. run scoreboard players remove $need mg.st 158
scoreboard players operation $pt mg.st = @s mg.olmp
scoreboard players operation $pt mg.st *= $need mg.st
scoreboard players operation $pt mg.st /= @s mg.olmm
scoreboard players remove $pt mg.st 1
execute if score $pt mg.st matches ..-1 run scoreboard players set $pt mg.st 0
execute store result storage mg:ombre mb.p int 1 run scoreboard players get $pt mg.st
function mg:ombre/mana_bar_m with storage mg:ombre mb
