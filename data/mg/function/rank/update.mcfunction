# @s : score général, niveau, barre d'XP
execute unless score @s mg.stp matches -2147483648.. run scoreboard players set @s mg.stp 0
execute unless score @s mg.wins matches -2147483648.. run scoreboard players set @s mg.wins 0
execute unless score @s mg.stk matches -2147483648.. run scoreboard players set @s mg.stk 0
scoreboard players operation $rg mg.st = @s mg.stp
scoreboard players operation $rg mg.st *= #10 mg.st
scoreboard players operation $rw mg.st = @s mg.wins
scoreboard players operation $rw mg.st *= #50 mg.st
scoreboard players operation $rg mg.st += $rw mg.st
scoreboard players operation $rw mg.st = @s mg.stk
scoreboard players operation $rw mg.st *= #2 mg.st
scoreboard players operation $rg mg.st += $rw mg.st
scoreboard players operation @s mg.gen = $rg mg.st
execute unless score @s mg.lvl matches 0.. run scoreboard players set @s mg.lvl 0
execute if score @s mg.gen = @s mg.genc if entity @s[tag=mg.xpok] run return 0
tag @s remove mg.rkfirst
execute unless score @s mg.genc matches -2147483648.. run tag @s add mg.rkfirst
scoreboard players operation @s mg.genc = @s mg.gen
scoreboard players operation $rl0 mg.st = @s mg.lvl
function mg:rank/level_up
execute if score @s mg.lvl > $rl0 mg.st unless entity @s[tag=mg.rkfirst] run function mg:rank/announce
execute if entity @s[tag=mg.rkfirst] run function mg:hall/top {obj:"mg.lvl",key:"gen",lbl:"🏅 Meilleur niveau général",col:"aqua",unit:" niv."}
tag @s remove mg.xpok
execute unless entity @s[tag=mg.play] unless entity @s[tag=mg.surv] run function mg:rank/xp
