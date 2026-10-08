# Fin d'étape : complète les réponses manquantes, puis étape suivante
execute if score $tp mg.st matches 0 as @a[tag=mg.play,scores={mg.ti=0..}] unless entity @s[tag=mg.tdone] run function mg:tel/fill_word
execute if score $tp mg.st matches 2 as @a[tag=mg.play,scores={mg.ti=0..}] unless entity @s[tag=mg.tdone] run function mg:tel/fill_guess
execute if score $tp mg.st matches 4 as @a[tag=mg.play,scores={mg.ti=0..}] unless entity @s[tag=mg.tdone] run function mg:tel/fill_guess
execute if score $tp mg.st matches 1 run gamemode adventure @a[tag=mg.play,scores={mg.ti=0..}]
execute if score $tp mg.st matches 3 run gamemode adventure @a[tag=mg.play,scores={mg.ti=0..}]
kill @e[type=minecraft:item,x=-400,y=0,z=19400,dx=800,dy=200,dz=250]
function mg:tel/phase_start
