# Pause entre deux trous
scoreboard players remove $gfw mg.st 1
execute if score $gfw mg.st matches 0 if score $gfh mg.st matches 6.. run return run function mg:golf/finish
execute if score $gfw mg.st matches 0 run function mg:golf/hole_next
