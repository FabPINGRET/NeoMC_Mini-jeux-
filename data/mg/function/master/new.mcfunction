# Nouvel ordre ($mso = ordre, $msv = 1 vrai / 0 piège, délai $msw)
scoreboard players add $msr mg.st 1
execute store result score $mso mg.st run random value 1..10
scoreboard players set $msv mg.st 1
execute store result score $r mg.st run random value 1..100
execute if score $mso mg.st matches 1..3 if score $r mg.st matches ..35 run scoreboard players set $msv mg.st 0
scoreboard players set $msw mg.st 60
scoreboard players operation $r mg.st = $msr mg.st
scoreboard players operation $r mg.st *= #2 mg.st
scoreboard players operation $msw mg.st -= $r mg.st
execute if score $msw mg.st matches ..19 run scoreboard players set $msw mg.st 20
scoreboard players operation $mst mg.st = $msw mg.st
scoreboard players set $msp mg.st 1
tag @a[tag=mg.play] remove mg.mso
tag @a[tag=mg.play] remove mg.msf
execute store result storage mg:ms t.d int 1 run scoreboard players get $msw mg.st
scoreboard players set $msx mg.st 0
execute store result score $r mg.st run random value 1..100
execute if score $n0 mg.st matches 2.. if score $msr mg.st matches 3.. if score $r mg.st matches ..12 run scoreboard players set $msx mg.st 1
execute as @a[tag=mg.play] run scoreboard players operation @s mg.mo = $mso mg.st
execute as @a[tag=mg.play] run scoreboard players operation @s mg.mv = $msv mg.st
execute if score $msx mg.st matches 1 as @a[tag=mg.play] run function mg:master/roll
execute as @a[tag=mg.play] at @s run function mg:master/show
