# TNT Tag — préparation de la carte 2 « Canyon » (centre 0 ~ 26800), générée par tools/tnttag/gen_maps.py
function mg:tnttag/map/build_2
# Perchoir des éliminés (~15 blocs au-dessus du point le plus haut) et hauteur d'élimination
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 111
scoreboard players set $pz mg.st 26800
scoreboard players set $tty mg.st 80
kill @e[type=minecraft:item,x=-25,y=76,z=26775,dx=50,dy=44,dz=50]
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 83 26799
# Placement sur 16 points de départ fixes au sol (tirés au hasard, deux passes si beaucoup de joueurs)
tag @a remove mg.tts
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:0.5,y:83,z:26799.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-3.5,y:84,z:26814.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:3.5,y:83,z:26785.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-5.5,y:89,z:26804.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:6.5,y:83,z:26816.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:18.5,y:83,z:26818.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-18.5,y:87,z:26805.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:18.5,y:87,z:26798.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-17.5,y:91,z:26789.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:17.5,y:91,z:26786.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-20.5,y:87,z:26822.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:13.5,y:87,z:26810.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-14.5,y:87,z:26812.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-18.5,y:95,z:26779.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:19.5,y:95,z:26779.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-5.5,y:83,z:26778.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:0.5,y:83,z:26799.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-3.5,y:84,z:26814.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:3.5,y:83,z:26785.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-5.5,y:89,z:26804.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:6.5,y:83,z:26816.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:18.5,y:83,z:26818.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-18.5,y:87,z:26805.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:18.5,y:87,z:26798.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-17.5,y:91,z:26789.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:17.5,y:91,z:26786.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-20.5,y:87,z:26822.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:13.5,y:87,z:26810.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-14.5,y:87,z:26812.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-18.5,y:95,z:26779.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:19.5,y:95,z:26779.5,fx:0.5,fz:26800.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-5.5,y:83,z:26778.5,fx:0.5,fz:26800.5}
tp @a[tag=mg.play,tag=!mg.tts] 0.5 83 26799.5
tag @a remove mg.tts
