# ⚡ Tron — tick
scoreboard players add $trt mg.st 1
execute if score $trm mg.st matches 1 as @a[tag=mg.play] run function mg:tronxl/jump_tick
scoreboard players reset @a[scores={mg.qs=1..}] mg.qs
execute as @a[tag=mg.play] run function mg:tronxl/step
execute store result score $alive mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $alive mg.st matches 1 as @a[tag=mg.play,limit=1] run function mg:core/win_player
execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw
