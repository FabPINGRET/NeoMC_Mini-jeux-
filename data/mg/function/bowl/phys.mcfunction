# Un sous-pas de physique (2 par tick) : boules puis quilles en mouvement
execute as @e[type=minecraft:item_display,tag=mg.bball] run function mg:bowl/ball_step
execute as @e[type=minecraft:block_display,tag=mg.bpmv] run function mg:bowl/pin_step
