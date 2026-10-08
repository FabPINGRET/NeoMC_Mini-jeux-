# Sol 26 : perchoir, élimination, placement sur l’étage du haut. Généré.
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 90
scoreboard players set $pz mg.st 24300
scoreboard players set $yd mg.st 62
scoreboard players set $ky mg.st 62
scoreboard players set $nf mg.st 3
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 88 24300
tag @a remove mg.tts
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-12.5,y:81,z:24287.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:0.5,y:81,z:24287.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:13.5,y:81,z:24287.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:13.5,y:81,z:24300.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:13.5,y:81,z:24313.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:0.5,y:81,z:24313.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-12.5,y:81,z:24313.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-12.5,y:81,z:24300.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-9.5,y:81,z:24287.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:13.5,y:81,z:24290.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:10.5,y:81,z:24313.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-12.5,y:81,z:24310.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-12.5,y:81,z:24287.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:0.5,y:81,z:24287.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:13.5,y:81,z:24287.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:13.5,y:81,z:24300.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:13.5,y:81,z:24313.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:0.5,y:81,z:24313.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-12.5,y:81,z:24313.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-12.5,y:81,z:24300.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-9.5,y:81,z:24287.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:13.5,y:81,z:24290.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:10.5,y:81,z:24313.5,fx:0.5,fz:24300.5}
execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {x:-12.5,y:81,z:24310.5,fx:0.5,fz:24300.5}
tp @a[tag=mg.play,tag=!mg.tts] -12.5 81 24287.5
tag @a remove mg.tts
