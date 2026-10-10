# Mini-Jeux Void — chargement (idempotent)

# --- Objectifs ---
scoreboard objectives add mg.st dummy
# Modèles du resource pack activés par défaut (/function mg:rp_off pour les couper)
execute unless score $rp mg.st matches 0..1 run scoreboard players set $rp mg.st 1
# Neo City (monde GTA) : construite une fois (dimension mg:gta, 2 min)
execute if score $setup mg.st matches 1 unless data storage mg:gta built run schedule function mg:gta/world_build 45s
execute if score $setup mg.st matches 1 unless data storage mg:lobby gtaclean run schedule function mg:gta/spawn_clean 8s
scoreboard players set $gtw mg.st 0
# Neo City (monde GTA) : construite une fois (dimension mg:gta, 2 min)
execute if score $setup mg.st matches 1 unless data storage mg:gta built run schedule function mg:gta/world_build 45s
scoreboard players set $gtw mg.st 0
# $rp a été écrasé par rank/xp (il servait de variable temporaire, corrigé) : remis à 1 une seule fois
execute unless data storage mg:rank rpfix run scoreboard players set $rp mg.st 1
data modify storage mg:rank rpfix set value 1b
scoreboard objectives add mg.t dummy
scoreboard objectives add mg.wins dummy [{"text":"✦ Victoires ✦","color":"gold"}]
scoreboard objectives add mg.stp dummy
scoreboard objectives add mg.stk playerKillCount
scoreboard objectives add mg.deaths deathCount
scoreboard objectives add mg.cs minecraft.used:minecraft.carrot_on_a_stick
scoreboard objectives add mg.us minecraft.used:minecraft.snowball
scoreboard objectives add mg.menu trigger
scoreboard objectives add mg.go trigger
scoreboard objectives add mg.cd dummy
scoreboard objectives add mg.cls trigger
scoreboard objectives add mg.cl dummy
scoreboard objectives add mg.svx dummy
scoreboard objectives add mg.svy dummy
scoreboard objectives add mg.svz dummy
scoreboard objectives add mg.opt trigger
scoreboard objectives add mg.buy trigger
scoreboard objectives add mg.mb dummy [{"text":"☠ MOB ARENA ☠","color":"red"}]
scoreboard objectives add mg.tw dummy
scoreboard objectives add mg.ts dummy [{"text":"▮ TURF WARS ▮","color":"gold"}]
scoreboard objectives add mg.pb dummy [{"text":"▓ PAINTBALL — % peint ▓","color":"gold"}]
scoreboard objectives add mg.pi dummy
scoreboard objectives add mg.ph dummy
scoreboard objectives add mg.pt dummy
scoreboard objectives add mg.ak dummy
scoreboard objectives add mg.ag dummy
scoreboard objectives add mg.cp dummy
scoreboard objectives add mg.lp dummy
scoreboard objectives add mg.ri dummy
scoreboard objectives add mg.rp dummy [{"text":"⛵ COURSE — progression %","color":"aqua"}]
scoreboard objectives add mg.vote trigger
scoreboard objectives add mg.bb trigger
scoreboard objectives add mg.bw trigger
scoreboard objectives add mg.uoi minecraft.mined:minecraft.iron_ore
scoreboard objectives add mg.uog minecraft.mined:minecraft.gold_ore
scoreboard objectives add mg.uod minecraft.mined:minecraft.diamond_ore
scoreboard objectives add mg.uor minecraft.mined:minecraft.redstone_ore
scoreboard objectives add mg.uol minecraft.mined:minecraft.lapis_ore
scoreboard objectives add mg.sjp dummy
team add mg_at
team modify mg_at friendlyFire false
team modify mg_at nametagVisibility always
scoreboard objectives add mg.atl dummy {"text":"🚗 Coups restants","color":"aqua","bold":true}
scoreboard objectives add mg.atp dummy
scoreboard objectives add mg.atid dummy
scoreboard objectives add mg.atx dummy
scoreboard objectives add mg.atz dummy
scoreboard objectives add mg.atv dummy
scoreboard objectives add mg.atc dummy
scoreboard objectives add mg.pco dummy {"text":"💰 Pièces (arène PvP)","color":"gold"}
scoreboard objectives add mg.pkc playerKillCount
scoreboard objectives add mg.pks dummy
scoreboard objectives add mg.phc dummy
scoreboard objectives add mg.pdt minecraft.custom:minecraft.damage_taken
scoreboard objectives add mg.pshop trigger
scoreboard objectives add mg.pvid dummy
scoreboard objectives add mg.pcl dummy
execute if score $setup mg.st matches 1 unless data storage mg:lobby pvpc2 run schedule function mg:pvpc/build_start 22s
team add mg_sq
team modify mg_sq friendlyFire false
team modify mg_sq collisionRule never
team modify mg_sq nametagVisibility always
scoreboard objectives add mg.sqx dummy
scoreboard objectives add mg.sqy dummy
scoreboard objectives add mg.sqz dummy
function mg:golf/load
scoreboard objectives add mg.blu minecraft.used:minecraft.warped_fungus_on_a_stick
scoreboard objectives add mg.bln dummy
scoreboard objectives add mg.bcx dummy
scoreboard objectives add mg.bx dummy
scoreboard objectives add mg.bz dummy
scoreboard objectives add mg.bvx dummy
scoreboard objectives add mg.bvz dummy
scoreboard objectives add mg.bsp dummy
scoreboard objectives add mg.bph dummy
scoreboard objectives add mg.btm dummy
scoreboard objectives add mg.bfr dummy
scoreboard objectives add mg.brl dummy
scoreboard objectives add mg.bpw dummy
scoreboard objectives add mg.bpd dummy
scoreboard objectives add mg.bk dummy
scoreboard objectives add mg.br1 dummy
scoreboard objectives add mg.br2 dummy
scoreboard objectives add mg.bfs dummy
scoreboard objectives add mg.bcu dummy
scoreboard objectives add mg.bp1f dummy
scoreboard objectives add mg.bp1s dummy
scoreboard objectives add mg.bp1n dummy
scoreboard objectives add mg.bp2f dummy
scoreboard objectives add mg.bp2s dummy
scoreboard objectives add mg.bp2n dummy
scoreboard objectives add mg.bxs dummy
scoreboard objectives add mg.bsc dummy {"text":"🎳 Bowling","color":"light_purple"}
scoreboard objectives add mg.tnc dummy
scoreboard objectives add mg.tns dummy
scoreboard objectives add mg.tnx dummy
scoreboard objectives add mg.tny dummy
scoreboard objectives add mg.tnz dummy
scoreboard objectives add mg.tnvx dummy
scoreboard objectives add mg.tnvy dummy
scoreboard objectives add mg.tnvz dummy
scoreboard objectives add mg.tnb dummy
scoreboard objectives add mg.tnl dummy
scoreboard objectives add mg.tnph dummy
scoreboard objectives add mg.tnt dummy
scoreboard objectives add mg.tnp1 dummy
scoreboard objectives add mg.tnp2 dummy
scoreboard objectives add mg.tng1 dummy
scoreboard objectives add mg.tng2 dummy
scoreboard objectives add mg.tngw dummy {"text":"🎾 Jeux gagnés","color":"yellow"}
scoreboard objectives add mg.phn minecraft.used:minecraft.goat_horn
scoreboard objectives add mg.pid dummy
scoreboard objectives add mg.php dummy
scoreboard objectives add mg.phx dummy
scoreboard objectives add mg.phz dummy
scoreboard objectives add mg.phs dummy
team add mg_cm
team modify mg_cm nametagVisibility never
team modify mg_cm friendlyFire false
team modify mg_cm collisionRule never
team modify mg_cm color green
scoreboard objectives add mg.cmid dummy
scoreboard objectives add mg.cmq minecraft.used:minecraft.warped_fungus_on_a_stick
scoreboard objectives add mg.cmp trigger
scoreboard objectives add mg.cmo trigger
scoreboard objectives add mg.cmpo dummy
scoreboard objectives add mg.cmpt dummy
scoreboard objectives add mg.cmst dummy
scoreboard objectives add mg.cmlx dummy
scoreboard objectives add mg.cmly dummy
scoreboard objectives add mg.cmlz dummy
scoreboard objectives add mg.cmdl dummy
scoreboard objectives add mg.cmdn dummy
scoreboard objectives add mg.cmtc dummy
scoreboard objectives add mg.cmgc dummy
scoreboard objectives add mg.cmpts dummy
scoreboard objectives add mg.cmf dummy
scoreboard objectives add mg.gcas trigger
scoreboard objectives add mg.gcre dummy
scoreboard objectives add mg.gsa dummy
scoreboard objectives add mg.gsr dummy
scoreboard objectives add mg.gsb dummy
scoreboard objectives add mg.gs1 dummy
scoreboard objectives add mg.gs2 dummy
scoreboard objectives add mg.gs3 dummy
scoreboard objectives add mg.gcas trigger
scoreboard objectives add mg.gcre dummy
scoreboard objectives modify mg.gta displayname [{"text":"💵 Neo GTA","color":"green","bold":true},{"text":" : les plus riches","color":"gray","bold":false}]
scoreboard objectives add mg.gmis trigger
scoreboard objectives add mg.gmt dummy
scoreboard objectives add mg.gms dummy
scoreboard objectives add mg.gmtime dummy
scoreboard objectives add mg.gmsec dummy
scoreboard objectives add mg.gnit dummy
scoreboard objectives add mg.gth dummy
scoreboard objectives add mg.gtn dummy
scoreboard objectives add mg.gttx dummy
scoreboard objectives add mg.gttz dummy
scoreboard objectives add mg.gtmod dummy
scoreboard objectives add mg.gtw8 dummy
scoreboard objectives add mg.grob dummy
scoreboard objectives add mg.gsid dummy
scoreboard objectives add mg.gveh dummy
scoreboard objectives add mg.gqs minecraft.used:minecraft.warped_fungus_on_a_stick
scoreboard objectives add mg.gta dummy {"text":"💵 Dollars","color":"green","bold":true}
scoreboard objectives add mg.gwl dummy {"text":"★ recherché","color":"gold"}
scoreboard objectives add mg.gwt dummy
scoreboard objectives add mg.grk dummy
scoreboard objectives add mg.gpt dummy
scoreboard objectives add mg.gtl dummy
scoreboard objectives add mg.gal dummy
scoreboard objectives add mg.gpc dummy
scoreboard objectives add mg.gvid dummy
scoreboard objectives add mg.gpx dummy
scoreboard objectives add mg.gpz dummy
scoreboard objectives add mg.gkp playerKillCount
scoreboard objectives add mg.gkv minecraft.killed:minecraft.villager
scoreboard objectives add mg.gks minecraft.killed:minecraft.skeleton
scoreboard objectives add mg.gkw minecraft.killed:minecraft.wither_skeleton
scoreboard objectives add mg.cvrt dummy
scoreboard objectives add mg.bmb dummy {"text":"💣 Dégâts","color":"red","bold":true}
scoreboard objectives add mg.bid dummy
scoreboard objectives add mg.bty dummy
scoreboard objectives add mg.bc1 dummy
scoreboard objectives add mg.bc2 dummy
scoreboard objectives add mg.bc3 dummy
scoreboard objectives add mg.bc4 dummy
scoreboard objectives add mg.trc dummy
scoreboard objectives add mg.trs dummy
scoreboard objectives add mg.trj dummy
scoreboard players set #1 mg.st 1
scoreboard objectives add mg.rt trigger
scoreboard objectives add mg.rts dummy
scoreboard objectives add mg.rtn dummy
scoreboard objectives add mg.rgs dummy
scoreboard objectives add mg.rgn dummy
scoreboard objectives add mg.rfs dummy
scoreboard objectives add mg.rfn dummy
function mg:rate/init
team add mg_ph
team modify mg_ph nametagVisibility never
team modify mg_ph friendlyFire false
team modify mg_ph collisionRule never
scoreboard players set #4 mg.st 4
scoreboard objectives add mg.pid dummy
scoreboard objectives add mg.fx dummy
scoreboard objectives add mg.fy dummy
scoreboard objectives add mg.fz dummy
scoreboard objectives add mg.php dummy
scoreboard objectives add mg.phx dummy
scoreboard objectives add mg.phz dummy
scoreboard objectives add mg.phs dummy
scoreboard players set #2 mg.st 2
scoreboard players set #3 mg.st 3
scoreboard players set #5 mg.st 5
scoreboard players set #8 mg.st 8
scoreboard players set #60 mg.st 60
scoreboard objectives add mg.zpt dummy {"text":"🧟 Points","color":"dark_green"}
scoreboard objectives add mg.zk minecraft.killed:minecraft.zombie
scoreboard objectives add mg.gcd dummy
scoreboard objectives add mg.grl dummy
scoreboard objectives add mg.grt dummy
scoreboard objectives add mg.gsn minecraft.custom:minecraft.sneak_time
scoreboard objectives add mg.g1 dummy
scoreboard objectives add mg.g2 dummy
scoreboard objectives add mg.g3 dummy
scoreboard objectives add mg.g4 dummy
scoreboard objectives add mg.g5 dummy
scoreboard objectives add mg.g6 dummy
scoreboard players set #7 mg.st 7
scoreboard players set #11 mg.st 11
scoreboard players set #30 mg.st 30
scoreboard objectives add mg.cf dummy {"text":"🚩 Drapeaux","color":"gold"}
scoreboard objectives add mg.tw dummy {"text":"🏰 The Towers","color":"gold"}
scoreboard objectives add mg.kh dummy {"text":"👑 Colline","color":"gold"}
scoreboard objectives add mg.trc dummy
scoreboard objectives add mg.trs dummy
scoreboard objectives add mg.tel trigger
scoreboard objectives add mg.ti dummy
scoreboard objectives add mg.tc dummy
scoreboard objectives add mg.tx dummy
scoreboard objectives add mg.tz dummy
scoreboard objectives add mg.tpt dummy {"text":"📞 Points","color":"gold"}
scoreboard objectives add mg.bi dummy
scoreboard objectives add mg.br dummy
scoreboard objectives add mg.ba dummy
scoreboard objectives add mg.vc dummy
scoreboard objectives add mg.vb dummy [{"text":"☑ VOTES — prochain jeu","color":"green"}]
scoreboard objectives add mg.fw minecraft.used:minecraft.blaze_rod
scoreboard objectives add mg.wc minecraft.used:minecraft.wind_charge
scoreboard objectives add mg.wd dummy
scoreboard objectives add mg.fd dummy
scoreboard objectives add mg.ec dummy
scoreboard objectives add mg.et dummy
scoreboard objectives add mg.eg dummy
scoreboard objectives add mg.est dummy
scoreboard objectives add mg.erb dummy
scoreboard objectives add mg.ehw dummy
scoreboard objectives add mg.ecr dummy
scoreboard objectives add mg.erb2 dummy
scoreboard objectives add mg.ok dummy [{"text":"➶ KILLS — 10 pour gagner","color":"gold"}]
scoreboard objectives add mg.qk dummy [{"text":"⚡ QUAKECRAFT ⚡","color":"aqua"}]
scoreboard objectives add mg.ppc dummy
scoreboard objectives add mg.ppt dummy
scoreboard objectives add mg.ppb dummy
scoreboard objectives add mg.ppf dummy
scoreboard objectives add mg.ks dummy
scoreboard objectives add mg.gi dummy
scoreboard objectives add mg.qp dummy
scoreboard objectives add mg.qs minecraft.used:minecraft.warped_fungus_on_a_stick
scoreboard objectives add mg.dp dummy [{"text":"★","color":"gold"}]
scoreboard objectives add mg.ln dummy
scoreboard objectives add mg.lv dummy [{"text":"♥","color":"red"}]
function mg:core/load_lg
function mg:core/load_pk
function mg:core/load_hp
function mg:elyrace/objectives
scoreboard objectives add mg.pl trigger
scoreboard objectives add mg.plot dummy
scoreboard objectives add mg.pcx dummy
scoreboard objectives add mg.pcz dummy
scoreboard objectives add mg.dice trigger
scoreboard objectives add mg.dz minecraft.used:minecraft.echo_shard
scoreboard objectives add mg.mpm dummy [{"text":"● PIÈCES (★ sous le pseudo)","color":"gold"}]
scoreboard objectives add mg.mpk dummy [{"text":"★","color":"yellow"}]
scoreboard objectives add mg.mpi dummy
scoreboard objectives add mg.mpo dummy
scoreboard objectives add mg.mpz dummy
scoreboard objectives add mg.mpv dummy
scoreboard objectives add mg.mid dummy
scoreboard objectives add mg.mit dummy
scoreboard objectives add mg.mip dummy
scoreboard objectives add mg.sv trigger
scoreboard objectives add mg.kty dummy
scoreboard objectives add mg.kcol dummy
scoreboard objectives add mg.kbl dummy
scoreboard objectives add mg.kch trigger
scoreboard objectives add mg.krl dummy
scoreboard objectives add mg.ksp dummy
scoreboard objectives add mg.kdr dummy
scoreboard objectives add mg.kdd dummy
scoreboard objectives add mg.kbo dummy
scoreboard objectives add mg.khi dummy
scoreboard objectives add mg.kst dummy
scoreboard objectives add mg.kit dummy
scoreboard objectives add mg.kcp dummy
scoreboard objectives add mg.klp dummy
scoreboard objectives add mg.kvy dummy
scoreboard objectives add mg.kfp dummy
scoreboard objectives add mg.kpg dummy
scoreboard objectives add mg.krk dummy
scoreboard objectives add mg.krc dummy
scoreboard objectives add mg.khd dummy
scoreboard objectives add mg.kspr dummy
scoreboard objectives add mg.kvm dummy
scoreboard objectives add mg.kv trigger
scoreboard objectives add mg.kstk dummy
scoreboard objectives add mg.kof dummy
scoreboard objectives add mg.klt dummy
scoreboard objectives add mg.klb dummy
scoreboard objectives add mg.lcd dummy
scoreboard objectives add mg.esn dummy
scoreboard objectives add mg.esc dummy
scoreboard objectives add mg.est dummy
scoreboard objectives add mg.eup dummy
scoreboard objectives add mg.ebl dummy
scoreboard objectives add mg.ept dummy
scoreboard objectives add mg.kic dummy
scoreboard objectives add mg.kgd dummy
scoreboard objectives add mg.kbill dummy
scoreboard objectives add mg.kboo dummy
scoreboard objectives add mg.kmg dummy
scoreboard objectives add mg.kmap dummy [{"text":"🗺 Circuit Champignon","color":"gold","bold":true}]
scoreboard objectives modify mg.kmap numberformat blank
scoreboard objectives modify mg.kmap displayname [{"text":"🗺 Circuit Champignon","color":"gold","bold":true}]
scoreboard objectives add mg.kps dummy [{"text":"🏎 KART : progression %","color":"gold"}]
scoreboard objectives add mg.svid dummy
scoreboard objectives add mg.svvx dummy

