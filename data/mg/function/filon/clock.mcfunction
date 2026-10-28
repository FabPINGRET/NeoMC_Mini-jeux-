# Chaque seconde (toujours) : cycle de 45 min, cours du marché, PvP, annonces
scoreboard players add $fnt mg.st 1
execute if score $fnt mg.st matches 2700.. if score $fnw mg.st matches 1 if score $fnok mg.st matches 1 run function mg:filon/regen
execute if score $fnt mg.st matches 2700.. run function mg:filon/cycle_idle
scoreboard players operation #m mg.st = $fnt mg.st
scoreboard players operation #m mg.st %= #fnmk mg.st
execute if score #m mg.st matches 0 run function mg:filon/market
execute unless score $fnw mg.st matches 1 run return 0
function mg:filon/pvp_check
execute if score $fnt mg.st matches 2640 run tellraw @a[tag=mg.fnw] {"text":"⛏ Le filon se régénère dans 1 minute (les mineurs remonteront tout seuls).","color":"gold"}
scoreboard players operation #pa mg.st = $fnpr mg.st
scoreboard players remove #pa mg.st 30
execute if score $fnt mg.st = #pa mg.st run tellraw @a[tag=mg.fnw] {"text":"⚔ Attention : PvP dans la mine dans 30 secondes !","color":"red"}
execute if score $fnt mg.st = #pa mg.st as @a[tag=mg.fnw] at @s run playsound minecraft:block.bell.use master @s ~ ~ ~ 1 0.8
function mg:filon/second
