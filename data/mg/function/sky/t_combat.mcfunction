# Mode 2 : sonnés, recharge des charges de vent, détonation de proximité des charges
scoreboard players remove @a[scores={mg.skst=1..}] mg.skst 1
execute as @a[tag=mg.skstun,scores={mg.skst=..0}] run function mg:sky/unstun
scoreboard players add $skwt mg.st 1
execute if score $skwt mg.st matches 300.. run function mg:sky/wc_refill
scoreboard players set $skws mg.st 300
scoreboard players operation $skws mg.st -= $skwt mg.st
scoreboard players operation $skws mg.st /= #20 mg.st
execute as @e[type=minecraft:wind_charge,x=-225,y=60,z=27570,dx=450,dy=240,dz=860] at @s run function mg:sky/wc_check
