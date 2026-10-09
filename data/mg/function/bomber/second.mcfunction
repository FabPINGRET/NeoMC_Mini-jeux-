# Une seconde : barre de destruction, fusées rechargées, joueurs sous le sol ou sortis de la ville ramenés au-dessus
scoreboard players operation $bpct mg.st = $bdes mg.st
scoreboard players set #100 mg.st 100
scoreboard players operation $bpct mg.st *= #100 mg.st
scoreboard players set #btot mg.st 151022
scoreboard players operation $bpct mg.st /= #btot mg.st
execute store result bossbar mg:bomber value run scoreboard players get $bdes mg.st
bossbar set mg:bomber name [{"text":"🏙 Ville détruite : ","color":"red"},{"score":{"name":"$bpct","objective":"mg.st"},"color":"yellow","bold":true},{"text":" %","color":"red"}]
execute as @a[tag=mg.play] at @s if entity @s[y=-64,dy=120] run tp @s 0 171 32400
execute as @a[tag=mg.play] unless entity @s[x=-88,y=-64,z=32312,dx=176,dy=400,dz=176] run tp @s 0 171 32400
execute as @a[tag=mg.play] run item replace entity @s hotbar.8 with minecraft:firework_rocket[custom_data={mg_bomb:1b},fireworks={flight_duration:1},custom_name={"text":"Fusée (illimitée)","color":"gold","italic":false}] 16
execute if score $state mg.st matches 2 if score $bpct mg.st matches 85.. run function mg:bomber/timeout
