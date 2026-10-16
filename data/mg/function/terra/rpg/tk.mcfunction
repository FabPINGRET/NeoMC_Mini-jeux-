# @s : choix dans un dialogue (trigger mg.trtk)
scoreboard players operation $tk mg.st = @s mg.trtk
scoreboard players reset @s mg.trtk
scoreboard players enable @s mg.trtk
execute if score $tk mg.st matches 9 run function mg:terra/rpg/quest
execute if score $tk mg.st matches 110 run function mg:terra/board
execute if score $tk mg.st matches 101 if score @s mg.trch matches 0 run function mg:terra/rpg/ch {n:10}
execute if score $tk mg.st matches 102 if score @s mg.trch matches 15 run function mg:terra/rpg/rw {xp:150,c:100,n:20}
execute if score $tk mg.st matches 103 if score @s mg.trch matches 45 run function mg:terra/rpg/rw {xp:500,c:300,n:50}
execute if score $tk mg.st matches 104 if score @s mg.trch matches 66 run function mg:terra/rpg/rw {xp:700,c:500,n:70}
execute if score $tk mg.st matches 105 if score @s mg.trch matches 90 run function mg:terra/rpg/finale
execute if score $tk mg.st matches 201 if score @s mg.trch matches 20 run function mg:terra/rpg/give_scanner
execute if score $tk mg.st matches 202 if score @s mg.trch matches 28 run function mg:terra/rpg/rw {xp:150,c:0,n:30}
execute if score $tk mg.st matches 203 if score @s mg.trch matches 35 run function mg:terra/rpg/rw {xp:300,c:200,n:40}
execute if score $tk mg.st matches 204 if score @s mg.trch matches 70 run function mg:terra/rpg/ch {n:72}
execute if score $tk mg.st matches 210 run function mg:terra/rpg/bestiary
execute if score $tk mg.st matches 600 run function mg:terra/rpg/cl/menu
execute if score $tk mg.st matches 601..604 run function mg:terra/rpg/cl/pick_tk
execute if score $tk mg.st matches 211 run function mg:terra/rpg/eggs
execute if score $tk mg.st matches 401 if score @s mg.trch matches 52 run function mg:terra/rpg/ch {n:55}
execute if score $tk mg.st matches 402 if score @s mg.trch matches 58 run function mg:terra/rpg/rw {xp:400,c:0,n:60}
execute if score $tk mg.st matches 301 run function mg:terra/rpg/craft_301
execute if score $tk mg.st matches 302 run function mg:terra/rpg/craft_302
execute if score $tk mg.st matches 303 run function mg:terra/rpg/craft_303
execute if score $tk mg.st matches 304 run function mg:terra/rpg/craft_304
execute if score $tk mg.st matches 305 run function mg:terra/rpg/craft_305
execute if score $tk mg.st matches 306 run function mg:terra/rpg/craft_306
execute if score $tk mg.st matches 307 run function mg:terra/rpg/craft_307
execute if score $tk mg.st matches 501 run function mg:terra/rpg/go/1
execute if score $tk mg.st matches 502 run function mg:terra/rpg/go/2
execute if score $tk mg.st matches 503 run function mg:terra/rpg/go/3
execute if score $tk mg.st matches 504 run function mg:terra/rpg/go/4
execute if score $tk mg.st matches 505 run function mg:terra/rpg/go/5
function mg:terra/rpg/tk2
