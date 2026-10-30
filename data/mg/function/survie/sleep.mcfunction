scoreboard players set $svn mg.st 0
scoreboard players set $svs mg.st 0
# (at @s : « if dimension » teste la dimension d'exécution, pas celle du joueur)
execute as @a[tag=mg.surv] at @s if dimension mg:survie run scoreboard players add $svn mg.st 1
execute as @a[tag=mg.surv,nbt={SleepTimer:100s}] at @s if dimension mg:survie run scoreboard players add $svs mg.st 1
execute if score $svs mg.st matches 1.. if score $svs mg.st = $svn mg.st run function mg:survie/morning
