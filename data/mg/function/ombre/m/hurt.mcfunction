# @s (joueur) vient d'être blessé : effet de l'attaquant, animation des créatures
scoreboard players set @s mg.oldt 0
execute on attacker if entity @s[tag=mg.olbd] run scoreboard players set @s mg.olat 8
execute if function mg:ombre/m/att_araignee run effect give @s minecraft:poison 3 0
execute if function mg:ombre/m/att_yeti run effect give @s minecraft:slowness 3 1
execute if function mg:ombre/m/att_sangsue run effect give @s minecraft:poison 3 0
execute if function mg:ombre/m/att_scorpion run effect give @s minecraft:poison 4 1
execute if function mg:ombre/m/att_rampant run effect give @s minecraft:poison 3 1
execute if function mg:ombre/m/att_chevnoir run effect give @s minecraft:wither 3 0
execute if function mg:ombre/m/att_errant run effect give @s minecraft:darkness 3 0
execute if function mg:ombre/m/att_a_tisseuse run effect give @s minecraft:poison 4 1
execute if function mg:ombre/m/att_a_wendigo run effect give @s minecraft:slowness 3 2
