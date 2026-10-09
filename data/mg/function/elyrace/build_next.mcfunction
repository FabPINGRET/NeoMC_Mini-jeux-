# Lance la construction du premier parcours pas encore construit (drapeau absent) ; rien à faire quand tous le sont
execute if data storage mg:elyrace v2 if data storage mg:elyrace c2v2 run return 0
# une construction tourne déjà ($xbk = tranche en cours, 0 sinon : posé par build_start, remis à 0 par la dernière tranche,
# build_fail et build_abort ; core/load le remet à 0 au chargement) : la dernière tranche rappellera build_next
execute if score $xbk mg.st matches 1.. run return 0
# pas pendant une partie ni un solo : on réessaie dans une minute (build_abort libérerait la zone de départ chargée par fl_add)
execute unless score $state mg.st matches 0 run return run schedule function mg:elyrace/build_next 60s
execute if entity @a[tag=mg.xso] run return run schedule function mg:elyrace/build_next 60s
execute unless data storage mg:elyrace v2 run return run function mg:elyrace/c1/build_start
execute unless data storage mg:elyrace c2v2 run return run function mg:elyrace/c2/build_start
