execute if score $ols mg.st matches 10.. run return run function mg:ombre/st/done
execute if score $olsw mg.st matches 0 run scoreboard players operation $olrl mg.st = $ols mg.st
execute if score $olsw mg.st matches 0 if score $ols mg.st matches 1 in mg:ombrelune run function mg:ombre/b/fl1
execute if score $olsw mg.st matches 0 if score $ols mg.st matches 2 in mg:ombrelune run function mg:ombre/b/fl2
execute if score $olsw mg.st matches 0 if score $ols mg.st matches 3 in mg:ombrelune run function mg:ombre/b/fl3
execute if score $olsw mg.st matches 0 if score $ols mg.st matches 4 in mg:ombrelune run function mg:ombre/b/fl4
execute if score $olsw mg.st matches 0 if score $ols mg.st matches 5 in mg:ombrelune run function mg:ombre/b/fl5
execute if score $olsw mg.st matches 0 if score $ols mg.st matches 6 in mg:ombrelune run function mg:ombre/b/fl6
execute if score $olsw mg.st matches 0 if score $ols mg.st matches 7 in mg:ombrelune run function mg:ombre/b/fl7
execute if score $olsw mg.st matches 0 if score $ols mg.st matches 8 in mg:ombrelune run function mg:ombre/b/fl8
execute if score $olsw mg.st matches 0 if score $ols mg.st matches 9 in mg:ombrelune run function mg:ombre/b/fl9
scoreboard players set $olsw mg.st 1
execute in mg:ombrelune unless function mg:ombre/b/ready run return run schedule function mg:ombre/st/step 5t
execute if score $ols mg.st matches 1 in mg:ombrelune run function mg:ombre/st/1
execute if score $ols mg.st matches 2 in mg:ombrelune run function mg:ombre/st/2
execute if score $ols mg.st matches 3 in mg:ombrelune run function mg:ombre/st/3
execute if score $ols mg.st matches 4 in mg:ombrelune run function mg:ombre/st/4
execute if score $ols mg.st matches 5 in mg:ombrelune run function mg:ombre/st/5
execute if score $ols mg.st matches 6 in mg:ombrelune run function mg:ombre/st/6
execute if score $ols mg.st matches 7 in mg:ombrelune run function mg:ombre/st/7
execute if score $ols mg.st matches 8 in mg:ombrelune run function mg:ombre/st/8
execute if score $ols mg.st matches 9 in mg:ombrelune run function mg:ombre/st/9
execute if score $ols mg.st matches 1 in mg:ombrelune run function mg:ombre/b/uf1
execute if score $ols mg.st matches 2 in mg:ombrelune run function mg:ombre/b/uf2
execute if score $ols mg.st matches 3 in mg:ombrelune run function mg:ombre/b/uf3
execute if score $ols mg.st matches 4 in mg:ombrelune run function mg:ombre/b/uf4
execute if score $ols mg.st matches 5 in mg:ombrelune run function mg:ombre/b/uf5
execute if score $ols mg.st matches 6 in mg:ombrelune run function mg:ombre/b/uf6
execute if score $ols mg.st matches 7 in mg:ombrelune run function mg:ombre/b/uf7
execute if score $ols mg.st matches 8 in mg:ombrelune run function mg:ombre/b/uf8
execute if score $ols mg.st matches 9 in mg:ombrelune run function mg:ombre/b/uf9
scoreboard players add $ols mg.st 1
scoreboard players set $olsw mg.st 0
schedule function mg:ombre/st/step 2t
