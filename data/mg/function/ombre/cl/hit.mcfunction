# @s (monstre) : dégâts $(d) du lanceur (tag mg.olcast), chiffre flottant
$damage @s $(d) mg:spell by @a[tag=mg.olcast,limit=1]
$summon minecraft:text_display ~ ~2 ~ {Tags:["mg.ol","mg.oldmg"],billboard:"center",teleport_duration:10,text:{"text":"-$(d)","color":"gold","bold":true},background:0,shadow:1b,see_through:1b}
scoreboard players set @e[tag=mg.oldmg,distance=..2.5,sort=nearest,limit=1] mg.olst 12
