# (marqueur) drapeau BLEU posé au sol ici
scoreboard players set $cfb mg.st 2
scoreboard players set $cfbt mg.st 600
summon minecraft:item_display ~ ~0.9 ~ {Tags:["mg.cfd","mg.cfdb"],billboard:"vertical",item:{id:"minecraft:blue_banner",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}
kill @s
tellraw @a[tag=mg.play] [{"text":"🚩 Le drapeau BLEU est tombé ! ","color":"blue"},{"text":"(retour automatique dans 30 s)","color":"gray"}]
