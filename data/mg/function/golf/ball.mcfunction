# @s = balle en mouvement, chaque tick : gravité, traînée, 4 sous-pas (collisions), sol, hors-jeu, trace
function mg:golf/speed
scoreboard players operation $gfsp0 mg.st = $gfsp mg.st
scoreboard players remove @s mg.gfv 40
execute unless entity @s[tag=mg.gfg] run function mg:golf/drag
execute if entity @s[tag=mg.gfmv] run function mg:golf/sub
execute if entity @s[tag=mg.gfmv] run function mg:golf/sub
execute if entity @s[tag=mg.gfmv] run function mg:golf/sub
execute if entity @s[tag=mg.gfmv] run function mg:golf/sub
execute unless entity @s[tag=mg.gfmv] run return 0
tag @s remove mg.gfg
execute at @s unless block ~ ~-0.05 ~ #mg:golf_pass run function mg:golf/roll
execute unless entity @s[tag=mg.gfmv] run return 0
execute if score @s mg.gfy matches ..56000 run return run function mg:golf/penalty_void
execute unless score @s mg.gfx matches 198000..402000 run return run function mg:golf/penalty_void
execute unless score @s mg.gfz matches 34498000..34702000 run return run function mg:golf/penalty_void
execute unless entity @s[tag=mg.gfg] run function mg:golf/trail
