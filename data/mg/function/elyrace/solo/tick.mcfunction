# Tick des contre-la-montre solo (core/tick, si au moins un joueur porte mg.xso) : deux passes, voir solo_run.py
execute as @a[tag=mg.xso] run function mg:elyrace/solo/seen
execute as @e[type=player,tag=mg.xso] run function mg:elyrace/solo/step
