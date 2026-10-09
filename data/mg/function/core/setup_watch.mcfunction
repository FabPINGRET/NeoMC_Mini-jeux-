# Surveille la fin de la génération lancée par mg:setup (toutes les 2 s). Généré par tools/setup/gen_setup_watch.py.
scoreboard players add $swt mg.st 1
scoreboard players set $swn mg.st 0
execute if data storage mg:lobby v6 run scoreboard players add $swn mg.st 1
execute if data storage mg:lobby food1 run scoreboard players add $swn mg.st 1
execute if data storage mg:lobby ely1 run scoreboard players add $swn mg.st 1
execute if data storage mg:hall v8 run scoreboard players add $swn mg.st 1
execute if data storage mg:lobby coaster2 run scoreboard players add $swn mg.st 1
execute if data storage mg:setup plot run scoreboard players add $swn mg.st 1
execute if data storage mg:party built run scoreboard players add $swn mg.st 1
execute if data storage mg:kart built if data storage mg:kart built2 if data storage mg:kart built3 run scoreboard players add $swn mg.st 1
execute if data storage mg:dropadv v3 run scoreboard players add $swn mg.st 1
execute if data storage mg:sky built run scoreboard players add $swn mg.st 1
execute if data storage mg:elyrace v2 if data storage mg:elyrace c2v2 run scoreboard players add $swn mg.st 1
execute if score $swn mg.st matches 11.. run return run function mg:core/setup_done
# toutes les 20 s : avancement
scoreboard players operation $swq mg.st = $swt mg.st
scoreboard players set #10 mg.st 10
scoreboard players operation $swq mg.st %= #10 mg.st
execute if score $swq mg.st matches 0 run function mg:core/setup_progress
# 15 min sans tout terminer : on arrête de surveiller et on dit ce qui manque
execute if score $swt mg.st matches 450.. run return run function mg:core/setup_timeout
schedule function mg:core/setup_watch 2s
