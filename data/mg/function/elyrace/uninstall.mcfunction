# Désinstallation de la Course d'élytres (appelé par mg:desinstaller)
# pas de build_abort ici : il appelle core/forceloads, qui réactiverait tous les chargements forcés que desinstaller vient de retirer
schedule clear mg:elyrace/build
schedule clear mg:elyrace/build_next
schedule clear mg:elyrace/c1/build_wait
schedule clear mg:elyrace/c2/build_wait
schedule clear mg:elyrace/c1/clear_1
schedule clear mg:elyrace/c1/clear_2
schedule clear mg:elyrace/c1/clear_3
schedule clear mg:elyrace/c1/clear_4
schedule clear mg:elyrace/c1/clear_5
schedule clear mg:elyrace/c1/clear_6
schedule clear mg:elyrace/c1/clear_7
schedule clear mg:elyrace/c1/clear_8
schedule clear mg:elyrace/c1/clear_9
schedule clear mg:elyrace/c1/clear_10
schedule clear mg:elyrace/c1/clear_11
schedule clear mg:elyrace/c2/clear_1
schedule clear mg:elyrace/c2/clear_2
schedule clear mg:elyrace/c2/clear_3
schedule clear mg:elyrace/c2/clear_4
schedule clear mg:elyrace/c2/clear_5
schedule clear mg:elyrace/c2/clear_6
schedule clear mg:elyrace/c2/clear_7
schedule clear mg:elyrace/c2/clear_8
schedule clear mg:elyrace/c2/clear_9
schedule clear mg:elyrace/c2/clear_10
schedule clear mg:elyrace/c2/clear_11
schedule clear mg:elyrace/c2/clear_12
# ancien chemin (avant 2a : construction en un seul module, sans c<N>/) : un schedule d'une version précédente peut survivre
schedule clear mg:elyrace/build_wait
function mg:elyrace/forget
clear @a minecraft:elytra[minecraft:custom_data~{mg_elyr:1b}]
clear @a minecraft:firework_rocket[minecraft:custom_data~{mg_elyr:1b}]
tag @a remove mg.xw1
tag @a remove mg.xtp
# contre-la-montre solo en cours : tags (solo, pause d'avant ; le tag mg.spectate lui-même est retiré par desinstaller) et gel
execute as @a[tag=mg.xso] run function mg:core/unfreeze
tag @a remove mg.xso
tag @a remove mg.xsp0
advancement revoke @a only mg:elyrace_wall
scoreboard objectives remove mg.xa
scoreboard objectives remove mg.xo
scoreboard objectives remove mg.xc
scoreboard objectives remove mg.xh
scoreboard objectives remove mg.xp
scoreboard objectives remove mg.xx
scoreboard objectives remove mg.xg
scoreboard objectives remove mg.xn
scoreboard objectives remove mg.xl
scoreboard objectives remove mg.xk
scoreboard objectives remove mg.xf
scoreboard objectives remove mg.xb1
scoreboard objectives remove mg.xb2
scoreboard objectives remove mg.xb3
# parcours et état du solo par joueur, trigger du solo, records par parcours (objectifs et détenteur figé dans le hall)
scoreboard objectives remove mg.xcr
scoreboard objectives remove mg.xph
scoreboard objectives remove mg.xst
scoreboard objectives remove mg.xse
scoreboard objectives remove mg.xsl
scoreboard objectives remove mg.xs
scoreboard objectives remove mg.xr1
scoreboard objectives remove mg.xr2
data remove storage mg:hall e.xr1
data remove storage mg:hall e.xr2
