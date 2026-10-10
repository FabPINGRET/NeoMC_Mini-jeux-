# Feu rouge : la poupée se retourne, 0,5 s de grâce
scoreboard players set $sqp mg.st 1
scoreboard players set $sqt mg.st 10
function mg:soleil/turn {yaw:180}
title @a[tag=mg.play] times 0 25 5
title @a[tag=mg.play] title {"text":"SOLEIL !","color":"red","bold":true}
title @a[tag=mg.play] subtitle {"text":"ne bouge plus","color":"gray"}
execute as @a[tag=mg.play] at @s run playsound minecraft:entity.elder_guardian.curse master @s ~ ~ ~ 0.4 1.6
