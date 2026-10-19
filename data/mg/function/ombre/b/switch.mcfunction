# Région suivante : on décharge l'ancienne, on charge la nouvelle
execute if score $olrl mg.st matches 1 run function mg:ombre/b/uf1
execute if score $olrl mg.st matches 2 run function mg:ombre/b/uf2
execute if score $olrl mg.st matches 3 run function mg:ombre/b/uf3
execute if score $olrl mg.st matches 4 run function mg:ombre/b/uf4
execute if score $olrl mg.st matches 5 run function mg:ombre/b/uf5
execute if score $olrl mg.st matches 6 run function mg:ombre/b/uf6
execute if score $olrl mg.st matches 7 run function mg:ombre/b/uf7
execute if score $olrl mg.st matches 8 run function mg:ombre/b/uf8
execute if score $olrl mg.st matches 9 run function mg:ombre/b/uf9
scoreboard players operation $olrl mg.st = $olrr mg.st
execute if score $olrl mg.st matches 1 run function mg:ombre/b/fl1
execute if score $olrl mg.st matches 2 run function mg:ombre/b/fl2
execute if score $olrl mg.st matches 3 run function mg:ombre/b/fl3
execute if score $olrl mg.st matches 4 run function mg:ombre/b/fl4
execute if score $olrl mg.st matches 5 run function mg:ombre/b/fl5
execute if score $olrl mg.st matches 6 run function mg:ombre/b/fl6
execute if score $olrl mg.st matches 7 run function mg:ombre/b/fl7
execute if score $olrl mg.st matches 8 run function mg:ombre/b/fl8
execute if score $olrl mg.st matches 9 run function mg:ombre/b/fl9
