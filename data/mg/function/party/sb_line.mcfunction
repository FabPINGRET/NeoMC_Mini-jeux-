# Ligne de @s dans le classement : rang = étoiles x 1000 + pièces, affichage « ★ étoiles   ● pièces »
scoreboard players operation @s mg.mpz = @s mg.mpk
scoreboard players operation @s mg.mpz *= #1000 mg.st
scoreboard players operation @s mg.mpz += @s mg.mpm
execute store result storage mg:party sb.k int 1 run scoreboard players get @s mg.mpk
execute store result storage mg:party sb.m int 1 run scoreboard players get @s mg.mpm
function mg:party/sb_line_m with storage mg:party sb
