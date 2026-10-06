# Spleef — retire les étages en trop selon le nombre de joueurs ($nf = étages conservés)
execute if score $nf mg.st matches ..1 run fill -12 73 288 12 73 312 minecraft:air
execute if score $nf mg.st matches ..2 run fill -10 66 290 10 66 310 minecraft:air
execute if score $nf mg.st matches ..3 run fill -8 59 292 8 59 308 minecraft:air
