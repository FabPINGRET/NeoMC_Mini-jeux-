scoreboard players set despawned_10 bool 0

execute unless score monstervatory Value matches 1 positioned -270 39 216 run function summon:diretroll
execute positioned -269 41 247 run function summon:diretroll
execute unless score monstervatory Value matches 1 positioned -221 50 253 run function summon:diretroll
execute positioned -193 42 248 run function summon:diretroll
execute unless score monstervatory Value matches 1 positioned -219 38 221 run function summon:diretroll
execute positioned -245 49 174 run function summon:diretroll
execute unless score monstervatory Value matches 1 positioned -244 57 196 run function summon:diretroll
execute positioned -232 58 239 run function summon:diretroll

execute unless score monstervatory Value matches 1 positioned -255 52 210 run function summon:abnormazoid/smallhead_diretroll

#execute unless score monstervatory Value matches 1 positioned x y z run function summon:monster
#execute positioned x y z run function summon:monster

return 1
