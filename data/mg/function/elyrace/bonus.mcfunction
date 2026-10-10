# @s = joueur qui arrive : #xrt (temps en ticks) diminue du bonus de ses anneaux d'or (mg.xu x 40 ticks), sans descendre sous 1 tick ;
# #xgs = bonus en secondes (affichage). Appelé par finish et solo/finish, entre #xrt = chrono et les records
scoreboard players operation #xgb mg.st = @s mg.xu
scoreboard players operation #xgb mg.st *= #kgb mg.st
scoreboard players operation #xrt mg.st -= #xgb mg.st
execute if score #xrt mg.st matches ..0 run scoreboard players set #xrt mg.st 1
scoreboard players operation #xgs mg.st = #xgb mg.st
scoreboard players operation #xgs mg.st /= #k20 mg.st