# --- Équipes ---
team add mg_red
team modify mg_red color red
team modify mg_red friendlyFire false
team modify mg_red prefix [{"text":"⬤ ","color":"red"}]
team add mg_blue
team modify mg_blue color blue
team modify mg_blue friendlyFire false
team modify mg_blue prefix [{"text":"⬤ ","color":"blue"}]
team add mg_green
team modify mg_green color green
team modify mg_green friendlyFire false
team modify mg_green prefix [{"text":"⬤ ","color":"green"}]
team add mg_yellow
team modify mg_yellow color yellow
team modify mg_yellow friendlyFire false
team modify mg_yellow prefix [{"text":"⬤ ","color":"yellow"}]
team add mg_party
team modify mg_party friendlyFire false
team modify mg_party collisionRule never

# --- Globals par défaut (seulement si absents) ---
execute unless score $state mg.st = $state mg.st run scoreboard players set $state mg.st 0
execute unless score $game mg.st = $game mg.st run scoreboard players set $game mg.st 0
execute unless score $timer mg.st = $timer mg.st run scoreboard players set $timer mg.st 0
execute unless score $sb mg.st = $sb mg.st run scoreboard players set $sb mg.st 0
execute unless score $setup mg.st = $setup mg.st run scoreboard players set $setup mg.st 0
execute unless score $tc mg.st = $tc mg.st run scoreboard players set $tc mg.st 0
execute unless score $pn mg.st = $pn mg.st run scoreboard players set $pn mg.st 0
execute unless score $mp mg.st = $mp mg.st run scoreboard players set $mp mg.st 0
execute unless score $svc mg.st = $svc mg.st run scoreboard players set $svc mg.st 0
# Règles du serveur (survie + mini-jeux) réappliquées à chaque chargement
execute if score $setup mg.st matches 1 run function mg:core/rules
execute if score $setup mg.st matches 1 unless data storage mg:kart built run schedule function mg:kart/build 5s
execute if score $setup mg.st matches 1 if data storage mg:kart built unless data storage mg:kart built2 run schedule function mg:kart/t2/build 8s
execute if score $setup mg.st matches 1 if data storage mg:kart built2 unless data storage mg:kart built3 run schedule function mg:kart/t3/build 10s
# Reconstructions automatiques après une mise à jour (numéro de version dans le stockage)
execute if score $setup mg.st matches 1 unless data storage mg:dropadv v3 run schedule function mg:dropadv/build 40s
execute if score $setup mg.st matches 1 run scoreboard players set $xbk mg.st 0
execute if score $setup mg.st matches 1 run schedule function mg:elyrace/build_next 60s
execute if score $setup mg.st matches 1 unless data storage mg:hall v14 run schedule function mg:hall/build 20s
execute if score $setup mg.st matches 1 unless data storage mg:lobby v6 run schedule function mg:lobby/build 10s
execute if score $setup mg.st matches 1 unless data storage mg:lobby v6 run schedule function mg:lobby/food_build 25s
execute if score $setup mg.st matches 1 unless data storage mg:lobby v6 run schedule function mg:elytra/build 30s
execute if score $setup mg.st matches 1 unless data storage mg:lobby food1 run schedule function mg:lobby/food_build 12s
execute if score $setup mg.st matches 1 unless data storage mg:lobby coaster4 run schedule function mg:coaster/build_start 16s
execute if score $setup mg.st matches 1 unless data storage mg:lobby beacon1 run schedule function mg:lobby/beacons 18s
execute if score $setup mg.st matches 1 unless data storage mg:lobby ely1 run schedule function mg:elytra/build 14s
execute if score $setup mg.st matches 1 unless data storage mg:lobby elyclean run schedule function mg:elytra/spawn_clean 9s

