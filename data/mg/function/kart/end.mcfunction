execute as @a[tag=mg.play] run function mg:kart/progress
execute as @a[tag=mg.play] run function mg:kart/rank_one
execute if score $kbat mg.st matches 1 run tellraw @a[tag=!mg.surv] [{"text":"\n🎈 CLASSEMENT DE LA BATAILLE","color":"red","bold":true}]
execute unless score $kbat mg.st matches 1 run tellraw @a[tag=!mg.surv] [{"text":"\n🏁 CLASSEMENT DE LA COURSE","color":"gold","bold":true}]
scoreboard players set $kr0 mg.st 1
function mg:kart/end_line
execute unless entity @a[tag=mg.play] run return run function mg:core/draw
execute as @a[tag=mg.play,scores={mg.krk=1},limit=1] run function mg:core/win_player
