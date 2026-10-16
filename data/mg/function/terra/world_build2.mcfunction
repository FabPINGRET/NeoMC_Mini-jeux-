# Construction des régions du RPG (marais, plaines, canyon, volcan) + cols de la vallée (~3 min)
scoreboard players set $tvrb mg.st 0
execute in mg:terranova run forceload add -112 -112 111 111
execute in mg:terranova run forceload add -96 -256 95 -97
execute in mg:terranova run forceload add 96 -96 255 95
execute in mg:terranova run forceload add -256 -96 -97 95
execute in mg:terranova run forceload add -96 96 95 255
schedule function mg:terra/rb_step 100t
