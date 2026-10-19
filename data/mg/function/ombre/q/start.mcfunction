# @s vient d'arriver à l'étape (titres de chapitre, déblocages, cinématiques)
execute if score @s mg.olch matches 5 run function mg:ombre/q/chapter {t:"I · Les brigands de Valdor"}
execute if score @s mg.olch matches 11 run function mg:ombre/q/chapter {t:"II · Le chant de Sylvanor"}
execute if score @s mg.olch matches 16 run function mg:ombre/q/chapter {t:"III · Le cœur de l'hiver"}
execute if score @s mg.olch matches 23 run function mg:ombre/q/chapter {t:"IV · La brume maudite"}
execute if score @s mg.olch matches 29 run function mg:ombre/q/chapter {t:"V · Les sables du pharaon"}
execute if score @s mg.olch matches 35 run function mg:ombre/q/chapter {t:"VI · Les ailes de feu"}
execute if score @s mg.olch matches 40 run function mg:ombre/q/chapter {t:"VII · La porte des rois"}
execute if score @s mg.olch matches 46 run function mg:ombre/q/chapter {t:"VIII · La Lune Noire"}
execute if score @s mg.olch matches 51 run function mg:ombre/q/chapter {t:"Épilogue · L'Aube retrouvée"}
execute if score @s mg.olch matches 3 run function mg:ombre/cs/open_w
execute if score @s mg.olch matches 11 run function mg:ombre/cs/open_nw
execute if score @s mg.olch matches 16 run function mg:ombre/cs/open_n
execute if score @s mg.olch matches 23 run function mg:ombre/cs/open_ne
execute if score @s mg.olch matches 29 run function mg:ombre/cs/open_e
execute if score @s mg.olch matches 35 run function mg:ombre/cs/open_se
execute if score @s mg.olch matches 40 run function mg:ombre/cs/open_s
execute if score @s mg.olch matches 46 run function mg:ombre/cs/open_sw
execute if score @s mg.olch matches 52 run function mg:ombre/cs/finale
