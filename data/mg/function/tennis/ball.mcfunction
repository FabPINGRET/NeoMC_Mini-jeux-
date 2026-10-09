# @s : balle (chaque tick) — gravité, déplacement, filet, rebond, sortie, frappe auto du service
scoreboard players remove @s mg.tnvy 16
scoreboard players set $tns0 mg.st 1
execute if score @s mg.tnz matches 0.. run scoreboard players set $tns0 mg.st 2
scoreboard players operation @s mg.tnx += @s mg.tnvx
scoreboard players operation @s mg.tny += @s mg.tnvy
scoreboard players operation @s mg.tnz += @s mg.tnvz
scoreboard players set $tns1 mg.st 1
execute if score @s mg.tnz matches 0.. run scoreboard players set $tns1 mg.st 2
execute if entity @s[tag=mg.tnlive] unless score $tns0 mg.st = $tns1 mg.st if score @s mg.tny matches ..66100 if score @s mg.tnx matches -7500..7500 run function mg:tennis/net
execute if score @s mg.tny matches ..65100 if score @s mg.tnvy matches ..-1 run function mg:tennis/bounce
execute if entity @s[tag=mg.tnlive] unless score @s mg.tnx matches -13000..13000 run function mg:tennis/dead
execute if entity @s[tag=mg.tnlive] unless score @s mg.tnz matches -19500..19500 run function mg:tennis/dead
execute if entity @s[tag=mg.tntoss] if score @s mg.tnvy matches ..0 run function mg:tennis/serve_hit
scoreboard players operation $tnq mg.st = @s mg.tnx
scoreboard players operation $tnq mg.st += $tncx mg.st
execute store result entity @s Pos[0] double 0.001 run scoreboard players get $tnq mg.st
execute store result entity @s Pos[1] double 0.001 run scoreboard players get @s mg.tny
scoreboard players operation $tnq mg.st = @s mg.tnz
scoreboard players add $tnq mg.st 35400500
execute store result entity @s Pos[2] double 0.001 run scoreboard players get $tnq mg.st
execute at @s run particle minecraft:dust{color:[0.85,1.0,0.25],scale:0.7} ~ ~ ~ 0 0 0 0 1
