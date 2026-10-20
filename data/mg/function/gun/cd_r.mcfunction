# Variante « dernière balle » (macro n, s = recharge, h = recharge Speed Cola) : l'overlay couvre la recharge
$execute if entity @s[tag=mg.zsc] unless items entity @s weapon.mainhand *[custom_data~{gcr:2b}] run function mg:gun/cd_set {n:$(n),s:$(h),m:2}
$execute unless entity @s[tag=mg.zsc] unless items entity @s weapon.mainhand *[custom_data~{gcr:1b}] run function mg:gun/cd_set {n:$(n),s:$(s),m:1}
