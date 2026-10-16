# @s : passage(s) de niveau (besoin = 80 + 40 × niveau)
execute if score @s mg.trlv matches 20.. run return run scoreboard players set @s mg.trxp 0
scoreboard players operation $need mg.st = @s mg.trlv
scoreboard players operation $need mg.st *= #40 mg.st
scoreboard players add $need mg.st 80
execute if score @s mg.trxp < $need mg.st run return 0
scoreboard players operation @s mg.trxp -= $need mg.st
scoreboard players add @s mg.trlv 1
function mg:terra/rpg/lvup
function mg:terra/rpg/lvchk
