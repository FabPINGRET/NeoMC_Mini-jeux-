"""Contre-la-montre solo de la Course d'elytres, partie DEROULEMENT (le lancement est dans solo.py). Chaque joueur en solo (tag mg.xso) a son
propre tick, appele par core/tick (branchement : wire_elyrace4.py) tant qu'au moins un joueur porte le tag. Phases (mg.xph) : 1 decompte,
2 course, 3 arrivee, 4 choix (Rejouer ou lobby, 30 s) ; mg.xst = chrono du joueur (ticks depuis le lancement, le GO, l'arrivee ou le choix selon la phase), mg.xsl = dernier tick ou
il etait en ligne. Le solo n'ecrit jamais $state, $game, $timer, ni ne lit $xc ou $xt : la course d'un joueur ne depend que de ses scores.
Deux passes par tick : `seen` sur @a (voit aussi un joueur sur l'ecran de mort : sa presence ne doit pas disparaitre) puis `step` sur
@e[type=player] (ignore le joueur mort pendant la reapparition : respawn le replacerait deux fois).
SEULE ENTREE en course : solo/go (phase 2, meme apres « Rejouer » : solo/arm repasse par le decompte). SEULE SORTIE : solo/stop (tag retire, pause d'avant retablie,
retour au lobby) ; la phase 4 (solo/choice, solo/wait) attend le joueur sans rien quitter ; aucune
teleportation vers l'avant ailleurs que place_tp, respawn et le lobby. La gravite de course est posee par solo/go (grav_on) et remise a la
normale par solo/stop (core/attr_reset_g).
Fonctions generees : elyrace/solo/{tick, seen, step, countdown, go, finish, choice, wait, stop}. Python stdlib uniquement (compatible 3.8).
"""
import course_common as CC
import game as G
import menus as M

COUNT = 100              # decompte : 5 s (mg.xst de 0 a 100)
END_TIMER = 30           # ticks de phase 3 (arrivee) avant le choix (phase 4)
CHOICE_WAIT = 600        # ticks de phase 4 (choix : Rejouer ou lobby) avant le retour automatique au lobby (30 s)
PLUS_30 = G.TIME_LIMIT - 600     # « plus que 30 secondes » (mg.xst)
LEFT = (('mg.surv', 'Tu es parti en survie'), ('mg.inplot', 'Tu es parti sur ton plot'), ('mg.visit', 'Tu es parti en visite de plot'))
# activités du lobby ouvertes pendant un solo (tag, début du message) : fin du solo, sans retour au lobby ; solo.py doit refuser chacune au lancement


def msg(text, color='gray'):
    return '{"text":"%s","color":"%s"}' % (text, color)


def tick_lines():
    return ['# Tick des contre-la-montre solo (core/tick, si au moins un joueur porte mg.xso) : deux passes, voir solo_run.py',
            'execute as @a[tag=mg.xso] run function mg:elyrace/solo/seen',
            'execute as @e[type=player,tag=mg.xso] run function mg:elyrace/solo/step']


def seen_lines():
    out = ['# @s = joueur en solo, mort ou vivant (@a) : activité quittée, présence, pause, chrono',
           '# le joueur est parti en survie, dans un plot ou en visite (ces activités étaient fermées par mg.play avant le solo par joueur) :',
           '# fin du solo AVANT toute règle de course (c<N>/player le verrait hors zone et c<N>/respawn le ramènerait sur le parcours) ;',
           '# stop ne le ramène pas au lobby. survie/tick passe avant solo/tick (survie vue au même tick), plot/cmd après (vu au tick suivant)']
    for tag, why in LEFT:
        out.append('execute if entity @s[tag=%s] run tellraw @s [%s]' % (tag, msg('%s : contre-la-montre terminé.' % why)))
        out.append('execute if entity @s[tag=%s] run return run function mg:elyrace/solo/stop' % tag)
    return out + ['# reconnexion : mg.xsl doit valoir le tick précédent ($tc - 1), sinon le joueur n\'était pas en ligne (core/reconnect l\'a déjà remis au lobby)',
                  'scoreboard players operation #xsl mg.st = $tc mg.st',
                  'scoreboard players remove #xsl mg.st 1',
                  'execute unless score @s mg.xsl = #xsl mg.st run return run function mg:elyrace/solo/stop',
                  '# pause désactivée à la main (mg.spectate retiré) : fin du solo',
                  'execute unless entity @s[tag=mg.spectate] run tellraw @s [%s]' % msg('▶ Pause désactivée : contre-la-montre terminé.'),
                  'execute unless entity @s[tag=mg.spectate] run return run function mg:elyrace/solo/stop',
                  'scoreboard players operation @s mg.xsl = $tc mg.st',
                  'scoreboard players add @s mg.xst 1']


