# Chaque seconde : monstres neutres provoqués, capacités, noms des élites, nettoyage au loin
scoreboard players add $olcy mg.st 1
execute if score $olcy mg.st matches 9.. run scoreboard players set $olcy mg.st 1
function mg:ombre/m/pop
# toutes les 3 s : un neutre sans proie proche « flaire » un joueur à 20 blocs
execute if score $olq60 mg.st matches 0 as @e[tag=mg.olprov] at @s unless entity @a[tag=mg.olw,distance=..5] if entity @a[tag=mg.olw,gamemode=adventure,distance=..20] run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..20]
execute as @e[tag=mg.olelnm] run function mg:ombre/m/elite_name
execute if score $olq60 mg.st matches 20 as @e[tag=mg.olm,tag=!mg.olboss,tag=!mg.olalpha,tag=!mg.oldg] at @s unless entity @a[tag=mg.olw,distance=..100] run kill @s
# capacités
execute as @e[tag=mg.olk_yeti] at @s if entity @a[tag=mg.olw,gamemode=adventure,distance=..3] if predicate mg:tv_c20 run function mg:ombre/m/ab_slam
execute as @e[tag=mg.olk_drake] at @s if entity @a[tag=mg.olw,gamemode=adventure,distance=3..9] if predicate mg:tv_c33 run function mg:ombre/m/ab_breath
execute as @e[tag=mg.olk_garou] at @s if entity @a[tag=mg.olw,gamemode=adventure,distance=3..8] if predicate mg:tv_c20 run function mg:ombre/m/ab_pounce
execute as @e[tag=mg.olk_gardien] at @s if entity @a[tag=mg.olw,gamemode=adventure,distance=..4] if predicate mg:tv_c20 run function mg:ombre/m/ab_slam
execute as @e[tag=mg.olk_a_tisseuse] at @s if entity @a[tag=mg.olw,gamemode=adventure,distance=..10] if predicate mg:tv_c20 run function mg:ombre/m/ab_web
