# Pas de mot validé → tentative de lecture du livre, sinon mot au hasard
function mg:tel/read_book
execute if entity @s[tag=mg.tdone] run return 0
function mg:bb/pick_word
data modify storage mg:tel tmp set from storage mg:bb word
execute store result storage mg:tel p.c int 1 run scoreboard players get @s mg.tc
data modify storage mg:tel p.k set value "s0"
function mg:tel/store with storage mg:tel p
tellraw @s [{"text":"⏱ Temps écoulé : mot tiré au hasard → ","color":"gray"},{"nbt":"tmp","storage":"mg:tel","color":"white"}]
