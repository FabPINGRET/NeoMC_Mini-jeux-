# 🔴 1, 2, 3 Soleil — tick
scoreboard players add $sqc mg.st 1
scoreboard players remove $sqt mg.st 1
execute store result bossbar mg:soleil value run scoreboard players get $sqc mg.st
execute as @a[tag=mg.play,tag=!mg.sqf,x=-21,y=55,z=37080,dx=42,dy=30,dz=18] run function mg:soleil/finish
execute if score $sqp mg.st matches 0 if score $sqt mg.st matches ..0 run function mg:soleil/red
execute if score $sqp mg.st matches 1 if score $sqt mg.st matches ..0 run function mg:soleil/watch
execute if score $sqp mg.st matches 2 as @a[tag=mg.play,tag=!mg.sqf] run function mg:soleil/check
execute if score $sqp mg.st matches 2 if score $sqt mg.st matches ..0 run function mg:soleil/green
execute as @a[tag=mg.play,tag=!mg.sqf] unless entity @s[x=-23,y=55,z=36997,dx=46,dy=30,dz=102] run function mg:soleil/place
scoreboard players operation $q mg.st = $sqc mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $q mg.st %= #20 mg.st
execute if score $q mg.st matches 0 run function mg:soleil/second
execute store result score $a mg.st if entity @a[tag=mg.play,tag=!mg.sqf]
execute if score $state mg.st matches 2 if score $a mg.st matches 0 run return run function mg:soleil/end
execute if score $state mg.st matches 2 if score $sqc mg.st matches 1800.. run function mg:soleil/timeout
