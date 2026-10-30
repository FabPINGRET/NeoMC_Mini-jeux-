# TNT Tag — préparation de la carte 4 « Icebergs » (centre 0 ~ 31200), générée par tools/tnttag/gen_maps.py
function mg:tnttag/map/build_4
# Perchoir des éliminés (~15 blocs au-dessus du point le plus haut) et hauteur d'élimination
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 105
scoreboard players set $pz mg.st 31200
scoreboard players set $tty mg.st 79
kill @e[type=minecraft:item,x=-25,y=76,z=31175,dx=50,dy=44,dz=50]
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 82 31194
# Placement sur 16 points de départ fixes au sol (tirés au hasard, deux passes si beaucoup de joueurs)
tag @a remove mg.tts
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:0.5,y:82,z:31194.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-6.5,y:82,z:31198.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:6.5,y:82,z:31199.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:10.5,y:82,z:31205.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-9.5,y:82,z:31208.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:2.5,y:82,z:31209.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-4.5,y:82,z:31185.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:9.5,y:82,z:31183.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:20.5,y:82,z:31192.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:21.5,y:82,z:31210.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-21.5,y:82,z:31206.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-20.5,y:82,z:31190.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-11.5,y:87,z:31189.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:11.5,y:87,z:31212.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-12.5,y:86,z:31213.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:0.5,y:82,z:31222.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:0.5,y:82,z:31194.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-6.5,y:82,z:31198.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:6.5,y:82,z:31199.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:10.5,y:82,z:31205.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-9.5,y:82,z:31208.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:2.5,y:82,z:31209.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-4.5,y:82,z:31185.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:9.5,y:82,z:31183.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:20.5,y:82,z:31192.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:21.5,y:82,z:31210.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-21.5,y:82,z:31206.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-20.5,y:82,z:31190.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-11.5,y:87,z:31189.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:11.5,y:87,z:31212.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-12.5,y:86,z:31213.5,fx:0.5,fz:31200.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:0.5,y:82,z:31222.5,fx:0.5,fz:31200.5}
tp @a[tag=mg.play,tag=!mg.tts] 0.5 82 31194.5
tag @a remove mg.tts
