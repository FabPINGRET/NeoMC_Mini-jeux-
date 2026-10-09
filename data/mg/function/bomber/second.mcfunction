# Une seconde : barre de destruction, joueurs retenus au-dessus de la ville
scoreboard players operation $bpct mg.st = $bdes mg.st
scoreboard players set #100 mg.st 100
scoreboard players operation $bpct mg.st *= #100 mg.st
scoreboard players set #btot mg.st 161321
scoreboard players operation $bpct mg.st /= #btot mg.st
execute store result bossbar mg:bomber value run scoreboard players get $bdes mg.st
bossbar set mg:bomber name [{"text":"🏙 Ville détruite : ","color":"red"},{"score":{"name":"$bpct","objective":"mg.st"},"color":"yellow","bold":true},{"text":" %","color":"red"}]
execute as @a[tag=mg.play] at @s if entity @s[y=0,dy=169] run tp @s 0 171 32400
execute if score $state mg.st matches 2 if score $bpct mg.st matches 85.. run function mg:bomber/timeout
