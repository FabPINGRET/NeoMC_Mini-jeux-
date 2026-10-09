# Monte de niveau tant que le score le permet (récursif ; les stats ne baissent jamais)
function mg:rank/need
execute if score @s mg.gen >= $rn mg.st run scoreboard players add @s mg.lvl 1
execute if score @s mg.gen >= $rn mg.st if score @s mg.lvl matches ..999 run function mg:rank/level_up
