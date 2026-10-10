# 👑 Master dit — tick
scoreboard players add $msc mg.st 1
scoreboard players remove $mst mg.st 1
execute if score $msp mg.st matches 1 run function mg:master/window
execute if score $msp mg.st matches 1 if score $mst mg.st matches ..0 run function mg:master/end_round
execute if score $msp mg.st matches 0 if score $mst mg.st matches ..0 run function mg:master/new
execute if score $msp mg.st matches 2 if score $mst mg.st matches ..0 run function mg:master/new
execute store result score $a mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $a mg.st matches ..1 run return run function mg:master/end
execute if score $state mg.st matches 2 unless score $n0 mg.st matches 2.. if score $msr mg.st matches 21.. run return run function mg:master/end
execute if score $state mg.st matches 2 if score $msc mg.st matches 6000.. run function mg:master/end
