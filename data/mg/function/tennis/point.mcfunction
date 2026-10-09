# @s : marqueur — point pour le côté $tnw ($tnwhy = raison)
tag @e[type=minecraft:item_display,tag=mg.tnball,tag=mg.tnk] remove mg.tnlive
tag @e[type=minecraft:item_display,tag=mg.tnball,tag=mg.tnk] remove mg.tntoss
execute if score $tnw mg.st matches 1 run scoreboard players add @s mg.tnp1 1
execute if score $tnw mg.st matches 2 run scoreboard players add @s mg.tnp2 1
scoreboard players set @s mg.tnph 3
scoreboard players set @s mg.tnt 50
tag @e[type=minecraft:mannequin,tag=mg.tnrob,tag=mg.tnk] remove mg.tnchase
title @a[tag=mg.tnk] times 3 25 8
execute if score $tnwhy mg.st matches 1 run title @a[tag=mg.tnk] subtitle {"text":"Filet !","color":"gray"}
execute if score $tnwhy mg.st matches 2 run title @a[tag=mg.tnk] subtitle {"text":"Faute : balle dehors","color":"gray"}
execute if score $tnwhy mg.st matches 3 run title @a[tag=mg.tnk] subtitle {"text":"Double rebond","color":"gray"}
execute if score $tnwhy mg.st matches 4 run title @a[tag=mg.tnk] subtitle {"text":"Faute : rebond dans son camp","color":"gray"}
execute if score $tnwhy mg.st matches 5 run title @a[tag=mg.tnk] subtitle {"text":"Balle non rattrapée","color":"gray"}
execute if score $tnw mg.st matches 1 run title @a[tag=mg.tnk] title [{"text":"Point ","color":"white"},{"text":"BLEU","color":"aqua","bold":true}]
execute if score $tnw mg.st matches 2 run title @a[tag=mg.tnk] title [{"text":"Point ","color":"white"},{"text":"ROUGE","color":"red","bold":true}]
execute as @a[tag=mg.tnk] at @s if score @s mg.tns = $tnw mg.st run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.8 1.2
execute as @a[tag=mg.tnk] at @s unless score @s mg.tns = $tnw mg.st run playsound minecraft:block.note_block.bass master @s ~ ~ ~ 0.8 0.7
scoreboard players operation $tnq mg.st = @s mg.tnp1
scoreboard players operation $tnq mg.st -= @s mg.tnp2
execute if score @s mg.tnp1 matches 4.. if score $tnq mg.st matches 2.. run function mg:tennis/game_won1
execute if score @s mg.tnp2 matches 4.. if score $tnq mg.st matches ..-2 run function mg:tennis/game_won2
function mg:tennis/labels
