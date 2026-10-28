# Chaque seconde (joueurs présents) : effets, recharges, barre, PvP en surface
execute as @a[tag=mg.fnw] run function mg:filon/effects
scoreboard players remove @a[tag=mg.fnw,scores={mg.fncd=1..}] mg.fncd 1
# coincé dans la roche (reconnecté après une régénération) : remonté
execute as @a[tag=mg.fnw,tag=mg.fnin] at @s if block ~ ~ ~ #mg:filon_mine if block ~ ~1 ~ #mg:filon_mine run function mg:filon/to_surface
execute if score $fnpvp mg.st matches 1 run effect give @a[tag=mg.fnw,tag=!mg.fnin] minecraft:resistance 2 4 true
execute if score $fnpvp mg.st matches 1 run effect give @a[tag=mg.fnw,tag=!mg.fnin] minecraft:weakness 2 255 true
bossbar set mg:filon players @a[tag=mg.fnw]
execute store result bossbar mg:filon value run scoreboard players get $fnt mg.st
scoreboard players set #r mg.st 2700
scoreboard players operation #r mg.st -= $fnt mg.st
scoreboard players operation #r mg.st /= #fn60 mg.st
execute if score $fnpvp mg.st matches 1 run bossbar set mg:filon color red
execute if score $fnpvp mg.st matches 1 run bossbar set mg:filon name [{"text":"⚔ PvP dans la mine","color":"red","bold":true},{"text":" — régénération dans ","color":"gray","bold":false},{"score":{"name":"#r","objective":"mg.st"},"color":"yellow","bold":false},{"text":" min","color":"gray","bold":false}]
execute unless score $fnpvp mg.st matches 1 run bossbar set mg:filon color yellow
execute unless score $fnpvp mg.st matches 1 run bossbar set mg:filon name [{"text":"⛏ Filon","color":"gold","bold":true},{"text":" — régénération dans ","color":"gray","bold":false},{"score":{"name":"#r","objective":"mg.st"},"color":"yellow","bold":false},{"text":" min","color":"gray","bold":false}]
# (objets au sol : disparition naturelle au bout de 5 min)