def step_lines(specs):
    out = ['# @s = joueur en solo, vivant (@e[type=player]) : filet, décompte, course, arrivée',
           '# filet : une partie l\'a pris comme participant (ne devrait pas arriver, il est en pause) : le solo s\'arrête',
           'execute if entity @s[tag=mg.play] run return run function mg:elyrace/solo/stop',
           '# lobby/wind_used (charge de vent) donne slow_falling : retiré, il fausserait la glisse',
           'effect clear @s minecraft:slow_falling',
           'execute if score @s mg.xph matches 1 run return run function mg:elyrace/solo/countdown',
           '# phase 3 (arrivée) : %d ticks pour lire le temps, puis phase 4 (choix) ; aucune règle de course' % END_TIMER,
           'execute if score @s mg.xph matches 3 if score @s mg.xst matches %d.. run return run function mg:elyrace/solo/choice' % END_TIMER,
           'execute if score @s mg.xph matches 3 run return 0',
           '# phase 4 (choix : Rejouer ou lobby) : AVANT c<N>/player, donc ni détection de course, ni HUD, ni anneaux, ni mur, ni arrivée',
           'execute if score @s mg.xph matches 4 run return run function mg:elyrace/solo/wait',
           '# phase 2 : le tick du parcours (règles, anneaux, reprises), puis HUD et limite de temps',
           '# (l\'arrivée a pu passer le joueur en phase 3 pendant ce tick : plus de HUD ni de limite)']
    out += CC.per_course(specs, 'player')
    out += ['execute unless score @s mg.xph matches 2 run return 0',
            'scoreboard players operation #xm mg.st = @s mg.xst',
            'scoreboard players operation #xm mg.st %= #k10 mg.st',
            'execute if score #xm mg.st matches 0 run function mg:elyrace/hud',
            'execute if score @s mg.xst matches %d run tellraw @s [%s]' % (PLUS_30, msg('🪽 Plus que 30 secondes !', 'gold')),
            'execute if score @s mg.xst matches %d.. run tellraw @s [%s]' % (G.TIME_LIMIT, msg('⏱ Temps écoulé (3 minutes) : contre-la-montre terminé sans arrivée.')),
            'execute if score @s mg.xst matches %d.. run function mg:elyrace/solo/stop' % G.TIME_LIMIT]
    return out


def countdown_lines():
    out = ['# @s = joueur en décompte (phase 1, 5 s) : titres et sons pour lui seul ; mg.xst = ticks depuis le lancement (titre 5 au lancement)']
    for t, n, col, pitch in ((20, 4, 'yellow', '1'), (40, 3, 'gold', '1.2'), (60, 2, 'red', '1.4'), (80, 1, 'dark_red', '1.6')):
        out.append('execute if score @s mg.xst matches %d run title @s title [{"text":"%d","color":"%s","bold":true}]' % (t, n, col))
        out.append('execute if score @s mg.xst matches %d at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 %s' % (t, pitch))
    return out + ['execute if score @s mg.xst matches %d.. run function mg:elyrace/solo/go' % COUNT]


