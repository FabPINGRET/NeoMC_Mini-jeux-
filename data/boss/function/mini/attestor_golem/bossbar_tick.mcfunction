execute store result score boss:attestor BossHealth run data get entity @n[tag=a_golem,distance=0..] Health

execute if score boss:attestor BossHealth < boss:attestor_half BossHealth run bossbar set boss:attestor color yellow
execute if score boss:attestor BossHealth < boss:attestor_quarter BossHealth run bossbar set boss:attestor color red
