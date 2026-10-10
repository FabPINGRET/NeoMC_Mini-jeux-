# Forme les paires au hasard (récursif) : un marcheur puis un guide ; reste impair → guide en plus ; 8 paires max
execute unless entity @a[tag=mg.play,tag=!mg.lbx] run return 0
execute if score $lbn mg.st matches 8.. run return run execute as @a[tag=mg.play,tag=!mg.lbx] run function mg:lab/extra_one
execute store result score $u mg.st if entity @a[tag=mg.play,tag=!mg.lbx]
execute if score $u mg.st matches 1 if score $lbn mg.st matches 1.. run return run execute as @a[tag=mg.play,tag=!mg.lbx] run function mg:lab/extra_one
scoreboard players add $lbn mg.st 1
execute as @a[tag=mg.play,tag=!mg.lbx,sort=random,limit=1] run function mg:lab/set_walker
execute as @a[tag=mg.play,tag=!mg.lbx,sort=random,limit=1] run function mg:lab/set_guide
function mg:lab/pair
