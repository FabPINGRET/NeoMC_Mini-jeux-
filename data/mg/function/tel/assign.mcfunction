execute if score $tk mg.st matches ..11 run scoreboard players operation @s mg.ti = $tk mg.st
execute if score $tk mg.st matches 12.. run scoreboard players set @s mg.ti -1
scoreboard players add $tk mg.st 1
