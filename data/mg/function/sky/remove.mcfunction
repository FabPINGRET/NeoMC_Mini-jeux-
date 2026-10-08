# Élytra : désinstallation (à appeler depuis mg:desinstaller)
scoreboard objectives remove mg.skr
scoreboard objectives remove mg.sks
scoreboard objectives remove mg.skg
scoreboard objectives remove mg.skst
scoreboard objectives remove mg.skl
scoreboard objectives remove mg.sko
schedule clear mg:sky/b_next
schedule clear mg:sky/pad_wait
function mg:sky/fl_secs_off
function mg:sky/pad_fl_off
data remove storage mg:sky built
data remove storage mg:sky z
advancement revoke @a only mg:sky/hurt
