# TNT Tag — début de partie
scoreboard players set $c20 mg.st 20
scoreboard players set $c100 mg.st 100
scoreboard players set $mx mg.st 600
scoreboard players set $ttb mg.st 200
execute if score $ar mg.st matches 1.. run function mg:var/mode/tnttag_go
scoreboard players set @a[tag=mg.play] mg.cd 0
effect give @a[tag=mg.play] minecraft:resistance infinite 4 true
effect give @a[tag=mg.play] minecraft:saturation infinite 0 true
tellraw @a[tag=mg.play] [{"text":"✹ TNT TAG ! ","color":"red","bold":true},{"text":"Un joueur a la TNT sur la tête : frappe un adversaire pour lui passer la bombe ! À la fin du compte à rebours, elle explose et élimine son porteur. Dernier survivant = gagnant !","color":"gray"}]
function mg:tnttag/new_round
