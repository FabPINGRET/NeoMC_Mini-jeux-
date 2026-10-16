# Chaque seconde (dimension) : régions, lieux, étapes, primes, population, capacités, boss
execute as @a[tag=mg.tvw,tag=!mg.trcine] run function mg:terra/rpg/region
function mg:terra/rpg/pois
execute as @a[tag=mg.tvw,tag=!mg.trcine] run function mg:terra/rpg/qtick
# première arrivée : cinématique d'introduction (la carte est chargée)
execute as @a[tag=mg.tvw,tag=!mg.trcine,tag=!mg.trintro,scores={mg.trch=0}] run function mg:terra/rpg/intro_go
scoreboard players enable @a[tag=mg.tvw] mg.trtk
execute as @a[tag=mg.tvw,scores={mg.tkdilo=1..}] run function mg:terra/rpg/k_dilo
execute as @a[tag=mg.tvw,scores={mg.tkcompy=1..}] run function mg:terra/rpg/k_compy
execute as @a[tag=mg.tvw,scores={mg.tkptera=1..}] run function mg:terra/rpg/k_ptera
execute as @a[tag=mg.tvw,scores={mg.tksix=1..}] run function mg:terra/rpg/k_six
execute as @a[tag=mg.tvw,scores={mg.tkherb=1..}] run function mg:terra/rpg/k_herb2
execute as @a[tag=mg.tvw,scores={mg.tkherb2=1..}] run function mg:terra/rpg/k_herb2
execute as @a[tag=mg.tvw,scores={mg.tkherb3=1..}] run function mg:terra/rpg/k_herb2
execute as @a[tag=mg.tvw,scores={mg.tkherb4=1..}] run function mg:terra/rpg/k_herb2
# cycle de 6 s : une région complétée par seconde, puis nettoyage des dinosaures loin de tout joueur
scoreboard players add $trq3 mg.st 1
execute if score $trq3 mg.st matches 6.. run scoreboard players set $trq3 mg.st 0
execute if score $trq3 mg.st matches 0 if entity @a[tag=mg.tvw,scores={mg.trrg=1}] run function mg:terra/rpg/pop_n
execute if score $trq3 mg.st matches 1 if entity @a[tag=mg.tvw,scores={mg.trrg=2}] run function mg:terra/rpg/pop_e
execute if score $trq3 mg.st matches 2 if entity @a[tag=mg.tvw,scores={mg.trrg=3}] run function mg:terra/rpg/pop_w
execute if score $trq3 mg.st matches 3 if entity @a[tag=mg.tvw,scores={mg.trrg=4}] run function mg:terra/rpg/pop_s
execute if score $trq3 mg.st matches 5 as @e[tag=mg.trr,tag=!mg.trboss] at @s unless entity @a[tag=mg.tvw,distance=..96] run tp @s ~ -400 ~
function mg:terra/rpg/abilities
function mg:terra/rpg/bosses
function mg:terra/rpg/dungeons
function mg:terra/rpg/cl/second
function mg:terra/rpg/second2
