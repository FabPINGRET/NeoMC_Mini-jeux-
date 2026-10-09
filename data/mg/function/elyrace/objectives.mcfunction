# Objectifs de la Course d'élytres (généré par tools/elyrace/gen_elyrace.py ; appelé par mg:core/load)
scoreboard objectives add mg.xa dummy [{"text":"🪽 COURSE D'ÉLYTRES — anneaux","color":"aqua"}]
scoreboard objectives add mg.xo dummy
scoreboard objectives add mg.xc dummy
scoreboard objectives add mg.xh dummy
scoreboard objectives add mg.xp dummy
scoreboard objectives add mg.xx dummy
scoreboard objectives add mg.xg dummy
scoreboard objectives add mg.xn dummy
scoreboard objectives add mg.xl dummy
scoreboard objectives add mg.xk dummy
scoreboard objectives add mg.xf dummy
scoreboard objectives add mg.xb1 dummy
scoreboard objectives add mg.xb2 dummy
scoreboard objectives add mg.xb3 dummy
# hors de OBJECTIVES (prepare les remet à zéro à chaque départ) : trigger du contre-la-montre solo, records par parcours
scoreboard objectives add mg.xs trigger
scoreboard objectives add mg.xr1 dummy
scoreboard objectives add mg.xr2 dummy
# constantes de elyrace/time ; $xs (solo en cours) ne survit pas à un rechargement hors partie
scoreboard players set #k5 mg.st 5
scoreboard players set #k20 mg.st 20
execute unless score $state mg.st matches 1.. run scoreboard players set $xs mg.st 0
