# @s (colon) vient d'être blessé : le dinosaure qui l'a mordu joue son attaque
scoreboard players set @s mg.trdt 0
execute on attacker if entity @s[tag=mg.tvd] run scoreboard players set @s mg.tvat 8