def go_lines(specs):
    out = ['# @s = joueur : GO ! SEULE ENTRÉE en course (phase 2, chrono à 0). Même départ que core/begin puis elyrace/go, pour lui seul',
           'effect clear @s minecraft:slowness',
           'effect clear @s minecraft:resistance',
           'function mg:core/unfreeze',
           'effect give @s minecraft:instant_health 1 10 true',
           'effect give @s minecraft:saturation 1 9 true',
           'title @s title [{"text":"GO !","color":"green","bold":true}]',
           'execute at @s run playsound minecraft:event.raid.horn master @s ~ ~ ~ 0.7 1.4',
           'effect give @s minecraft:resistance infinite 4 true',
           'effect give @s minecraft:saturation infinite 0 true',
           '# portillon de son parcours (ouvert pour tous les solos du parcours : ils sont gelés tant que le décompte dure)']
    out += CC.per_course(specs, 'gate_off')
    out += CC.per_course(specs, 'go_text')
    out += ['# gravité de course de son parcours (comme go pour le groupe) ; solo/stop la remet à la normale', G.GRAV_ON]
    return out +['scoreboard players set @s mg.xst 0', 'scoreboard players set @s mg.xph 2']


def finish_lines(specs):
    return ['# @s = joueur qui franchit l\'anneau d\'arrivée en solo (appelé en 1re ligne de elyrace/finish) : annonce, records, phase 3',
            '# temps = chrono du joueur moins le bonus de ses anneaux d\'or (elyrace/bonus : #xgs = secondes retirées)',
            'scoreboard players operation #xrt mg.st = @s mg.xst',
            'function mg:elyrace/bonus',
            'scoreboard players operation #s mg.st = #xrt mg.st', 'scoreboard players operation #s mg.st /= #k20 mg.st',
            'tellraw @s [{"text":"🏁 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" passe la ligne d\'arrivée (","color":"gray"},'
            '{"score":{"name":"#s","objective":"mg.st"},"color":"white"},{"text":" s)","color":"gray"}]',
            'execute if score @s mg.xu matches 1.. run tellraw @s ' + G.BONUS_TELLRAW,
            'title @s subtitle ""',                # efface un sous-titre resté (« ★ -2 s », choc) : il s'afficherait sous « Arrivée ! »
            'title @s title [{"text":"🏁 Arrivée !","color":"gold","bold":true}]',
            'execute at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1',
            'execute at @s run particle minecraft:firework ~ ~1 ~ 1 1 1 0.2 60',
            '# records : le temps est lu dans #xrt, personnel puis serveur, selon son parcours (mg.xcr)'] + CC.per_course(specs, 'record') + [
            '# phase 3 : le chrono repart à 0 pour compter %d ticks, puis solo/choice (le temps de l\'arrivée est déjà enregistré)' % END_TIMER,
            'scoreboard players set @s mg.xph 3',
            'scoreboard players set @s mg.xst 0']


