# Pas de devinette validée → tentative de lecture du livre, sinon « ??? »
function mg:tel/read_book
execute if entity @s[tag=mg.tdone] run return 0
data modify storage mg:tel tmp set value "???"
execute store result storage mg:tel p.c int 1 run scoreboard players get @s mg.tc
execute if score $tp mg.st matches 2 run data modify storage mg:tel p.k set value "s2"
execute if score $tp mg.st matches 4 run data modify storage mg:tel p.k set value "s4"
function mg:tel/store with storage mg:tel p
