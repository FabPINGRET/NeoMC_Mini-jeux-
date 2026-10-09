# @s : quille debout ; contact si distance à la boule < 0,5
scoreboard players operation #dx mg.st = @s mg.bx
scoreboard players operation #dx mg.st -= #bx mg.st
execute unless score #dx mg.st matches -500..500 run return 0
scoreboard players operation #dz mg.st = @s mg.bz
scoreboard players operation #dz mg.st -= #bz mg.st
execute unless score #dz mg.st matches -500..500 run return 0
scoreboard players operation #d2 mg.st = #dx mg.st
scoreboard players operation #d2 mg.st *= #dx mg.st
scoreboard players operation #q mg.st = #dz mg.st
scoreboard players operation #q mg.st *= #dz mg.st
scoreboard players operation #d2 mg.st += #q mg.st
execute if score #d2 mg.st matches 250000.. run return 0
function mg:bowl/ball_hit
