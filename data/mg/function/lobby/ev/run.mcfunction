scoreboard players remove $evt mg.st 1
bossbar set mg:ev players @a[tag=mg.evl]
execute if score $evon mg.st matches 1 run function mg:lobby/ev/e1_sec
execute if score $evon mg.st matches 2 run function mg:lobby/ev/e2_sec
execute if score $evon mg.st matches 3 run function mg:lobby/ev/e3_sec
execute if score $evon mg.st matches 1.. if score $evt mg.st matches ..0 run function mg:lobby/ev/timeup
