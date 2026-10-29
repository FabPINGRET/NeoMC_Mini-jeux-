# Un candidat (@s = joueur listé ; le demandeur porte mg.dlq) : occupé ? (ligne grise non cliquable + raison), sinon numéro et ligne cliquable
function mg:duel/busy
execute if entity @s[tag=mg.mpp] run return run tellraw @a[tag=mg.dlq] [{"text":"  ⚔ ","color":"gray"},{"selector":"@s","color":"gray"},{"text":" — en Mini Party","color":"gray"}]
execute if entity @s[tag=mg.play] run return run tellraw @a[tag=mg.dlq] [{"text":"  ⚔ ","color":"gray"},{"selector":"@s","color":"gray"},{"text":" — en partie","color":"gray"}]
execute if entity @s[tag=mg.out] run return run tellraw @a[tag=mg.dlq] [{"text":"  ⚔ ","color":"gray"},{"selector":"@s","color":"gray"},{"text":" — en partie","color":"gray"}]
execute if entity @s[tag=mg.gtw] run return run tellraw @a[tag=mg.dlq] [{"text":"  ⚔ ","color":"gray"},{"selector":"@s","color":"gray"},{"text":" — dans GTA","color":"gray"}]
execute if entity @s[tag=mg.tvw] run return run tellraw @a[tag=mg.dlq] [{"text":"  ⚔ ","color":"gray"},{"selector":"@s","color":"gray"},{"text":" — dans Terra Nova","color":"gray"}]
execute if entity @s[tag=mg.surv] run return run tellraw @a[tag=mg.dlq] [{"text":"  ⚔ ","color":"gray"},{"selector":"@s","color":"gray"},{"text":" — en survie","color":"gray"}]
execute if entity @s[tag=mg.inplot] run return run tellraw @a[tag=mg.dlq] [{"text":"  ⚔ ","color":"gray"},{"selector":"@s","color":"gray"},{"text":" — sur un plot","color":"gray"}]
execute if entity @s[tag=mg.visit] run return run tellraw @a[tag=mg.dlq] [{"text":"  ⚔ ","color":"gray"},{"selector":"@s","color":"gray"},{"text":" — sur un plot","color":"gray"}]
execute if entity @s[tag=mg.ely] run return run tellraw @a[tag=mg.dlq] [{"text":"  ⚔ ","color":"gray"},{"selector":"@s","color":"gray"},{"text":" — en course d'élytres","color":"gray"}]
execute if entity @s[tag=mg.elyf] run return run tellraw @a[tag=mg.dlq] [{"text":"  ⚔ ","color":"gray"},{"selector":"@s","color":"gray"},{"text":" — en course d'élytres","color":"gray"}]
execute if entity @s[tag=mg.xso] run return run tellraw @a[tag=mg.dlq] [{"text":"  ⚔ ","color":"gray"},{"selector":"@s","color":"gray"},{"text":" — en contre-la-montre","color":"gray"}]
execute if entity @s[tag=mg.pkr] run return run tellraw @a[tag=mg.dlq] [{"text":"  ⚔ ","color":"gray"},{"selector":"@s","color":"gray"},{"text":" — en parcours","color":"gray"}]
execute if entity @s[tag=mg.lk] run return run tellraw @a[tag=mg.dlq] [{"text":"  ⚔ ","color":"gray"},{"selector":"@s","color":"gray"},{"text":" — en kart","color":"gray"}]
execute if entity @s[tag=mg.pvpc] run return run tellraw @a[tag=mg.dlq] [{"text":"  ⚔ ","color":"gray"},{"selector":"@s","color":"gray"},{"text":" — dans l'arène PvP","color":"gray"}]
execute if entity @s[tag=mg.dl] run return run tellraw @a[tag=mg.dlq] [{"text":"  ⚔ ","color":"gray"},{"selector":"@s","color":"gray"},{"text":" — en duel","color":"gray"}]
execute if entity @s[gamemode=spectator] run return run tellraw @a[tag=mg.dlq] [{"text":"  ⚔ ","color":"gray"},{"selector":"@s","color":"gray"},{"text":" — spectateur","color":"gray"}]
execute if entity @s[tag=mg.dlrq] run return run tellraw @a[tag=mg.dlq] [{"text":"  ⚔ ","color":"gray"},{"selector":"@s","color":"gray"},{"text":" — invitation en cours","color":"gray"}]
execute if entity @s[scores={mg.dlto=1..}] run return run tellraw @a[tag=mg.dlq] [{"text":"  ⚔ ","color":"gray"},{"selector":"@s","color":"gray"},{"text":" — invitation en cours","color":"gray"}]
execute if score $dlb mg.st matches 1 run return run tellraw @a[tag=mg.dlq] [{"text":"  ⚔ ","color":"gray"},{"selector":"@s","color":"gray"},{"text":" — occupé","color":"gray"}]
execute unless score @s mg.dlid matches 1.. run function mg:duel/new_id
scoreboard players add $dlc mg.st 1
scoreboard players operation #dll mg.st = @s mg.dlid
scoreboard players add #dll mg.st 1000
execute store result storage mg:duel m.v int 1 run scoreboard players get #dll mg.st
function mg:duel/list_line with storage mg:duel m
