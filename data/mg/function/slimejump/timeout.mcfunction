# 4 min : le plus avancé gagne (égalité = nul)
tellraw @a[tag=mg.play] {"text":"⏰ Temps écoulé !","color":"red","bold":true}
execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw
scoreboard players set $b mg.st -1
scoreboard players operation $b mg.st > @a[tag=mg.play] mg.sjp
tag @a remove mg.sjw
execute as @a[tag=mg.play] if score @s mg.sjp = $b mg.st run tag @s add mg.sjw
execute store result score $c mg.st if entity @a[tag=mg.sjw]
execute if score $c mg.st matches 1 as @a[tag=mg.sjw,limit=1] run return run function mg:core/win_player
function mg:core/draw
