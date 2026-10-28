# Chaque tick (monde des mini-jeux) : horloge du Filon, session
execute unless score $setup mg.st matches 1 run return 0
scoreboard players add $fnq mg.st 1
execute if score $fnq mg.st matches 20.. run function mg:filon/clock
execute if score $fnq mg.st matches 20.. run scoreboard players set $fnq mg.st 0
execute unless score $fnw mg.st matches 1 if entity @a[tag=mg.fnw] run function mg:filon/session_start
execute if score $fnw mg.st matches 1 unless entity @a[tag=mg.fnw] run function mg:filon/session_end
execute if score $fnw mg.st matches 1 run function mg:filon/tick
