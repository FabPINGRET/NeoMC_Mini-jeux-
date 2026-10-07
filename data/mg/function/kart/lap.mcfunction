execute if score $klob mg.st matches 1 run return run function mg:lobkart/lap
scoreboard players add @s mg.klp 1
execute if score @s mg.klp > $kLaps mg.st run return run function mg:kart/finish
execute if score @s mg.klp matches 2.. if score @s mg.klp < $kLaps mg.st run title @s actionbar [{"text":"🏁 Tour ","color":"gold"},{"score":{"name":"@s","objective":"mg.klp"},"color":"yellow","bold":true},{"text":" / ","color":"gold"},{"score":{"name":"$kLaps","objective":"mg.st"},"color":"gold"}]
execute if score @s mg.klp = $kLaps mg.st run title @s title [{"text":"TOUR FINAL !","color":"gold","bold":true}]
execute if score @s mg.klp = $kLaps mg.st if score $kfl mg.st matches 0 run function mg:kart/final_lap
execute if score @s mg.klp = $kLaps mg.st at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.8 1.6
