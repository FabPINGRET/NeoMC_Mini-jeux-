# 🚗 Autos tamponneuses — tick
scoreboard players add $att mg.st 1
scoreboard players set #m1 mg.st -1
execute store result bossbar mg:autotamp value run scoreboard players get $att mg.st
execute as @e[type=#mg:at_boats,tag=mg.atb] run function mg:autotamp/speed
execute as @e[type=#mg:at_boats,tag=mg.atb] unless score @s mg.atc matches 1.. at @s run function mg:autotamp/bump
execute as @a[tag=mg.play] unless predicate mg:coaster_riding run function mg:autotamp/remount
execute as @e[type=#mg:at_boats,tag=mg.atb] unless predicate mg:coaster_has_rider run kill @s
execute store result score $a mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $a mg.st matches ..1 run return run function mg:autotamp/end
execute if score $state mg.st matches 2 if score $att mg.st matches 3600.. run function mg:autotamp/end
