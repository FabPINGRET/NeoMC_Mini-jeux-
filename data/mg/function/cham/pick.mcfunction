execute as @a[tag=mg.play,tag=!mg.cms,sort=random,limit=1] run tag @s add mg.cms
scoreboard players remove $cmn mg.st 1
execute if score $cmn mg.st matches 1.. run function mg:cham/pick
