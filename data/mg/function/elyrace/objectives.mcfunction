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
scoreboard objectives add mg.xq1 dummy
scoreboard objectives add mg.xq2 dummy
scoreboard objectives add mg.xq3 dummy
scoreboard objectives add mg.xu dummy
scoreboard objectives add mg.xft dummy
# hors de OBJECTIVES (prepare les remet à zéro à chaque départ) : parcours du joueur et état du solo (par joueur), trigger du solo, records par parcours
scoreboard objectives add mg.xcr dummy
scoreboard objectives add mg.xph dummy
scoreboard objectives add mg.xst dummy
scoreboard objectives add mg.xse dummy
scoreboard objectives add mg.xsl dummy
scoreboard objectives add mg.xs trigger
scoreboard objectives add mg.xr1 dummy
scoreboard objectives add mg.xr2 dummy
# constantes de elyrace/time, de speed, du bonus d'or (#kgb) et du HUD du solo (plus posées par prepare : le solo n'y passe pas)
scoreboard players set #k5 mg.st 5
scoreboard players set #k10 mg.st 10
scoreboard players set #k20 mg.st 20
scoreboard players set #k100 mg.st 100
scoreboard players set #krel mg.st 30
scoreboard players set #kgb mg.st 40
# purge des anciens drapeaux du solo de la 2c (le solo ne passe plus par $state : $xs et $xse n'existent plus)
scoreboard players reset $xs mg.st
scoreboard players reset $xse mg.st
