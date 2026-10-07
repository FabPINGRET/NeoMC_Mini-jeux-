execute if score $kr0 mg.st > $kn mg.st run return 0
execute as @a[tag=mg.play] if score @s mg.krk = $kr0 mg.st run tellraw @a[tag=!mg.surv] [{"text":"  ","color":"gray"},{"score":{"name":"$kr0","objective":"mg.st"},"color":"gold","bold":true},{"text":". ","color":"gold"},{"selector":"@s","color":"white"}]
scoreboard players add $kr0 mg.st 1
function mg:kart/end_line
