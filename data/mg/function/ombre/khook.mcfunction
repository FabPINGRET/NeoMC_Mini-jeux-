# @s a vaincu l'espèce n° $kk : campagne, quêtes secondaires, contrat
execute if score @s mg.olch matches 3 if score $kk mg.st matches 0 run function mg:ombre/q/kp {n:4}
execute if score @s mg.olch matches 3 if score $kk mg.st matches 1 run function mg:ombre/q/kp {n:4}
execute if score @s mg.olch matches 3 if score $kk mg.st matches 2 run function mg:ombre/q/kp {n:4}
execute if score @s mg.olch matches 3 if score $kk mg.st matches 3 run function mg:ombre/q/kp {n:4}
execute if score @s mg.olch matches 3 if score $kk mg.st matches 4 run function mg:ombre/q/kp {n:4}
execute if score @s mg.olch matches 19 if score $kk mg.st matches 10 run function mg:ombre/q/kp {n:6}
execute if score @s mg.olch matches 19 if score $kk mg.st matches 13 run function mg:ombre/q/kp {n:6}
execute if score @s mg.olch matches 19 if score $kk mg.st matches 12 run function mg:ombre/q/kp {n:6}
execute if score @s mg.olch matches 19 if score $kk mg.st matches 11 run function mg:ombre/q/kp {n:6}
execute if score @s mg.olch matches 42 if score $kk mg.st matches 29 run function mg:ombre/q/kp {n:8}
execute if score @s mg.olch matches 42 if score $kk mg.st matches 30 run function mg:ombre/q/kp {n:8}
execute if score @s mg.olch matches 42 if score $kk mg.st matches 31 run function mg:ombre/q/kp {n:8}
execute if score @s mg.olch matches 42 if score $kk mg.st matches 32 run function mg:ombre/q/kp {n:8}
execute if score @s mg.olch matches 42 if score $kk mg.st matches 33 run function mg:ombre/q/kp {n:8}
execute if score $kk mg.st matches 0 if function mg:ombre/sq/1_on run scoreboard players add @s mg.olq1 1
execute if score $kk mg.st matches 11 if function mg:ombre/sq/5_on run scoreboard players add @s mg.olq5 1
execute if score $kk mg.st matches 18 if function mg:ombre/sq/7_on run scoreboard players add @s mg.olq7 1
execute if score $kk mg.st matches 25 if function mg:ombre/sq/11_on run scoreboard players add @s mg.olq11 1
execute if score $kk mg.st matches 34 if function mg:ombre/sq/15_on run scoreboard players add @s mg.olq15 1
scoreboard players operation $kc mg.st = $kk mg.st
scoreboard players add $kc mg.st 1
execute if score @s mg.olct = $kc mg.st run function mg:ombre/ct/prog
