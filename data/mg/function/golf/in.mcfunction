# @s : a rentré sa balle
execute unless score @s mg.gfs matches 0..1 run return 0
scoreboard players operation $gfrel mg.st = @s mg.gfc
scoreboard players operation $gfrel mg.st -= $gfpar mg.st
execute if score @s mg.gfc matches 1 run return run function mg:golf/ace
execute if score $gfrel mg.st matches -99..-4 run tellraw @a[tag=mg.play] [{"text":"⛳ ","color":"green"},{"selector":"@s","color":"yellow"},{"text":" rentre en ","color":"gray"},{"score":{"name":"@s","objective":"mg.gfc"},"color":"white","bold":true},{"text":" coup(s) — ","color":"gray"},{"text":"🦅 Condor","color":"light_purple","bold":true}]
execute if score $gfrel mg.st matches -99..-4 run title @s title {"text":"🦅 Condor","color":"light_purple","bold":true}
execute if score $gfrel mg.st matches -3..-3 run tellraw @a[tag=mg.play] [{"text":"⛳ ","color":"green"},{"selector":"@s","color":"yellow"},{"text":" rentre en ","color":"gray"},{"score":{"name":"@s","objective":"mg.gfc"},"color":"white","bold":true},{"text":" coup(s) — ","color":"gray"},{"text":"🦅 Albatros !","color":"light_purple","bold":true}]
execute if score $gfrel mg.st matches -3..-3 run title @s title {"text":"🦅 Albatros !","color":"light_purple","bold":true}
execute if score $gfrel mg.st matches -2..-2 run tellraw @a[tag=mg.play] [{"text":"⛳ ","color":"green"},{"selector":"@s","color":"yellow"},{"text":" rentre en ","color":"gray"},{"score":{"name":"@s","objective":"mg.gfc"},"color":"white","bold":true},{"text":" coup(s) — ","color":"gray"},{"text":"🦅 Eagle !","color":"gold","bold":true}]
execute if score $gfrel mg.st matches -2..-2 run title @s title {"text":"🦅 Eagle !","color":"gold","bold":true}
execute if score $gfrel mg.st matches -1..-1 run tellraw @a[tag=mg.play] [{"text":"⛳ ","color":"green"},{"selector":"@s","color":"yellow"},{"text":" rentre en ","color":"gray"},{"score":{"name":"@s","objective":"mg.gfc"},"color":"white","bold":true},{"text":" coup(s) — ","color":"gray"},{"text":"🐦 Birdie !","color":"green","bold":true}]
execute if score $gfrel mg.st matches -1..-1 run title @s title {"text":"🐦 Birdie !","color":"green","bold":true}
execute if score $gfrel mg.st matches 0..0 run tellraw @a[tag=mg.play] [{"text":"⛳ ","color":"green"},{"selector":"@s","color":"yellow"},{"text":" rentre en ","color":"gray"},{"score":{"name":"@s","objective":"mg.gfc"},"color":"white","bold":true},{"text":" coup(s) — ","color":"gray"},{"text":"Par","color":"white","bold":true}]
execute if score $gfrel mg.st matches 0..0 run title @s title {"text":"Par","color":"white","bold":true}
execute if score $gfrel mg.st matches 1..1 run tellraw @a[tag=mg.play] [{"text":"⛳ ","color":"green"},{"selector":"@s","color":"yellow"},{"text":" rentre en ","color":"gray"},{"score":{"name":"@s","objective":"mg.gfc"},"color":"white","bold":true},{"text":" coup(s) — ","color":"gray"},{"text":"Bogey","color":"yellow","bold":true}]
execute if score $gfrel mg.st matches 1..1 run title @s title {"text":"Bogey","color":"yellow","bold":true}
execute if score $gfrel mg.st matches 2..2 run tellraw @a[tag=mg.play] [{"text":"⛳ ","color":"green"},{"selector":"@s","color":"yellow"},{"text":" rentre en ","color":"gray"},{"score":{"name":"@s","objective":"mg.gfc"},"color":"white","bold":true},{"text":" coup(s) — ","color":"gray"},{"text":"Double bogey","color":"red","bold":true}]
execute if score $gfrel mg.st matches 2..2 run title @s title {"text":"Double bogey","color":"red","bold":true}
execute if score $gfrel mg.st matches 3..99 run tellraw @a[tag=mg.play] [{"text":"⛳ ","color":"green"},{"selector":"@s","color":"yellow"},{"text":" rentre en ","color":"gray"},{"score":{"name":"@s","objective":"mg.gfc"},"color":"white","bold":true},{"text":" coup(s) — ","color":"gray"},{"text":"Triple bogey ou pire","color":"dark_red","bold":true}]
execute if score $gfrel mg.st matches 3..99 run title @s title {"text":"Triple bogey ou pire","color":"dark_red","bold":true}
execute if score $gfrel mg.st matches ..-1 at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.8 1.2
function mg:golf/score
