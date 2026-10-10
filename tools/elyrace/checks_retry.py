"""Controles statiques de la phase 4 du solo (choix) et de « Rejouer » (appeles par checks_solo.problems) : retry ne fait que rearmer par solo/arm,
la phase 4 n'est atteinte que par l'arrivee et n'est jamais traitee par la logique de course. Aucun import de checks_solo ni de checks
(checks_solo lui passe son fn_code). Python stdlib uniquement (compatible 3.8).
"""
import re

import course_common as CC
import game as G
import menus as M
import solo_run as SR

RETRY_FORBIDDEN = (r'mg\.xse\b', r'mg\.xsp0\b', r'mg\.xsi\b', r'spectate', r'mg\.ri\b', r'tag @s add mg\.xso\b', r'solo/start', r'solo/stop', r'announce')   # retry ne relance rien d'autre que arm
ARM_NEED = ('function mg:elyrace/equip', 'function mg:elyrace/place_tp', 'function mg:core/freeze')    # l'equipement et le depart gele d'une tentative
STEP_EARLY = ('execute if score @s mg.xph matches 1 run return run function mg:elyrace/solo/countdown', 'execute if score @s mg.xph matches 3 run return 0')


def retry_problems(files, specs, fn_code):
    """retry ne fait que rearmer (solo/arm : tout l'etat de course remis a zero), jamais relancer ni arreter ; la phase 4 n'est atteinte que par l'arrivee
    (la limite de 3 minutes arrete le solo : pas de nouvelle tentative) et les phases 1, 3 et 4 sont traitees AVANT c<N>/player (aucune detection de course)."""
    bad, retry, step, wait = [], fn_code(files, 'solo/retry'), fn_code(files, 'solo/step'), fn_code(files, 'solo/wait')
    for line in retry:
        for pat in RETRY_FORBIDDEN:
            if re.search(pat, line):
                bad.append('solo/retry : ne doit pas toucher a %s (rearmer seulement) : %s' % (pat, line))
    arm = 'function mg:elyrace/solo/arm'
    gates = ['execute unless entity @s[tag=mg.xso] run return run tellraw @s ', 'execute unless score @s mg.xph matches 4 run return run tellraw @s ']
    idx = [[i for i, l in enumerate(retry) if l.startswith(g)] for g in gates]
    if retry.count(arm) != 1 or retry[-1:] != [arm]:
        bad.append('solo/retry : doit finir par un unique appel a solo/arm (%s)' % arm)
    if not all(idx) or (arm in retry and max(max(i) for i in idx) > retry.index(arm)):
        bad.append('solo/retry : refus absents ou apres solo/arm (hors contre-la-montre, hors phase 4 : %s)' % gates)
    if arm not in fn_code(files, 'solo/start'):
        bad.append('solo/start : doit armer le joueur par solo/arm (%s)' % arm)
    cmd = fn_code(files, 'solo/cmd')
    for line in ('execute if score #xv mg.st matches %d run function mg:elyrace/solo/retry' % M.SOLO_RETRY,
                 'execute if score #xv mg.st matches %d if score @s mg.xph matches 4 run function mg:elyrace/solo/stop' % M.SOLO_LOBBY):
        if line not in cmd:       # [Retour au lobby] : arret en phase 4 SEULEMENT (un vieux lien du chat n'abandonne pas une autre tentative)
            bad.append('solo/cmd : ligne absente : %s' % line)
    armed = fn_code(files, 'solo/arm')
    for n, _, _ in G.OBJECTIVES:        # tout l'etat de course (ors mg.xu / mg.xo, classement mg.xft, arrivee mg.xf, reprise, balayage...) est remis a zero a chaque tentative
        if not any(l.startswith('scoreboard players set @s mg.%s ' % n) for l in armed):
            bad.append('solo/arm : ne remet pas mg.%s a zero (Rejouer garderait l\'etat de la tentative precedente)' % n)
    bad += ['solo/arm : ligne absente : %s' % l for l in ARM_NEED if l not in armed]
    choice = fn_code(files, 'solo/choice')
    for need in (G.GRAV_RESET, 'function mg:elyrace/place_tp', 'function mg:core/freeze'):
        if need not in choice:
            bad.append('solo/choice : ligne absente : %s' % need)
    if any('solo/stop' in l or 'mg.xso' in l for l in choice):
        bad.append('solo/choice : la phase 4 attend le joueur, elle ne retire ni ne pose mg.xso et n\'arrete pas le solo')
    calls = [l for l in step if 'function mg:elyrace/solo/choice' in l]
    if len(calls) != 1 or 'mg.xph matches 3 ' not in calls[0]:
        bad.append('solo/step : doit appeler solo/choice une seule fois, a l\'arrivee (phase 3) : %s' % calls)
    limit = 'execute if score @s mg.xst matches %d.. run function mg:elyrace/solo/stop' % G.TIME_LIMIT
    if limit not in step:
        bad.append('solo/step : la limite de 3 minutes doit rester un solo/stop (pas de nouvelle tentative) : %s' % limit)
    race = [step.index(l) for l in CC.per_course(specs, 'player') if l in step]
    gate = 'execute if score @s mg.xph matches 4 run return run function mg:elyrace/solo/wait'
    for line in STEP_EARLY + (gate,):
        if line not in step or not race or step.index(line) > min(race):
            bad.append('solo/step : la phase (decompte, arrivee, choix) doit etre traitee AVANT c<N>/player (aucune detection de course) : %s' % line)
    go = fn_code(files, 'solo/go')
    for s in specs:        # intro du depart : 1re tentative seulement (tag mg.xsi), puis le tag part (une ligne `execute ... execute` serait invalide)
        line = 'execute if entity @s[tag=mg.xsi] if score @s mg.xcr matches %d run function %s' % (s.NUM, CC.fn(s, 'go_text'))
        if line not in go:
            bad.append('solo/go : ligne absente : %s' % line)
    if 'tag @s remove mg.xsi' not in go or any('go_text' in l and 'tag=mg.xsi' not in l for l in go):
        bad.append('solo/go : le texte du depart doit etre garde par mg.xsi, et mg.xsi retire par go')
    if 'tag @s add mg.xsi' not in fn_code(files, 'solo/start') or 'tag @s remove mg.xsi' not in fn_code(files, 'solo/stop'):
        bad.append('mg.xsi : pose par solo/start, retire par solo/stop (et par uninstall via G.SOLO_TAGS)')
    back = 'execute if score @s mg.xst matches %d.. run return run function mg:elyrace/solo/stop' % SR.CHOICE_WAIT
    if back not in wait:
        bad.append('solo/wait : le retour au lobby apres %d ticks est absent : %s' % (SR.CHOICE_WAIT, back))
    return bad
