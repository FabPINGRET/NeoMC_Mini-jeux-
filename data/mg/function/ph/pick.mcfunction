execute as @a[tag=mg.play,tag=!mg.phs,sort=random,limit=1] run tag @s add mg.phs
scoreboard players remove $phn mg.st 1
execute if score $phn mg.st matches 1.. run function mg:ph/pick
