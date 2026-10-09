# Surface sous la balle → $gff frottement en roulant (‰ gardés / tick), $gfr restitution, $gfh vitesse gardée à l'impact
scoreboard players set $gff mg.st 900
scoreboard players set $gfr mg.st 450
scoreboard players set $gfh mg.st 750
execute if block ~ ~-0.05 ~ #mg:golf_green run return run function mg:golf/s_green
execute if block ~ ~-0.05 ~ #mg:golf_fairway run return run function mg:golf/s_fair
execute if block ~ ~-0.05 ~ #mg:golf_rough run return run function mg:golf/s_rough
execute if block ~ ~-0.05 ~ minecraft:sand run return run function mg:golf/s_sand
