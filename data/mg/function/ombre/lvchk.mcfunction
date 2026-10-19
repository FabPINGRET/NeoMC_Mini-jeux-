# @s : passage(s) de niveau (besoin = 100 + 50 × niveau)
execute if score @s mg.ollv matches 35.. run return run scoreboard players set @s mg.olxp 0
scoreboard players operation $need mg.st = @s mg.ollv
scoreboard players operation $need mg.st *= #50 mg.st
scoreboard players add $need mg.st 100
execute if score @s mg.olxp < $need mg.st run return 0
scoreboard players operation @s mg.olxp -= $need mg.st
scoreboard players add @s mg.ollv 1
function mg:ombre/lvup
function mg:ombre/lvchk
