# Désinstallation (OP) — retire scoreboards, équipes, décor et zones chargées
kill @e[type=minecraft:text_display,tag=mg.deco]
kill @e[tag=mg.lby]
kill @e[tag=mg.lkart]
kill @e[tag=mg.arm]
kill @e[tag=mg.mob]
kill @e[tag=mg.sheep]
kill @e[tag=mg.npc]
execute as @a run function mg:core/unfreeze
forceload remove all
data remove storage mg:var a
scoreboard objectives setdisplay sidebar
scoreboard objectives setdisplay list
scoreboard objectives setdisplay below_name
scoreboard objectives remove mg.hp
scoreboard objectives remove mg.svx
scoreboard objectives remove mg.svy
scoreboard objectives remove mg.svz
scoreboard objectives remove mg.fw
scoreboard objectives remove mg.wc
scoreboard objectives remove mg.wd
scoreboard objectives remove mg.vote
scoreboard objectives remove mg.bb
scoreboard objectives remove mg.bw
schedule clear mg:core/setup_watch
data remove storage mg:setup plot
scoreboard objectives remove mg.rt
scoreboard objectives remove mg.rts
scoreboard objectives remove mg.rtn
scoreboard objectives remove mg.rgs
scoreboard objectives remove mg.rgn
scoreboard objectives remove mg.rfs
scoreboard objectives remove mg.rfn
schedule clear mg:rate/ask
data remove storage mg:rate lab
team remove mg_ph
scoreboard objectives remove mg.pid
scoreboard objectives remove mg.php
scoreboard objectives remove mg.phx
scoreboard objectives remove mg.phz
scoreboard objectives remove mg.phs
data remove storage mg:zm hp
scoreboard objectives remove mg.zpt
scoreboard objectives remove mg.zk
scoreboard objectives remove mg.gcd
scoreboard objectives remove mg.grl
scoreboard objectives remove mg.grt
scoreboard objectives remove mg.gsn
scoreboard objectives remove mg.g1
scoreboard objectives remove mg.g2
scoreboard objectives remove mg.g3
scoreboard objectives remove mg.g4
scoreboard objectives remove mg.g5
scoreboard objectives remove mg.g6
data remove storage mg:zone r
scoreboard objectives remove mg.cf
stopsound @a record
bossbar remove mg:convoy
scoreboard objectives remove mg.kh
scoreboard objectives remove mg.trc
scoreboard objectives remove mg.trs
schedule clear mg:tel/plots
scoreboard objectives remove mg.tel
scoreboard objectives remove mg.ti
scoreboard objectives remove mg.tc
scoreboard objectives remove mg.tx
scoreboard objectives remove mg.tz
scoreboard objectives remove mg.tpt
scoreboard objectives remove mg.tel
scoreboard objectives remove mg.ti
scoreboard objectives remove mg.tc
scoreboard objectives remove mg.tx
scoreboard objectives remove mg.tz
scoreboard objectives remove mg.tpt
scoreboard objectives remove mg.bi
scoreboard objectives remove mg.br
scoreboard objectives remove mg.ba
kill @e[type=minecraft:marker,tag=mg.bpm]
kill @e[tag=mg.bbd]
scoreboard objectives remove mg.vc
scoreboard objectives remove mg.vb
scoreboard objectives remove mg.ak
scoreboard objectives remove mg.ag
scoreboard objectives remove mg.cp
scoreboard objectives remove mg.lp
scoreboard objectives remove mg.ri
scoreboard objectives remove mg.rp
scoreboard objectives remove mg.tw
scoreboard objectives remove mg.qk
scoreboard objectives remove mg.pb
scoreboard objectives remove mg.pi
scoreboard objectives remove mg.ph
scoreboard objectives remove mg.pt
scoreboard objectives remove mg.ppc
scoreboard objectives remove mg.ppt
scoreboard objectives remove mg.ppb
scoreboard objectives remove mg.ppf
kill @e[type=minecraft:marker,tag=mg.pkm]
kill @e[type=minecraft:text_display,tag=mg.pkd]
scoreboard objectives remove mg.ks
scoreboard objectives remove mg.gi
scoreboard objectives remove mg.qp
scoreboard objectives remove mg.qs
scoreboard objectives remove mg.ts
scoreboard objectives remove mg.dp
scoreboard objectives remove mg.ln
scoreboard objectives remove mg.lv
scoreboard objectives remove mg.mb
scoreboard objectives remove mg.st
scoreboard objectives remove mg.t
scoreboard objectives remove mg.wins
scoreboard objectives remove mg.deaths
scoreboard objectives remove mg.cs
scoreboard objectives remove mg.us
scoreboard objectives remove mg.menu
scoreboard objectives remove mg.go
scoreboard objectives remove mg.cd
scoreboard objectives remove mg.cls
scoreboard objectives remove mg.cl
scoreboard objectives remove mg.opt
scoreboard objectives remove mg.buy
scoreboard objectives remove mg.lg
scoreboard objectives remove mg.pk
scoreboard objectives remove mg.pl
scoreboard objectives remove mg.plot
scoreboard objectives remove mg.pcx
scoreboard objectives remove mg.pcz
scoreboard objectives remove mg.dice
scoreboard objectives remove mg.dz
scoreboard objectives remove mg.mpm
scoreboard objectives remove mg.mpk
scoreboard objectives remove mg.mpi
scoreboard objectives remove mg.mpo
scoreboard objectives remove mg.mpz
scoreboard objectives remove mg.mpv
scoreboard objectives remove mg.mid
scoreboard objectives remove mg.sv
scoreboard objectives remove mg.kty
scoreboard objectives remove mg.kcol
scoreboard objectives remove mg.kbl
scoreboard objectives remove mg.kch
scoreboard objectives remove mg.krl
scoreboard objectives remove mg.ksp
scoreboard objectives remove mg.kdr
scoreboard objectives remove mg.kdd
scoreboard objectives remove mg.kbo
scoreboard objectives remove mg.khi
scoreboard objectives remove mg.kst
scoreboard objectives remove mg.kit
scoreboard objectives remove mg.kcp
scoreboard objectives remove mg.klp
scoreboard objectives remove mg.kvy
scoreboard objectives remove mg.kfp
scoreboard objectives remove mg.kpg
scoreboard objectives remove mg.krk
scoreboard objectives remove mg.kps
scoreboard objectives remove mg.krc
scoreboard objectives remove mg.khd
scoreboard objectives remove mg.kspr
scoreboard objectives remove mg.kvm
scoreboard objectives remove mg.kv
scoreboard objectives remove mg.kic
scoreboard objectives remove mg.kgd
scoreboard objectives remove mg.kbill
scoreboard objectives remove mg.kboo
scoreboard objectives remove mg.kmg
scoreboard objectives remove mg.kmap
bossbar remove mg:party
bossbar remove mg:boss
scoreboard objectives remove mg.mit
scoreboard objectives remove mg.mip
kill @e[type=minecraft:armor_stand,tag=mg.mppawn]
kill @e[type=minecraft:text_display,tag=mg.mpdeco]
kill @e[type=minecraft:text_display,tag=mg.mpdice]
kill @e[type=minecraft:text_display,tag=mg.mpstar]
data remove storage mg:party built
data remove storage mg:plot owner
kill @e[type=minecraft:text_display,tag=mg.pdisp]
tag @a remove mg.inplot
tag @a remove mg.visit
tag @a remove mg.plabel
team remove mg_red
team remove mg_blue
team remove mg_green
team remove mg_yellow
team remove mg_party
tag @a remove mg.init
tag @a remove mg.play
tag @a remove mg.out
tag @a remove mg.win
tag @a remove mg.spectate
tag @a remove mg.admin
tellraw @a [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Désinstallé. Les constructions restent (les arènes ne sont pas effacées). Retire ensuite le datapack du dossier datapacks.","color":"gray"}]

# Objectifs restants
scoreboard objectives remove mg.ec
scoreboard objectives remove mg.et
scoreboard objectives remove mg.eg
scoreboard objectives remove mg.est
scoreboard objectives remove mg.erb
scoreboard objectives remove mg.fd
scoreboard objectives remove mg.stp
scoreboard objectives remove mg.stk
scoreboard objectives remove mg.dfl
scoreboard objectives remove mg.dlv
scoreboard objectives remove mg.dpw
scoreboard objectives remove mg.ok
scoreboard objectives remove mg.svid
scoreboard objectives remove mg.svvx
scoreboard objectives remove mg.kstk
scoreboard objectives remove mg.kof
scoreboard objectives remove mg.klt
scoreboard objectives remove mg.klb
scoreboard objectives remove mg.lcd
scoreboard objectives remove mg.esn
scoreboard objectives remove mg.esc
scoreboard objectives remove mg.eup
scoreboard objectives remove mg.ebl
scoreboard objectives remove mg.ept

# Annule les constructions planifiées en cours (chaînes schedule)
schedule clear mg:bb/clear_old_run
schedule clear mg:core/diag_late
schedule clear mg:core/setup_build
schedule clear mg:sky/build
schedule clear mg:dropadv/build
schedule clear mg:dropadv/build_10
schedule clear mg:dropadv/build_11
schedule clear mg:dropadv/build_12
schedule clear mg:dropadv/build_13
schedule clear mg:dropadv/build_14
schedule clear mg:dropadv/build_15
schedule clear mg:dropadv/build_16
schedule clear mg:dropadv/build_17
schedule clear mg:dropadv/build_2
schedule clear mg:dropadv/build_3
schedule clear mg:dropadv/build_4
schedule clear mg:dropadv/build_5
schedule clear mg:dropadv/build_6
schedule clear mg:dropadv/build_7
schedule clear mg:dropadv/build_8
schedule clear mg:dropadv/build_9
schedule clear mg:dropadv/build_wait
schedule clear mg:kart/build
schedule clear mg:kart/place_all
schedule clear mg:kart/pre_tick
schedule clear mg:kart/t1/build_2
schedule clear mg:kart/t1/build_3
schedule clear mg:kart/t1/build_4
schedule clear mg:kart/t1/build_5
schedule clear mg:kart/t1/build_6
schedule clear mg:kart/t1/build_7
schedule clear mg:kart/t1/build_8
schedule clear mg:kart/t1/build_wait
schedule clear mg:kart/t2/build
schedule clear mg:kart/t2/build_10
schedule clear mg:kart/t2/build_11
schedule clear mg:kart/t2/build_12
schedule clear mg:kart/t2/build_13
schedule clear mg:kart/t2/build_14
schedule clear mg:kart/t2/build_15
schedule clear mg:kart/t2/build_16
schedule clear mg:kart/t2/build_17
schedule clear mg:kart/t2/build_18
schedule clear mg:kart/t2/build_19
schedule clear mg:kart/t2/build_2
schedule clear mg:kart/t2/build_20
schedule clear mg:kart/t2/build_21
schedule clear mg:kart/t2/build_22
schedule clear mg:kart/t2/build_23
schedule clear mg:kart/t2/build_24
schedule clear mg:kart/t2/build_25
schedule clear mg:kart/t2/build_26
schedule clear mg:kart/t2/build_27
schedule clear mg:kart/t2/build_28
schedule clear mg:kart/t2/build_29
schedule clear mg:kart/t2/build_3
schedule clear mg:kart/t2/build_30
schedule clear mg:kart/t2/build_31
schedule clear mg:kart/t2/build_32
schedule clear mg:kart/t2/build_33
schedule clear mg:kart/t2/build_34
schedule clear mg:kart/t2/build_35
schedule clear mg:kart/t2/build_36
schedule clear mg:kart/t2/build_37
schedule clear mg:kart/t2/build_38
schedule clear mg:kart/t2/build_39
schedule clear mg:kart/t2/build_4
schedule clear mg:kart/t2/build_5
schedule clear mg:kart/t2/build_6
schedule clear mg:kart/t2/build_7
schedule clear mg:kart/t2/build_8
schedule clear mg:kart/t2/build_9
schedule clear mg:kart/t2/build_wait
schedule clear mg:kart/t3/build
schedule clear mg:kart/t3/build_10
schedule clear mg:kart/t3/build_11
schedule clear mg:kart/t3/build_12
schedule clear mg:kart/t3/build_2
schedule clear mg:kart/t3/build_3
schedule clear mg:kart/t3/build_4
schedule clear mg:kart/t3/build_5
schedule clear mg:kart/t3/build_6
schedule clear mg:kart/t3/build_7
schedule clear mg:kart/t3/build_8
schedule clear mg:kart/t3/build_9
schedule clear mg:kart/t3/build_wait
schedule clear mg:lobby/build
schedule clear mg:lobby/build_1
schedule clear mg:lobby/build_2
schedule clear mg:lobby/build_3
schedule clear mg:lobby/build_4
schedule clear mg:lobby/build_5
schedule clear mg:lobby/build_6
schedule clear mg:lobby/build_7
schedule clear mg:lobby/build_8
schedule clear mg:lobby/build_9
schedule clear mg:lobby/build_10
schedule clear mg:lobby/build_11
schedule clear mg:lobby/build_end
schedule clear mg:mobarena/xbuild
schedule clear mg:mobarena/xbuild2
schedule clear mg:party/build
schedule clear mg:party/build_2
schedule clear mg:party/build_3
schedule clear mg:party/build_4
schedule clear mg:party/build_5
schedule clear mg:party/build_6
schedule clear mg:party/build_7
schedule clear mg:party/build_8
schedule clear mg:plot/build_all
schedule clear mg:lobby/food_build
schedule clear mg:coaster/build_start
schedule clear mg:coaster/build
kill @e[tag=mg.cst]
kill @e[tag=mg.csd]
data remove storage mg:lobby coaster1
data remove storage mg:lobby coaster2
kill @e[tag=mg.foodd]
schedule clear mg:elytra/build
kill @e[tag=mg.elyd]
clear @a minecraft:elytra[minecraft:custom_data~{mg_ely:1b}]
clear @a minecraft:firework_rocket[minecraft:custom_data~{mg_ely:1b}]
data remove storage mg:lobby ely1
data remove storage mg:lobby food1
function mg:hall/remove
function mg:sky/remove
scoreboard objectives remove mg.seen
scoreboard objectives remove mg.sbg
scoreboard objectives remove mg.ehw
clear @a minecraft:elytra[minecraft:custom_data~{mg_elyf:1b}]
clear @a minecraft:firework_rocket[minecraft:custom_data~{mg_elyf:1b}]
tag @a remove mg.elyf
tag @a remove mg.efp
scoreboard objectives remove mg.ecr
scoreboard objectives remove mg.erb2
function mg:elyrace/uninstall
