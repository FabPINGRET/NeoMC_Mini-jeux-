# Un pas du rayon (0,5 bloc) : neige → détruite et fin ; autre bloc plein → fin ; air → on avance
execute if block ~ ~ ~ minecraft:snow_block run return run function mg:splegg/hit
execute unless block ~ ~ ~ #minecraft:air run return 0
particle minecraft:snowflake ~ ~ ~ 0 0 0 0 1
scoreboard players remove $rs mg.st 1
execute if score $rs mg.st matches 1.. positioned ^ ^ ^0.5 run function mg:splegg/ray
