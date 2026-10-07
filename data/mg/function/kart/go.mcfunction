# Départ : portillon ouvert
function mg:kart/gate_off
scoreboard players set $ktime mg.st 0
scoreboard players set @a[tag=mg.play] mg.ksp 0
tellraw @a[tag=mg.play] [{"text":"🏎 ","color":"gold"},{"text":"KART","color":"gold","bold":true},{"text":" : Z avancer, S freiner / reculer, Q / D tourner, ","color":"gray"},{"text":"ESPACE en tournant = dérapage","color":"yellow"},{"text":" (relâche après les étincelles bleues, orange ou violettes pour un mini-turbo). Boîtes ? = objets, Ctrl pour les utiliser. 3 tours !","color":"gray"}]
