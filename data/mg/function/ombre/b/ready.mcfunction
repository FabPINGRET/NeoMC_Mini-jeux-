# La région en cours ($olrl) est-elle chargée ?
execute if score $olrl mg.st matches 1 run return run function mg:ombre/b/ld1
execute if score $olrl mg.st matches 2 run return run function mg:ombre/b/ld2
execute if score $olrl mg.st matches 3 run return run function mg:ombre/b/ld3
execute if score $olrl mg.st matches 4 run return run function mg:ombre/b/ld4
execute if score $olrl mg.st matches 5 run return run function mg:ombre/b/ld5
execute if score $olrl mg.st matches 6 run return run function mg:ombre/b/ld6
execute if score $olrl mg.st matches 7 run return run function mg:ombre/b/ld7
execute if score $olrl mg.st matches 8 run return run function mg:ombre/b/ld8
execute if score $olrl mg.st matches 9 run return run function mg:ombre/b/ld9
return 0
