# Plateau (état 2, jeu 59). $mph : 0 début de tour, 1 attente du dé, 2 dé qui roule, 3 déplacement, 4 effet de case, 5 roulette du mini-jeu
execute if score $mph mg.st matches 0 run function mg:party/turn_start
execute if score $mph mg.st matches 1 run function mg:party/wait_roll
execute if score $mph mg.st matches 2 run function mg:party/roll_anim
execute if score $mph mg.st matches 3 run function mg:party/move_tick
execute if score $mph mg.st matches 4 run function mg:party/effect_wait
execute if score $mph mg.st matches 5 run function mg:party/roulette

scoreboard players add $mpu mg.st 1
execute if score $mpu mg.st matches 20.. run function mg:party/upkeep
