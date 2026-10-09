# @s : marqueur d'un court (chaque tick)
scoreboard players operation $tnk mg.st = @s mg.tnc
function mg:tennis/tagk
execute if score @s mg.tnph matches 4 run return 0
execute store result score $tnn1 mg.st if entity @e[tag=mg.tnk,scores={mg.tns=1}]
execute store result score $tnn2 mg.st if entity @e[tag=mg.tnk,scores={mg.tns=2}]
execute if score $tnn1 mg.st matches 0 if score $tnn2 mg.st matches 0 run return run function mg:tennis/court_end
execute if score $tnn1 mg.st matches 0 run scoreboard players set $tnw mg.st 2
execute if score $tnn2 mg.st matches 0 run scoreboard players set $tnw mg.st 1
execute if score $tnn1 mg.st matches 0 run return run function mg:tennis/forfeit
execute if score $tnn2 mg.st matches 0 run return run function mg:tennis/forfeit
execute if score @s mg.tnph matches 0 run function mg:tennis/phase0
execute if score @s mg.tnph matches 1..3 as @e[type=minecraft:item_display,tag=mg.tnball,tag=mg.tnk] run function mg:tennis/ball
execute if score @s mg.tnph matches 1..2 unless entity @e[type=minecraft:item_display,tag=mg.tnball,tag=mg.tnk,limit=1] run function mg:tennis/point_setup
execute if score @s mg.tnph matches 3 run function mg:tennis/phase3
execute as @e[type=minecraft:mannequin,tag=mg.tnrob,tag=mg.tnk] at @s run function mg:tennis/robot
execute if score $tnab mg.st matches 0 unless score @s mg.tnph matches 0 run title @a[tag=mg.tnk] actionbar [{"text":"🟦 ","color":"aqua"},{"selector":"@e[tag=mg.tnk,scores={mg.tns=1}]","color":"aqua"},{"text":"  ","color":"gray"},{"nbt":"data.a","entity":"@e[type=minecraft:marker,tag=mg.tncm,tag=mg.tnk,limit=1]","color":"white","bold":true},{"text":" — ","color":"gray"},{"nbt":"data.b","entity":"@e[type=minecraft:marker,tag=mg.tncm,tag=mg.tnk,limit=1]","color":"white","bold":true},{"text":"  ","color":"gray"},{"selector":"@e[tag=mg.tnk,scores={mg.tns=2}]","color":"red"},{"text":" 🟥","color":"red"},{"text":"   jeux ","color":"gray"},{"nbt":"data.ga","entity":"@e[type=minecraft:marker,tag=mg.tncm,tag=mg.tnk,limit=1]","color":"aqua"},{"text":"-","color":"gray"},{"nbt":"data.gb","entity":"@e[type=minecraft:marker,tag=mg.tncm,tag=mg.tnk,limit=1]","color":"red"}]
execute if score $tnab mg.st matches 0 if score @s mg.tnph matches 0 run title @a[tag=mg.tnk,tag=!mg.tnsrv] actionbar [{"text":"🟦 ","color":"aqua"},{"selector":"@e[tag=mg.tnk,scores={mg.tns=1}]","color":"aqua"},{"text":"  ","color":"gray"},{"nbt":"data.a","entity":"@e[type=minecraft:marker,tag=mg.tncm,tag=mg.tnk,limit=1]","color":"white","bold":true},{"text":" — ","color":"gray"},{"nbt":"data.b","entity":"@e[type=minecraft:marker,tag=mg.tncm,tag=mg.tnk,limit=1]","color":"white","bold":true},{"text":"  ","color":"gray"},{"selector":"@e[tag=mg.tnk,scores={mg.tns=2}]","color":"red"},{"text":" 🟥","color":"red"},{"text":"   jeux ","color":"gray"},{"nbt":"data.ga","entity":"@e[type=minecraft:marker,tag=mg.tncm,tag=mg.tnk,limit=1]","color":"aqua"},{"text":"-","color":"gray"},{"nbt":"data.gb","entity":"@e[type=minecraft:marker,tag=mg.tncm,tag=mg.tnk,limit=1]","color":"red"}]
execute if score $tnab mg.st matches 0 if score @s mg.tnph matches 0 run title @a[tag=mg.tnk,tag=mg.tnsrv] actionbar {"text":"🎾 À toi de servir : clic droit avec la raquette (service auto dans 10 s)","color":"yellow"}
