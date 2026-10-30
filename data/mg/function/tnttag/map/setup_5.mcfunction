# TNT Tag — préparation de la carte 5 « Patinoire » (centre 0 ~ 31500), générée par tools/tnttag/gen_maps.py
function mg:tnttag/map/build_5
# Perchoir des éliminés (~15 blocs au-dessus du point le plus haut) et hauteur d'élimination
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 104
scoreboard players set $pz mg.st 31500
scoreboard players set $tty mg.st 80
kill @e[type=minecraft:item,x=-25,y=76,z=31475,dx=50,dy=44,dz=50]
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 83 31490
# Placement sur 16 points de départ fixes au sol (tirés au hasard, deux passes si beaucoup de joueurs)
tag @a remove mg.tts
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:0.5,y:83,z:31490.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:0.5,y:83,z:31510.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-8.5,y:83,z:31497.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:8.5,y:83,z:31503.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-13.5,y:83,z:31492.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:13.5,y:83,z:31508.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-13.5,y:83,z:31508.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:13.5,y:83,z:31492.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-4.5,y:83,z:31504.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:4.5,y:83,z:31496.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-20.5,y:87,z:31480.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:20.5,y:87,z:31520.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-20.5,y:87,z:31520.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:20.5,y:87,z:31480.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-22.5,y:87,z:31508.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:22.5,y:87,z:31492.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:0.5,y:83,z:31490.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:0.5,y:83,z:31510.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-8.5,y:83,z:31497.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:8.5,y:83,z:31503.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-13.5,y:83,z:31492.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:13.5,y:83,z:31508.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-13.5,y:83,z:31508.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:13.5,y:83,z:31492.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-4.5,y:83,z:31504.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:4.5,y:83,z:31496.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-20.5,y:87,z:31480.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:20.5,y:87,z:31520.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-20.5,y:87,z:31520.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:20.5,y:87,z:31480.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-22.5,y:87,z:31508.5,fx:0.5,fz:31500.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:22.5,y:87,z:31492.5,fx:0.5,fz:31500.5}
tp @a[tag=mg.play,tag=!mg.tts] 0.5 83 31490.5
tag @a remove mg.tts
