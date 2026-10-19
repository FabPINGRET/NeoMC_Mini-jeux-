# Exécute la prochaine commande de construction (boucle de $olk commandes)
execute unless data storage mg:ombre q[0] run return 0
data modify storage mg:ombre c.c set from storage mg:ombre q[0]
data remove storage mg:ombre q[0]
function mg:ombre/b/exec with storage mg:ombre c
scoreboard players remove $olk mg.st 1
execute if score $olk mg.st matches 1.. run function mg:ombre/b/run
