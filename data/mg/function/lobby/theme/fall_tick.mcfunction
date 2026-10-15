# Cycle des chutes (chaque seconde, appelé par lobby/theme/tick) : compte à rebours, bascule, fondu
scoreboard players add $thi mg.st 0
scoreboard players remove $thd mg.st 1
execute if score $thd mg.st matches ..0 run function mg:lobby/theme/fall_flip
execute if score $thw mg.st matches 1 if score $thi mg.st matches ..7 run scoreboard players add $thi mg.st 1
execute if score $thw mg.st matches 0 if score $thi mg.st matches 1.. run scoreboard players remove $thi mg.st 1
