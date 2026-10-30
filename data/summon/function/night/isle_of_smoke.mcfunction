scoreboard players set despawned_19 bool 0

execute unless score monstervatory Value matches 1 positioned 9993 49 174 run function summon:dead_fairy
execute positioned 9956 33 228 run function summon:dead_fairy
execute unless score monstervatory Value matches 1 positioned 9988 57 250 run function summon:dead_fairy
execute positioned 10025 38 226 run function summon:dead_fairy
#Zoid
execute unless score monstervatory Value matches 1 positioned 9981 44 246 run function summon:abnormazoid/wings_ripped_off_fairy

#execute unless score monstervatory Value matches 1 positioned x y z run function summon:monster
#execute positioned x y z run function summon:monster

return 1
