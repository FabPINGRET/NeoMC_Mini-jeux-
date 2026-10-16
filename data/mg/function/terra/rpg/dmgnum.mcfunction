# Chiffre de dégâts au-dessus de @s (macro d), qui monte et disparaît
$summon minecraft:text_display ~ ~1.8 ~ {Tags:["mg.tv","mg.trdmg"],billboard:"center",teleport_duration:10,text:{"text":"-$(d)","color":"red","bold":true},background:0,shadow:1b,see_through:1b}
scoreboard players set @e[tag=mg.trdmg,distance=..2.5,sort=nearest,limit=1] mg.tvst 12