# Zones chargées (après une mise à jour du pack, les nouvelles zones sont prises en compte)
execute if score $setup mg.st matches 1 run function mg:core/forceloads

# Plots joueurs : construits automatiquement après une mise à jour du pack sur un monde déjà installé
execute if score $setup mg.st matches 1 unless data storage mg:plot built run function mg:plot/build
execute if score $setup mg.st matches 1 unless data storage mg:party {built:3b} run schedule function mg:party/build 3s

tellraw @a [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Datapack chargé. ","color":"gray"},{"text":"Première fois ? Un OP lance ","color":"gray"},{"text":"/function mg:setup","color":"yellow"},{"text":" pour tout construire.","color":"gray"}]

# Monde de survie : difficulté normale et apparition des monstres.
# Sur Paper, difficulté et règles de jeu sont propres à chaque monde : le
# « difficulty normal » du setup ne touche que le monde principal, mg:survie
# restait en paisible. Réappliqué à chaque chargement du datapack.
execute in mg:survie run difficulty normal
execute in mg:survie run gamerule spawn_mobs true

# Classements par mini-jeu + tableau à droite affiché par défaut (une seule fois ; masquable au menu)
function mg:hall/objectives
# Mini-jeu Élytra + suivi des reconnexions + tableaux de partie
function mg:sky/load
scoreboard objectives add mg.seen dummy
scoreboard objectives add mg.sbg dummy
execute unless data storage mg:hall sbon run scoreboard players set $sb mg.st 1
data modify storage mg:hall sbon set value 1b
function mg:version/load
execute unless score $rp mg.st matches 0.. run function mg:core/rp_default
execute if score $setup mg.st matches 1 unless data storage mg:lobby deco3 run schedule function mg:lobby/deco 6s
