# Kart libre au spawn (chaque tick) : moteur du kart pour les pilotes mg.lk, sur le circuit du spawn
execute as @a[tag=mg.lkz] unless entity @s[x=-1,y=63,z=54,dx=2.99,dy=2.5,dz=2.99] run tag @s remove mg.lkz
execute if score $state mg.st matches 0 as @a[tag=!mg.lk,tag=!mg.lkz,tag=!mg.play,tag=!mg.surv,tag=!mg.inplot,gamemode=adventure,x=-1,y=63,z=54,dx=2.99,dy=2.5,dz=2.99] run function mg:lobkart/enter
scoreboard players add $lko mg.st 1
execute if score $lko mg.st matches 100.. run function mg:lobkart/orphans
execute if score $lko mg.st matches 100.. run scoreboard players set $lko mg.st 0
execute unless entity @a[tag=mg.lk] run return 0
execute unless score $state mg.st matches 0 run return run function mg:lobkart/stop_all
execute as @a[tag=mg.lk,gamemode=creative] run function mg:lobkart/leave
execute as @a[tag=mg.lk,tag=mg.surv] run function mg:lobkart/leave
scoreboard players operation $lkb mg.st = $kbat mg.st
scoreboard players set $kbat mg.st 0
scoreboard players set $klob mg.st 1
function mg:kart/t4/const
execute if score $rp mg.st matches 1 as @e[type=minecraft:block_display,tag=mg.lkart,tag=!mg.rps] at @s run function mg:kart/rp_skin
execute if score $rp mg.st matches 1 as @e[tag=mg.fx,tag=!mg.rps] at @s run function mg:kart/rp_skin
scoreboard players add @a[tag=mg.lk,scores={mg.klp=1..}] mg.klt 1
execute as @a[tag=mg.lk] run function mg:kart/drive
tag @e[tag=mg.kk] remove mg.kk
tag @e[tag=mg.kcamc] remove mg.kcamc
execute as @e[type=minecraft:block_display,tag=mg.kart,tag=!mg.lkart] if score @s mg.ri matches 100.. run tag @s add mg.lkart
scoreboard players add $kph mg.st 1
execute if score $kph mg.st matches 4.. run scoreboard players set $kph mg.st 0
execute if score $kph mg.st matches 0 as @a[tag=mg.lk] run function mg:lobkart/hud
scoreboard players set $klob mg.st 0
scoreboard players operation $kbat mg.st = $lkb mg.st
function mg:kart/const
