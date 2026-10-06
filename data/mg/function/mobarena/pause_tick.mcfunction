# Mob Arena — compte à rebours avant la vague suivante
scoreboard players remove $wt mg.st 1
execute if score $wt mg.st matches ..0 run function mg:mobarena/next_wave
