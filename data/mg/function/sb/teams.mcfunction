# Lignes par équipe : joueurs encore en jeu (Bedwars : 🛏 lit debout / ✖ lit détruit)
execute if entity @a[team=mg_red] store result score #sb_red mg.sbg if entity @a[team=mg_red,tag=mg.play]
execute if score #sb_red mg.sbg matches 0.. run scoreboard players display numberformat #sb_red mg.sbg styled {"color":"white","bold":true}
execute if score #sb_red mg.sbg matches 0.. unless score $game mg.st matches 4 run scoreboard players display name #sb_red mg.sbg [{"text":"■ Équipe Rouge","color":"red","bold":true}]
execute if score $game mg.st matches 4 if score #sb_red mg.sbg matches 0.. if score $bed_red mg.st matches 1 run scoreboard players display name #sb_red mg.sbg [{"text":"■ Rouge ","color":"red","bold":true},{"text":"🛏 lit debout","color":"green","bold":false}]
execute if score $game mg.st matches 4 if score #sb_red mg.sbg matches 0.. unless score $bed_red mg.st matches 1 run scoreboard players display name #sb_red mg.sbg [{"text":"■ Rouge ","color":"red","bold":true},{"text":"✖ plus de lit","color":"red","bold":false}]
execute if entity @a[team=mg_blue] store result score #sb_blue mg.sbg if entity @a[team=mg_blue,tag=mg.play]
execute if score #sb_blue mg.sbg matches 0.. run scoreboard players display numberformat #sb_blue mg.sbg styled {"color":"white","bold":true}
execute if score #sb_blue mg.sbg matches 0.. unless score $game mg.st matches 4 run scoreboard players display name #sb_blue mg.sbg [{"text":"■ Équipe Bleue","color":"blue","bold":true}]
execute if score $game mg.st matches 4 if score #sb_blue mg.sbg matches 0.. if score $bed_blue mg.st matches 1 run scoreboard players display name #sb_blue mg.sbg [{"text":"■ Bleue ","color":"blue","bold":true},{"text":"🛏 lit debout","color":"green","bold":false}]
execute if score $game mg.st matches 4 if score #sb_blue mg.sbg matches 0.. unless score $bed_blue mg.st matches 1 run scoreboard players display name #sb_blue mg.sbg [{"text":"■ Bleue ","color":"blue","bold":true},{"text":"✖ plus de lit","color":"red","bold":false}]
execute if entity @a[team=mg_green] store result score #sb_green mg.sbg if entity @a[team=mg_green,tag=mg.play]
execute if score #sb_green mg.sbg matches 0.. run scoreboard players display numberformat #sb_green mg.sbg styled {"color":"white","bold":true}
execute if score #sb_green mg.sbg matches 0.. unless score $game mg.st matches 4 run scoreboard players display name #sb_green mg.sbg [{"text":"■ Équipe Verte","color":"green","bold":true}]
execute if score $game mg.st matches 4 if score #sb_green mg.sbg matches 0.. if score $bed_green mg.st matches 1 run scoreboard players display name #sb_green mg.sbg [{"text":"■ Verte ","color":"green","bold":true},{"text":"🛏 lit debout","color":"green","bold":false}]
execute if score $game mg.st matches 4 if score #sb_green mg.sbg matches 0.. unless score $bed_green mg.st matches 1 run scoreboard players display name #sb_green mg.sbg [{"text":"■ Verte ","color":"green","bold":true},{"text":"✖ plus de lit","color":"red","bold":false}]
execute if entity @a[team=mg_yellow] store result score #sb_yellow mg.sbg if entity @a[team=mg_yellow,tag=mg.play]
execute if score #sb_yellow mg.sbg matches 0.. run scoreboard players display numberformat #sb_yellow mg.sbg styled {"color":"white","bold":true}
execute if score #sb_yellow mg.sbg matches 0.. unless score $game mg.st matches 4 run scoreboard players display name #sb_yellow mg.sbg [{"text":"■ Équipe Jaune","color":"yellow","bold":true}]
execute if score $game mg.st matches 4 if score #sb_yellow mg.sbg matches 0.. if score $bed_yellow mg.st matches 1 run scoreboard players display name #sb_yellow mg.sbg [{"text":"■ Jaune ","color":"yellow","bold":true},{"text":"🛏 lit debout","color":"green","bold":false}]
execute if score $game mg.st matches 4 if score #sb_yellow mg.sbg matches 0.. unless score $bed_yellow mg.st matches 1 run scoreboard players display name #sb_yellow mg.sbg [{"text":"■ Jaune ","color":"yellow","bold":true},{"text":"✖ plus de lit","color":"red","bold":false}]