def choice_lines():
    return ['# @s = joueur dont la phase 3 (arrivée) se termine : PHASE 4, choix entre rejouer (solo/retry) et le lobby (solo/quit, ou solo/wait au bout de %d s).' % (CHOICE_WAIT // 20),
            '# Pas de stop : le tag, la pause et le parcours restent. Seule l\'arrivée y passe (la limite de 3 minutes, elle, arrête le solo : pas de nouvelle tentative)',
            '# gravité normale (plus de vol), retour sur sa place de départ, gel (le même que le décompte ; solo/retry le lève avant solo/arm)',
            G.GRAV_RESET,
            'function mg:elyrace/place_tp',
            'function mg:core/freeze',
            'scoreboard players set @s mg.xph 4',
            'scoreboard players set @s mg.xst 0',
            'tellraw @s [{"text":"🏁 Et maintenant ? ","color":"gold"},'
            '{"text":"[⟲ Rejouer]","color":"green","bold":true,"click_event":{"action":"run_command","command":"trigger mg.xs set %d"},'
            '"hover_event":{"action":"show_text","value":"Relancer le même parcours tout de suite"}},{"text":" ","color":"gray"},'
            '{"text":"[⌂ Retour au lobby]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.xs set %d"},'
            '"hover_event":{"action":"show_text","value":"Quitter le contre-la-montre"}},'
            '{"text":" (lobby automatique dans %d s)","color":"gray"}]' % (M.SOLO_RETRY, M.SOLO_QUIT, CHOICE_WAIT // 20),
            'execute at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.2']


def wait_lines():
    return ['# @s = joueur en phase 4 (choix ; appelée par step avant toute règle de course) : à %d ticks (%d s) sans clic, retour au lobby ;' % (CHOICE_WAIT, CHOICE_WAIT // 20),
            '# sinon compte à rebours dans la barre d\'action, une fois par seconde (mg.xst = ticks depuis le début du choix)',
            'execute if score @s mg.xst matches %d.. run tellraw @s [%s]' % (CHOICE_WAIT, msg('⌂ Pas de réponse : retour au lobby.')),
            'execute if score @s mg.xst matches %d.. run return run function mg:elyrace/solo/stop' % CHOICE_WAIT,
            'scoreboard players operation #xm mg.st = @s mg.xst',
            'scoreboard players operation #xm mg.st %= #k20 mg.st',
            'execute unless score #xm mg.st matches 0 run return 0',
            'scoreboard players set #xw mg.st %d' % CHOICE_WAIT,
            'scoreboard players operation #xw mg.st -= @s mg.xst',
            'scoreboard players operation #xw mg.st /= #k20 mg.st',
            'title @s actionbar [{"text":"⟲ Rejouer ou retour au lobby : ","color":"gray"},{"score":{"name":"#xw","objective":"mg.st"},"color":"white"},{"text":" s","color":"gray"}]']


def stop_lines():
    return ['# @s = joueur : SEULE SORTIE d\'un contre-la-montre solo (arrivée + %d ticks, puis choix terminé ou quitté, abandon, pause désactivée, survie / plot / visite, 3 min,' % END_TIMER,
            '# reconnexion, arrêt admin, départ d\'une course de groupe, désinstallation). Rien d\'autre ne retire mg.xso.',
            '# 1) plus aucune détection : le tag et les scores de course d\'abord (mg.xse, délai de 30 s, est posé plus bas)',
            'tag @s remove mg.xso',
            'scoreboard players reset @s mg.xph',
            'scoreboard players reset @s mg.xst',
            'scoreboard players reset @s mg.xsl',
            '# (mg.xcr appartient à la partie de groupe si une partie l\'a pris comme participant)',
            'execute unless entity @s[tag=mg.play] run scoreboard players reset @s mg.xcr',
            '# gravité normale (0,08), sans condition : celle de course (elyrace/grav_on) ne doit pas suivre le joueur au lobby',
            G.GRAV_RESET,
            '# 2) la pause d\'avant le solo : rétablie (mg.xsp0 = il était déjà en pause ; sinon la pause est retirée, même si une partie tourne)',
            'execute unless entity @s[tag=mg.xsp0] run tag @s remove mg.spectate',
            'tag @s remove mg.xsp0',
            'scoreboard players operation @s mg.xse = $tc mg.st',
            '# 3) retour au lobby, sauf si une partie l\'a pris (participant, ou spectateur placé par core/reconnect_spec)',
            '# ou s\'il est parti en survie, dans un plot ou en visite (reset_player l\'y arracherait : position de survie corrompue, boucle avec le plot)',
            'function mg:core/unfreeze',
            'execute %s run function mg:core/reset_player' % ' '.join('unless entity @s[tag=%s]' % t for t in ('mg.play', 'mg.out') + tuple(t for t, _ in LEFT)),
            '# plot ou visite : le point de réapparition du parcours ne doit pas rester (même point que reset_player ; survie : survie/restore l\'a déjà posé)',
            'execute if entity @s[tag=mg.inplot] in minecraft:overworld run spawnpoint @s 0 64 0',
            'execute if entity @s[tag=mg.visit] in minecraft:overworld run spawnpoint @s 0 64 0']


def functions(specs):
    return {'solo/tick': tick_lines(), 'solo/seen': seen_lines(), 'solo/step': step_lines(specs), 'solo/countdown': countdown_lines(),
            'solo/go': go_lines(specs), 'solo/finish': finish_lines(specs), 'solo/choice': choice_lines(), 'solo/wait': wait_lines(),
            'solo/stop': stop_lines()}
