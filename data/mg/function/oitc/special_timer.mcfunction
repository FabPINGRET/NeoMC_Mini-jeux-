# Toutes les 30 s : une flèche enchantée pour un joueur au hasard
scoreboard players set $os mg.st 0
execute as @r[tag=mg.play] run function mg:oitc/special_award
