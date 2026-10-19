"""🐉 Ombrelune : créatures articulées (dragons), données partagées par gen_ombrelune.py et tools/resourcepack/ol_rp.py.

Même moteur que les dinosaures de Terra Nova (tv_dinos : os, articulations, poses précalculées, quatre états d'animation),
avec un gabarit de dragon : quadrupède au long cou, cornes, piques dorsales, deux grandes ailes articulées, queue en trois parties.
"""
import math

import tv_dinos as T
from tv_dinos import Bone, Species, FRAMES, STATES, poses, bone_scale, bone_extent  # noqa: F401

SPECIES = {}


def reg(sp):
    SPECIES[sp.key] = sp
    return sp


def dragon(key, label, color, mats, s=1.0, body=(1.1, 0.95, 2.4), hip=1.25, shoulder=1.3, neck=(0.42, 1.5, 38), head=(0.55, 0.45, 1.0),
           tail=(0.4, 2.2), leg=(0.3, 0.34), wing=3.2, horns=0.55):
    bw, bh, bl = (v * s for v in body)
    nw, nl, nang = neck[0] * s, neck[1] * s, neck[2]
    hw, hh, hl = (v * s for v in head)
    tw, tl = tail[0] * s, tail[1] * s
    Hh, Hs = hip * s, shoulder * s
    lf, lh = leg[0] * s, leg[1] * s
    B = []
    body_b = Bone('body', None, (0, Hh, 0), anim='body', amp=1.4)
    body_b.box(-bw / 2, -bh * 0.42, -bl * 0.45, bw / 2, -bh * 0.08, bl * 0.5, 'belly')
    body_b.box(-bw / 2 - 0.005, -bh * 0.08, -bl * 0.47, bw / 2 + 0.005, bh * 0.52, bl * 0.52, 'skin')
    body_b.box(-bw * 0.4, bh * 0.52, -bl * 0.42, bw * 0.4, bh * 0.64, bl * 0.45, 'skin')
    for i in range(6):                                               # piques dorsales
        z = -bl * 0.4 + i * bl * 0.16
        body_b.box(-0.05 * s, bh * 0.64, z, 0.05 * s, bh * 0.64 + (0.32 - 0.03 * abs(i - 2.5)) * s, z + 0.14 * s, 'spike')
    B.append(body_b)
    # cou en deux parties, tête, mâchoire
    n1 = Bone('neck', 'body', (0, (Hs - Hh) + bh * 0.25, bl * 0.46), rest=(-nang, 0, 0), anim='neck', amp=0.8)
    n1.box(-nw / 2, -nw / 2, -nw * 0.3, nw / 2, nw / 2, nl * 0.55, 'skin')
    n1.box(-nw * 0.38, -nw / 2 - 0.01, 0, nw * 0.38, -nw * 0.2, nl * 0.55, 'belly')
    n1.box(-0.04 * s, nw / 2, nl * 0.15, 0.04 * s, nw / 2 + 0.18 * s, nl * 0.28, 'spike')
    B.append(n1)
    n2 = Bone('neck2', 'neck', (0, 0, nl * 0.5), rest=(nang * 0.35, 0, 0), anim='neck', amp=0.6, phase=0.6)
    n2.box(-nw * 0.45, -nw * 0.45, -0.05, nw * 0.45, nw * 0.45, nl * 0.5, 'skin')
    n2.box(-nw * 0.34, -nw * 0.45 - 0.01, 0, nw * 0.34, -nw * 0.18, nl * 0.5, 'belly')
    n2.box(-0.04 * s, nw * 0.45, nl * 0.2, 0.04 * s, nw * 0.45 + 0.15 * s, nl * 0.32, 'spike')
    B.append(n2)
    hd = Bone('head', 'neck2', (0, 0, nl * 0.5), rest=(nang * 0.6, 0, 0), anim='head')
    hd.box(-hw / 2, -hh * 0.25, -hh * 0.35, hw / 2, hh * 0.65, hl * 0.55, 'skin')
    hd.box(-hw * 0.38, -hh * 0.2, hl * 0.55, hw * 0.38, hh * 0.38, hl, 'skin')
    hd.box(-hw / 2 - 0.012, hh * 0.3, hl * 0.28, hw / 2 + 0.012, hh * 0.48, hl * 0.42, 'eye')
    hd.box(-hw * 0.34, -hh * 0.27, hl * 0.42, hw * 0.34, -hh * 0.2, hl * 0.96, 'teeth')
    hd.box(-hw * 0.12, hh * 0.38, hl * 0.86, -hw * 0.04, hh * 0.46, hl * 0.95, 'dark')
    hd.box(hw * 0.04, hh * 0.38, hl * 0.86, hw * 0.12, hh * 0.46, hl * 0.95, 'dark')
    for sx in (-1, 1):                                              # cornes rejetées vers l'arrière
        hd.box(sx * hw * 0.22, hh * 0.55, -hh * 0.2, sx * hw * 0.38, hh * 0.72, hl * 0.25, 'horn')
        hd.box(sx * hw * 0.26, hh * 0.62, -hh * 0.35 - horns * s, sx * hw * 0.36, hh * 0.72, -hh * 0.2, 'horn')
        hd.box(sx * hw * 0.5, -hh * 0.05, -hh * 0.1, sx * hw * 0.62, hh * 0.25, hl * 0.3, 'spike')
    B.append(hd)
    jw = Bone('jaw', 'head', (0, -hh * 0.25, -hh * 0.2), anim='jaw', amp=1.1)
    jw.box(-hw * 0.4, -hh * 0.3, 0, hw * 0.4, 0, hl * 0.95, 'belly')
    jw.box(-hw * 0.3, 0, hl * 0.45, hw * 0.3, 0.05 * s, hl * 0.92, 'teeth')
    B.append(jw)
    # queue en trois parties
    t1 = Bone('tail', 'body', (0, bh * 0.2, -bl * 0.45), rest=(-10, 0, 0), anim='tail', amp=0.8)
    t1.box(-tw / 2, -tw / 2, -tl * 0.36, tw / 2, tw / 2, 0.05, 'skin')
    t1.box(-0.04 * s, tw / 2, -tl * 0.3, 0.04 * s, tw / 2 + 0.2 * s, -tl * 0.18, 'spike')
    B.append(t1)
    t2 = Bone('tail2', 'tail', (0, 0, -tl * 0.35), rest=(-6, 0, 0), anim='tail', amp=1.2, phase=-0.8)
    t2.box(-tw * 0.36, -tw * 0.36, -tl * 0.36, tw * 0.36, tw * 0.36, 0.03, 'skin')
    t2.box(-0.035 * s, tw * 0.36, -tl * 0.28, 0.035 * s, tw * 0.36 + 0.16 * s, -tl * 0.16, 'spike')
    B.append(t2)
    t3 = Bone('tail3', 'tail2', (0, 0, -tl * 0.35), rest=(-3, 0, 0), anim='tail', amp=1.6, phase=-1.6)
    t3.box(-tw * 0.24, -tw * 0.24, -tl * 0.34, tw * 0.24, tw * 0.24, 0.02, 'skin')
    t3.box(-tw * 0.55, -0.03 * s, -tl * 0.42, tw * 0.55, 0.03 * s, -tl * 0.28, 'spike')   # pointe en fer de lance
    B.append(t3)
    # pattes
    for nm_, sx, z, top, w_, ph in (('armL', 1, bl * 0.32, Hs - Hh, lf, 0.0), ('armR', -1, bl * 0.32, Hs - Hh, lf, math.pi),
                                     ('legL', 1, -bl * 0.3, 0, lh, math.pi), ('legR', -1, -bl * 0.3, 0, lh, 0.0)):
        L = Hs if nm_.startswith('arm') else Hh
        lg = Bone(nm_, 'body', (sx * (bw / 2 - w_ * 0.3), top, z), anim='leg', amp=0.7, phase=ph)
        lg.box(-w_ / 2, -L * 0.55, -w_ / 2, w_ / 2, bh * 0.12, w_ / 2, 'skin')
        B.append(lg)
        kn = Bone(('fore' if nm_.startswith('arm') else 'shin') + nm_[-1], nm_, (0, -L * 0.52, 0), anim='knee', amp=0.5, phase=ph)
        kn.box(-w_ * 0.4, -L * 0.48, -w_ * 0.4, w_ * 0.4, 0.02, w_ * 0.4, 'skin')
        kn.box(-w_ * 0.5, -L * 0.5, -w_ * 0.45, w_ * 0.5, -L * 0.42, w_ * 0.75, 'dark')
        kn.box(-w_ * 0.42, -L * 0.5, w_ * 0.75, w_ * 0.42, -L * 0.45, w_ * 0.95, 'claw')
        B.append(kn)
    # ailes : bras (os, membrane) + pointe
    ws = wing * s
    for nm_, sx in (('wingL', 1), ('wingR', -1)):
        wb = Bone(nm_, 'body', (sx * bw * 0.42, bh * 0.5, bl * 0.22), rest=(0, 0, sx * 12), anim=nm_, amp=1.0)
        wb.box(0, -0.06 * s, -0.08 * s, sx * ws * 0.5, 0.06 * s, 0.08 * s, 'dark')               # humérus
        wb.box(0, -0.025 * s, -ws * 0.42, sx * ws * 0.5, 0.025 * s, 0, 'wing')                     # membrane
        B.append(wb)
        wt = Bone(nm_ + 't', nm_, (sx * ws * 0.5, 0, 0), rest=(0, 0, -sx * 8), anim=nm_, amp=0.8, phase=-0.6)
        wt.box(0, -0.05 * s, -0.06 * s, sx * ws * 0.55, 0.05 * s, 0.06 * s, 'dark')
        wt.box(0, -0.02 * s, -ws * 0.55, sx * ws * 0.55, 0.02 * s, 0, 'wing')
        for k in range(3):                                                                       # doigts
            wt.box(sx * ws * (0.15 + 0.18 * k), -0.03 * s, -ws * (0.2 + 0.12 * k), sx * ws * (0.18 + 0.18 * k), 0.03 * s, 0, 'dark')
        wt.box(sx * ws * 0.52, -0.05 * s, 0.0, sx * ws * 0.6, 0.05 * s, 0.18 * s, 'claw')
        B.append(wt)
    return Species(key, label, color, mats, B, s)


