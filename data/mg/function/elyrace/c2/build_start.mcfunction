# Démarre la construction du parcours 2 : tranche 1 chargée de force, la suite est enchaînée par build_wait
scoreboard players set $xbk mg.st 1
scoreboard players set $xbw mg.st 0
scoreboard players set $xcp mg.st 0
forceload add -16 29440 79 29759
schedule function mg:elyrace/c2/build_wait 20t
