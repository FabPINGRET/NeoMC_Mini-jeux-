# Élytra — nettoyage (appelé par core/return_lobby)
clear @a *[minecraft:custom_data~{mg_sky:1b}]
effect clear @a[scores={mg.skl=1..}] minecraft:levitation
kill @e[tag=mg.sky]
kill @e[type=minecraft:wind_charge,x=-225,y=0,z=27570,dx=450,dy=320,dz=1600]
tag @a remove mg.skf
tag @a remove mg.skstun
tag @a remove mg.skak
tag @a remove mg.skv
tag @a remove mg.skw
scoreboard players reset * mg.skr
scoreboard players reset * mg.sks
scoreboard players reset * mg.skg
scoreboard players reset * mg.skst
scoreboard players reset * mg.skl
scoreboard players reset * mg.sko
advancement revoke @a only mg:sky/hurt
schedule clear mg:sky/pad_wait
function mg:sky/pad_fl_off