def M(**kw):
    base = {'teeth': ((236, 230, 210), 'teeth', 'white_concrete'), 'claw': ((40, 34, 30), 'solid', 'black_terracotta'),
            'eye': ((255, 190, 30), 'eye', 'yellow_concrete'), 'dark': ((36, 30, 28), 'scales', 'black_terracotta')}
    base.update(kw)
    return base


reg(dragon('ignarok', 'Ignarok, dragon de feu', 'red', M(
    skin=((150, 40, 26), 'scales', 'red_terracotta'), belly=((222, 150, 60), 'plates', 'orange_terracotta'),
    wing=((110, 30, 22), 'wing', 'red_concrete'), spike=((40, 28, 24), 'solid', 'black_terracotta'), horn=((60, 44, 36), 'solid', 'brown_terracotta'),
    eye=((255, 220, 60), 'eye', 'yellow_concrete')), s=2.1))
reg(dragon('nyxar', 'Nyxar, dragon de la Lune Noire', 'dark_purple', M(
    skin=((44, 30, 66), 'scales', 'purple_terracotta'), belly=((110, 90, 140), 'plates', 'magenta_terracotta'),
    wing=((30, 18, 48), 'wing', 'black_concrete'), spike=((180, 160, 230), 'solid', 'purpur_block'), horn=((210, 200, 240), 'solid', 'white_terracotta'),
    eye=((120, 220, 255), 'eye', 'light_blue_concrete')), s=2.5, wing=3.6, horns=0.7))
reg(dragon('drake', 'Drake des braises', 'gold', M(
    skin=((120, 70, 40), 'scales', 'brown_terracotta'), belly=((200, 140, 80), 'plates', 'orange_terracotta'),
    wing=((90, 50, 30), 'wing', 'brown_concrete'), spike=((50, 30, 20), 'solid', 'black_terracotta'), horn=((70, 50, 40), 'solid', 'brown_terracotta')),
    s=0.85, wing=2.6, horns=0.4))
