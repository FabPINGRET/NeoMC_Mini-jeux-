#init clone
execute positioned -11528 137 260 positioned ~ ~ ~ run clone ~ ~ ~ ~4 ~4 ~4 ~ ~-50 ~

#execute positioned -11528 87 260 positioned ~ ~ ~ run clone ~ ~ ~ ~ ~4 ~ ~ ~50 ~

#rotate clones
execute positioned -11528 87 260 positioned ~ ~ ~ run clone ~ ~ ~ ~ ~4 ~ ~4 ~50 ~
execute positioned -11528 87 260 positioned ~4 ~ ~ run clone ~ ~ ~ ~ ~4 ~ ~ ~50 ~4
execute positioned -11528 87 260 positioned ~4 ~ ~4 run clone ~ ~ ~ ~ ~4 ~ ~-4 ~50 ~
execute positioned -11528 87 260 positioned ~ ~ ~4 run clone ~ ~ ~ ~ ~4 ~ ~ ~50 ~-4 

execute positioned -11528 87 260 positioned ~1 ~ ~ run clone ~ ~ ~ ~ ~4 ~ ~3 ~50 ~1
execute positioned -11528 87 260 positioned ~4 ~ ~1 run clone ~ ~ ~ ~ ~4 ~ ~-1 ~50 ~3
execute positioned -11528 87 260 positioned ~3 ~ ~4 run clone ~ ~ ~ ~ ~4 ~ ~-3 ~50 ~-1
execute positioned -11528 87 260 positioned ~ ~ ~3 run clone ~ ~ ~ ~ ~4 ~ ~1 ~50 ~-3

execute positioned -11528 87 260 positioned ~ ~ ~1 run clone ~ ~ ~ ~ ~4 ~ ~3 ~50 ~-1
execute positioned -11528 87 260 positioned ~3 ~ ~ run clone ~ ~ ~ ~ ~4 ~ ~1 ~50 ~3
execute positioned -11528 87 260 positioned ~4 ~ ~3 run clone ~ ~ ~ ~ ~4 ~ ~-3 ~50 ~1
execute positioned -11528 87 260 positioned ~1 ~ ~4 run clone ~ ~ ~ ~ ~4 ~ ~-1 ~50 ~-3

execute positioned -11528 87 260 positioned ~2 ~ ~ run clone ~ ~ ~ ~ ~4 ~ ~2 ~50 ~2
execute positioned -11528 87 260 positioned ~4 ~ ~2 run clone ~ ~ ~ ~ ~4 ~ ~-2 ~50 ~2
execute positioned -11528 87 260 positioned ~2 ~ ~4 run clone ~ ~ ~ ~ ~4 ~ ~-2 ~50 ~-2
execute positioned -11528 87 260 positioned ~ ~ ~2 run clone ~ ~ ~ ~ ~4 ~ ~2 ~50 ~-2

execute positioned -11528 87 260 positioned ~1 ~ ~1 run clone ~ ~ ~ ~ ~4 ~ ~2 ~50 ~
execute positioned -11528 87 260 positioned ~3 ~ ~1 run clone ~ ~ ~ ~ ~4 ~ ~ ~50 ~2
execute positioned -11528 87 260 positioned ~3 ~ ~3 run clone ~ ~ ~ ~ ~4 ~ ~-2 ~50 ~
execute positioned -11528 87 260 positioned ~1 ~ ~3 run clone ~ ~ ~ ~ ~4 ~ ~ ~50 ~-2

execute positioned -11528 87 260 positioned ~2 ~ ~1 run clone ~ ~ ~ ~ ~4 ~ ~1 ~50 ~1
execute positioned -11528 87 260 positioned ~3 ~ ~2 run clone ~ ~ ~ ~ ~4 ~ ~-1 ~50 ~1
execute positioned -11528 87 260 positioned ~2 ~ ~3 run clone ~ ~ ~ ~ ~4 ~ ~-1 ~50 ~-1
execute positioned -11528 87 260 positioned ~1 ~ ~2 run clone ~ ~ ~ ~ ~4 ~ ~1 ~50 ~-1

function dungeon:10/shape/3/shadow
