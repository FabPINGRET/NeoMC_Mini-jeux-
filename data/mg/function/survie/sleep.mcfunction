scoreboard players set $svn mg.st 0
scoreboard players set $svs mg.st 0
execute as @a[tag=mg.surv] if dimension mg:survie run scoreboard players add $svn mg.st 1
execute as @a[tag=mg.surv,nbt={SleepTimer:100s}] if dimension mg:survie run scoreboard players add $svs mg.st 1
execute if score $svs mg.st matches 1.. if score $svs mg.st = $svn mg.st run function mg:survie/morning
