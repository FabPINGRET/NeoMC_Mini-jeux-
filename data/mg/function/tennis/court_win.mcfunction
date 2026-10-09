# @s : marqueur — le côté $tnw remporte le match de ce court (fin après la pause)
tag @s add mg.tndone
scoreboard players operation @s mg.tnb = $tnw mg.st
execute as @a[tag=mg.tnk] if score @s mg.tns = $tnw mg.st run tag @s add mg.tnwin
tag @e[tag=mg.tnws] remove mg.tnws
tag @e[tag=mg.tnls] remove mg.tnls
execute as @e[tag=mg.tnk,scores={mg.tns=1..2}] if score @s mg.tns = $tnw mg.st run tag @s add mg.tnws
execute as @e[tag=mg.tnk,scores={mg.tns=1..2}] unless score @s mg.tns = $tnw mg.st run tag @s add mg.tnls
tellraw @a [{"text":"🎾 Court ","color":"gold"},{"score":{"name":"@s","objective":"mg.tnc"},"color":"gold"},{"text":" : ","color":"gold"},{"selector":"@e[tag=mg.tnws]","color":"yellow","bold":true},{"text":" bat ","color":"gray"},{"selector":"@e[tag=mg.tnls]","color":"gray"},{"text":" (","color":"gray"},{"score":{"name":"@s","objective":"mg.tng1"},"color":"aqua"},{"text":"-","color":"gray"},{"score":{"name":"@s","objective":"mg.tng2"},"color":"red"},{"text":")","color":"gray"}]
title @a[tag=mg.tnk,tag=mg.tnws] title {"text":"Jeu, set et match !","color":"gold","bold":true}
title @a[tag=mg.tnk,tag=mg.tnls] title {"text":"Match perdu","color":"gray"}
execute as @a[tag=mg.tnk,tag=mg.tnws] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.8 1.2
tag @e[tag=mg.tnws] remove mg.tnws
tag @e[tag=mg.tnls] remove mg.tnls
