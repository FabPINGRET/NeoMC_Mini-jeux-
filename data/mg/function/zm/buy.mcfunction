# @s = interaction cliquée
execute on target run tag @s add mg.zbuyer
data remove entity @s interaction
execute unless entity @a[tag=mg.zbuyer,tag=mg.play,tag=!mg.zdead] run return run tag @a remove mg.zbuyer
execute if entity @s[tag=mg.zb1] run scoreboard players set $zc mg.st 750
execute if entity @s[tag=mg.zb1] if function mg:zm/pay run function mg:zm/door_1
execute if entity @s[tag=mg.zb2] run scoreboard players set $zc mg.st 750
execute if entity @s[tag=mg.zb2] if function mg:zm/pay run function mg:zm/door_2
execute if entity @s[tag=mg.zb3] run scoreboard players set $zc mg.st 1000
execute if entity @s[tag=mg.zb3] if function mg:zm/pay run function mg:zm/door_3
execute if entity @s[tag=mg.zb4] run scoreboard players set $zc mg.st 1000
execute if entity @s[tag=mg.zb4] if function mg:zm/pay run function mg:zm/door_4
execute if entity @s[tag=mg.zb11] run scoreboard players set $zc mg.st 500
execute if entity @s[tag=mg.zb11] if function mg:zm/pay run function mg:zm/buy_gun {n:4}
execute if entity @s[tag=mg.zb12] run scoreboard players set $zc mg.st 500
execute if entity @s[tag=mg.zb12] if function mg:zm/pay run function mg:zm/buy_gun {n:3}
execute if entity @s[tag=mg.zb13] run scoreboard players set $zc mg.st 1000
execute if entity @s[tag=mg.zb13] if function mg:zm/pay run function mg:zm/buy_gun {n:2}
execute if entity @s[tag=mg.zb14] run scoreboard players set $zc mg.st 1500
execute if entity @s[tag=mg.zb14] if function mg:zm/pay run function mg:zm/buy_gun {n:5}
execute if entity @s[tag=mg.zb15] run scoreboard players set $zc mg.st 1000
execute if entity @s[tag=mg.zb15] if function mg:zm/pay run function mg:zm/buy_gun {n:11}
execute if entity @s[tag=mg.zb23] if entity @a[tag=mg.zbuyer,tag=mg.zqr] run return run function mg:zm/already
execute if entity @s[tag=mg.zb23] run scoreboard players set $zc mg.st 1500
execute if entity @s[tag=mg.zb23] if function mg:zm/pay as @a[tag=mg.zbuyer] run function mg:zm/perk_qr
execute if entity @s[tag=mg.zb24] if entity @a[tag=mg.zbuyer,tag=mg.zdbl] run return run function mg:zm/already
execute if entity @s[tag=mg.zb24] run scoreboard players set $zc mg.st 2000
execute if entity @s[tag=mg.zb24] if function mg:zm/pay as @a[tag=mg.zbuyer] run function mg:zm/perk_dt
execute if entity @s[tag=mg.zb25] if entity @a[tag=mg.zbuyer,tag=mg.zst] run return run function mg:zm/already
execute if entity @s[tag=mg.zb25] run scoreboard players set $zc mg.st 2000
execute if entity @s[tag=mg.zb25] if function mg:zm/pay as @a[tag=mg.zbuyer] run function mg:zm/perk_st
execute if entity @s[tag=mg.zb26] if entity @a[tag=mg.zbuyer,tag=mg.zmu] run return run function mg:zm/already
execute if entity @s[tag=mg.zb26] run scoreboard players set $zc mg.st 4000
execute if entity @s[tag=mg.zb26] if function mg:zm/pay as @a[tag=mg.zbuyer] run function mg:zm/perk_mu
execute if entity @s[tag=mg.zb27] as @a[tag=mg.zbuyer] unless items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] run return run function mg:zm/pap_no
execute if entity @s[tag=mg.zb27] as @a[tag=mg.zbuyer] if items entity @s weapon.mainhand *[custom_data~{pap:1b}] run return run function mg:zm/pap_no
execute if entity @s[tag=mg.zb27] run scoreboard players set $zc mg.st 3000
execute if entity @s[tag=mg.zb27] if function mg:zm/pay as @a[tag=mg.zbuyer] run function mg:zm/pap
execute if entity @s[tag=mg.zb20] run scoreboard players set $zc mg.st 950
execute if entity @s[tag=mg.zb20] if score $zfs mg.st matches 1.. run scoreboard players set $zc mg.st 10
execute if entity @s[tag=mg.zb20] if function mg:zm/pay run function mg:zm/box
execute if entity @s[tag=mg.zb21] if entity @a[tag=mg.zbuyer,tag=mg.zjug] run return run function mg:zm/already
execute if entity @s[tag=mg.zb21] run scoreboard players set $zc mg.st 2500
execute if entity @s[tag=mg.zb21] if function mg:zm/pay as @a[tag=mg.zbuyer] run function mg:zm/jug
execute if entity @s[tag=mg.zb22] if entity @a[tag=mg.zbuyer,tag=mg.zsc] run return run function mg:zm/already
execute if entity @s[tag=mg.zb22] run scoreboard players set $zc mg.st 3000
execute if entity @s[tag=mg.zb22] if function mg:zm/pay as @a[tag=mg.zbuyer] run function mg:zm/cola
tag @a remove mg.zbuyer
