# TNT Tag — préparation de la carte 1 « Collines » (centre 0 ~ 26500), générée par tools/tnttag/gen_maps.py
function mg:tnttag/map/build_1
# Perchoir des éliminés (~15 blocs au-dessus du point le plus haut) et hauteur d'élimination
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 115
scoreboard players set $pz mg.st 26500
scoreboard players set $tty mg.st 79
kill @e[type=minecraft:item,x=-25,y=76,z=26475,dx=50,dy=44,dz=50]
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s -3 87 26484
# Placement sur 16 points de départ fixes au sol (tirés au hasard, deux passes si beaucoup de joueurs)
tag @a remove mg.tts
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-3.5,y:87,z:26484.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:5.5,y:86,z:26486.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-18.5,y:85,z:26494.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-23.5,y:86,z:26512.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-10.5,y:88,z:26520.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:2.5,y:87,z:26515.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:13.5,y:91,z:26518.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:21.5,y:89,z:26515.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:17.5,y:85,z:26499.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:21.5,y:87,z:26490.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:13.5,y:88,z:26480.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-11.5,y:89,z:26478.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-15.5,y:83,z:26496.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:6.5,y:83,z:26504.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-4.5,y:83,z:26504.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:20.5,y:87,z:26523.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-3.5,y:87,z:26484.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:5.5,y:86,z:26486.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-18.5,y:85,z:26494.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-23.5,y:86,z:26512.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-10.5,y:88,z:26520.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:2.5,y:87,z:26515.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:13.5,y:91,z:26518.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:21.5,y:89,z:26515.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:17.5,y:85,z:26499.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:21.5,y:87,z:26490.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:13.5,y:88,z:26480.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-11.5,y:89,z:26478.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-15.5,y:83,z:26496.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:6.5,y:83,z:26504.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-4.5,y:83,z:26504.5,fx:0.5,fz:26500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:20.5,y:87,z:26523.5,fx:0.5,fz:26500.5}
tp @a[tag=mg.play,tag=!mg.tts] -3.5 87 26484.5
tag @a remove mg.tts
