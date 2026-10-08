execute as @a[tag=mg.play,tag=!mg.inf,sort=random,limit=1] run function mg:inf/make_zombie
scoreboard players remove $inn mg.st 1
execute if score $inn mg.st matches 1.. run function mg:inf/pick
