# Nouvelle bombe : un survivant au hasard + minuteur selon le nombre de survivants
execute store result score $al mg.st if entity @a[tag=mg.play]
execute if score $al mg.st matches 0 run return 0
tag @a remove mg.bomb
tag @r[tag=mg.play] add mg.bomb
scoreboard players remove $al mg.st 1
scoreboard players operation $tt mg.st = $al mg.st
scoreboard players operation $tt mg.st *= $c100 mg.st
scoreboard players add $tt mg.st 200
scoreboard players operation $tt mg.st < $mx mg.st
scoreboard players set @a[tag=mg.play] mg.cd 0
execute as @a[tag=mg.bomb] run function mg:tnttag/equip
