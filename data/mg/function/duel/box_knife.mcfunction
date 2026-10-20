# Coup de couteau sur la boîte de clic de l'adversaire (gun/cl_foreign : @s = attaquant, victime = @a[tag=mg.gcme]) :
# la boîte de 2,6 blocs autour de ses yeux intercepte le coup, mg:duel_melee ne se déclenche donc pas ; mêmes règles que melee_adv
execute unless entity @s[tag=mg.dl,tag=!mg.dlp] run return 0
execute unless items entity @s weapon.mainhand *[custom_data~{mg_kn:1b}] run return 0
execute if score @s mg.dlkc matches 1.. run return 0
scoreboard players operation $dli mg.st = @s mg.dli
execute at @s as @a[tag=mg.gcme,tag=mg.dl,tag=!mg.dlp,distance=..4.5] if score @s mg.dli = $dli mg.st run tag @s add mg.dlvc
execute unless entity @a[tag=mg.dlvc] run return 0
# recharge posée AVANT le coup (comme melee_adv), puis le coup existant (melee_hit)
scoreboard players set @s mg.dlkc 20
tag @s add mg.dlsh
execute as @a[tag=mg.dlvc,limit=1] run function mg:duel/melee_hit
tag @a remove mg.dlvc
tag @s remove mg.dlsh
