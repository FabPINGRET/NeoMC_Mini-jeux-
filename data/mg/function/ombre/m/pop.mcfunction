# Une région par seconde (cycle de 8 s) : groupe de monstres si elle a des joueurs et de la place
execute if score $olcy mg.st matches 1 if entity @a[tag=mg.olw,scores={mg.olrg=1}] run function mg:ombre/m/pop_w
execute if score $olcy mg.st matches 2 if entity @a[tag=mg.olw,scores={mg.olrg=2}] run function mg:ombre/m/pop_nw
execute if score $olcy mg.st matches 3 if entity @a[tag=mg.olw,scores={mg.olrg=3}] run function mg:ombre/m/pop_n
execute if score $olcy mg.st matches 4 if entity @a[tag=mg.olw,scores={mg.olrg=4}] run function mg:ombre/m/pop_ne
execute if score $olcy mg.st matches 5 if entity @a[tag=mg.olw,scores={mg.olrg=5}] run function mg:ombre/m/pop_e
execute if score $olcy mg.st matches 6 if entity @a[tag=mg.olw,scores={mg.olrg=6}] run function mg:ombre/m/pop_se
execute if score $olcy mg.st matches 7 if entity @a[tag=mg.olw,scores={mg.olrg=7}] run function mg:ombre/m/pop_s
execute if score $olcy mg.st matches 8 if entity @a[tag=mg.olw,scores={mg.olrg=8}] run function mg:ombre/m/pop_sw
