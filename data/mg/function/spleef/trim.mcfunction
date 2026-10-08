# Spleef — retire les étages en trop selon le nombre de joueurs ($nf = étages conservés)
execute if score $nf mg.st matches ..1 run fill -12 76 288 12 76 312 minecraft:air
execute if score $nf mg.st matches ..2 run fill -10 72 290 10 72 310 minecraft:air
execute if score $nf mg.st matches ..3 run fill -8 68 292 8 68 308 minecraft:air
