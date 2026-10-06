# Affiche les constructeurs par ordre décroissant de moyenne (récursif)
scoreboard players set $bbrm mg.st -1
execute as @a[tag=mg.play,scores={mg.bi=0..},tag=!mg.brk] run scoreboard players operation $bbrm mg.st > @s mg.ba
execute if score $bbrm mg.st matches ..-1 run return 0
scoreboard players set $bbrt mg.st 0
execute as @a[tag=mg.play,scores={mg.bi=0..},tag=!mg.brk] if score @s mg.ba = $bbrm mg.st run function mg:bb/rank_line
scoreboard players operation $bbrk mg.st += $bbrt mg.st
function mg:bb/rank_next
