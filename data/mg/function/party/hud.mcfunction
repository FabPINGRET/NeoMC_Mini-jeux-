# Tableau de droite : classement (étoiles puis pièces, « ★ 3   ● 23 » sur chaque ligne) ; étoiles sous le pseudo et dans Tab
scoreboard players set #1000 mg.st 1000
scoreboard objectives modify mg.mpz displayname [{"text":"★ MINI PARTY","color":"gold","bold":true}]
scoreboard objectives setdisplay sidebar mg.mpz
scoreboard objectives setdisplay below_name mg.mpk
scoreboard objectives setdisplay list mg.mpk
execute as @a[tag=mg.mpp] run function mg:party/sb_line
