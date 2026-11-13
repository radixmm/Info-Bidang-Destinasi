#!/usr/bin/env python3
"""Sisipkan ilustrasi (banner pemandangan Jawa Timur, ikon kartu, hiasan ombak)
ke template halaman "Info Bidang Destinasi".

Bisa dipakai pada build.py (TEMPLATE di dalamnya) maupun pada halaman HTML hasil
build. Idempoten: file yang sudah berilustrasi tidak diubah lagi.

  python3 ilustrasi.py MASUK KELUAR
"""
import sys

PENANDA = "hero-art"

CSS = r"""
/* ===== Ilustrasi ===== */
:root { --sky1:#0d1626; --sky2:#2a2131; --glow:rgba(217,89,38,.35); --sun:#f08a4b; --cloud:rgba(255,255,255,.07); --star:rgba(255,255,255,.75);
  --m1:#2a3247; --m2:#1f2a35; --m3:#18251f; --m4:#12201a; --terr:#24402f; --sea:#18304d; --sea2:#2c5482; --candi:#3a3036; --wall:#d9cfc0; --roof:#c4532a; --bird:#c9c4bb; --smoke:rgba(255,255,255,.18); }
@media (prefers-color-scheme: light) { :root:not([data-theme="dark"]) { --sky1:#cfe5fa; --sky2:#fdebd6; --glow:rgba(246,160,77,.35); --sun:#f6a04d; --cloud:rgba(255,255,255,.85); --star:transparent;
  --m1:#a9c3dc; --m2:#86b9a0; --m3:#5aa27c; --m4:#3a8660; --terr:#8fcaa2; --sea:#6aaee0; --sea2:#b5dcf7; --candi:#8d6b57; --wall:#fffaf2; --roof:#e0623a; --bird:#4b4a46; --smoke:rgba(255,255,255,.9); } }
:root[data-theme="light"] { --sky1:#cfe5fa; --sky2:#fdebd6; --glow:rgba(246,160,77,.35); --sun:#f6a04d; --cloud:rgba(255,255,255,.85); --star:transparent;
  --m1:#a9c3dc; --m2:#86b9a0; --m3:#5aa27c; --m4:#3a8660; --terr:#8fcaa2; --sea:#6aaee0; --sea2:#b5dcf7; --candi:#8d6b57; --wall:#fffaf2; --roof:#e0623a; --bird:#4b4a46; --smoke:rgba(255,255,255,.9); }
:root[data-theme="dark"] { --sky1:#0d1626; --sky2:#2a2131; --glow:rgba(217,89,38,.35); --sun:#f08a4b; --cloud:rgba(255,255,255,.07); --star:rgba(255,255,255,.75);
  --m1:#2a3247; --m2:#1f2a35; --m3:#18251f; --m4:#12201a; --terr:#24402f; --sea:#18304d; --sea2:#2c5482; --candi:#3a3036; --wall:#d9cfc0; --roof:#c4532a; --bird:#c9c4bb; --smoke:rgba(255,255,255,.18); }
.hero { position: relative; overflow: hidden; border-radius: 18px; border: 1px solid var(--line); padding: 20px 20px clamp(138px, 19vw, 205px);
  background:
    radial-gradient(1.4px 1.4px at 12% 18%, var(--star) 60%, transparent 62%), radial-gradient(1.2px 1.2px at 27% 9%, var(--star) 60%, transparent 62%),
    radial-gradient(1.6px 1.6px at 44% 22%, var(--star) 60%, transparent 62%), radial-gradient(1.1px 1.1px at 63% 12%, var(--star) 60%, transparent 62%),
    radial-gradient(1.5px 1.5px at 78% 26%, var(--star) 60%, transparent 62%), radial-gradient(1.2px 1.2px at 91% 8%, var(--star) 60%, transparent 62%),
    radial-gradient(1.3px 1.3px at 55% 34%, var(--star) 60%, transparent 62%), radial-gradient(120% 70% at 62% 100%, var(--glow), transparent 70%),
    linear-gradient(180deg, var(--sky1), var(--sky2)); }
.hero-txt { position: relative; z-index: 1; max-width: 40rem; display: grid; gap: 4px; }
.hero-txt .logo { margin-bottom: 6px; }
.hero .eyebrow { color: var(--fg); opacity: .8; }
.hero p { color: var(--fg); opacity: .78; }
.hero-art { position: absolute; left: 0; right: 0; bottom: 0; width: 100%; height: clamp(150px, 24vw, 260px); display: block; pointer-events: none; }
.hero-art .sun { fill: var(--sun); } .hero-art .glow { fill: var(--sun); opacity: .22; }
.hero-art .cloud { fill: var(--cloud); } .hero-art .m1 { fill: var(--m1); } .hero-art .m2 { fill: var(--m2); } .hero-art .m3 { fill: var(--m3); } .hero-art .m4 { fill: var(--m4); }
.hero-art .terr { fill: none; stroke: var(--terr); stroke-width: 2; stroke-linecap: round; }
.hero-art .sea { fill: var(--sea); } .hero-art .wave { fill: none; stroke: var(--sea2); stroke-width: 2; stroke-linecap: round; }
.hero-art .candi { fill: var(--candi); } .hero-art .wall { fill: var(--wall); } .hero-art .roof { fill: var(--roof); } .hero-art .door { fill: var(--candi); }
.hero-art .bridge { fill: none; stroke: var(--candi); stroke-width: 2.2; } .hero-art .tower { fill: var(--candi); }
.hero-art .bird { fill: none; stroke: var(--bird); stroke-width: 1.8; stroke-linecap: round; stroke-linejoin: round; }
.hero-art .smoke { fill: var(--smoke); } .hero-art .sail { fill: var(--c2); } .hero-art .hull { fill: var(--candi); }
.hero-art .trunk { fill: none; stroke: var(--candi); stroke-width: 3; stroke-linecap: round; } .hero-art .frond { fill: var(--m4); }
.hero-art .drift { animation: ibd-drift 38s ease-in-out infinite alternate; } .hero-art .drift2 { animation: ibd-drift 52s ease-in-out infinite alternate-reverse; }
.hero-art .bob { animation: ibd-bob 4.5s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }
.hero-art .puff { animation: ibd-puff 6s ease-in-out infinite; }
@keyframes ibd-drift { from { transform: translateX(-30px); } to { transform: translateX(40px); } }
@keyframes ibd-bob { 0%,100% { transform: translateY(0) rotate(-1.5deg); } 50% { transform: translateY(3px) rotate(1.5deg); } }
@keyframes ibd-puff { 0%,100% { opacity: .55; } 50% { opacity: 1; } }
.ch h2 { flex: 1; min-width: 0; }
.ill { flex: none; width: 46px; height: 46px; border-radius: 13px; display: grid; place-items: center; background: var(--grid); background: color-mix(in srgb, var(--tint, var(--c1)) 15%, transparent); transition: transform .25s ease; }
.ill svg { width: 38px; height: 38px; display: block; }
.card:hover .ill { transform: rotate(-5deg) scale(1.06); }
.ill .a { fill: var(--c1); } .ill .b { fill: var(--c2); } .ill .c { fill: var(--c3); } .ill .d { fill: var(--c4); } .ill .p { fill: var(--panel); } .ill .f { fill: var(--fg); } .ill .m { fill: var(--muted-bar); }
.ill .sk { stroke: var(--fg); stroke-opacity: .18; stroke-width: 1.2; } .ill .ps { stroke: var(--panel); stroke-width: 2; }
.ill .ln { fill: none; stroke: var(--muted-bar); stroke-width: 1.5; } .ill .ck { fill: none; stroke: #fff; stroke-width: 2.4; stroke-linecap: round; stroke-linejoin: round; }
.ill .sf { fill: none; stroke: var(--fg); stroke-width: 2.4; stroke-linecap: round; stroke-linejoin: round; }
.ill .sb { fill: none; stroke: var(--c2); stroke-width: 2.2; stroke-linecap: round; stroke-linejoin: round; }
.ill .sa { fill: none; stroke: var(--c1); stroke-width: 2.2; stroke-linecap: round; stroke-linejoin: round; }
.ill .dash { fill: none; stroke: var(--muted-bar); stroke-width: 1.6; stroke-dasharray: 2.5 3; stroke-linecap: round; }
.ombak { display: block; width: 100%; height: 34px; margin-bottom: -8px; }
.ombak .w1 { fill: none; stroke: var(--c1); stroke-opacity: .35; stroke-width: 2; } .ombak .w2 { fill: none; stroke: var(--c3); stroke-opacity: .35; stroke-width: 2; }
.ombak .sail { fill: var(--c2); opacity: .7; } .ombak .hull { fill: var(--muted-bar); }
@media (prefers-reduced-motion: reduce) { .hero-art .drift, .hero-art .drift2, .hero-art .bob, .hero-art .puff { animation: none; } .ill { transition: none; } }
"""

HERO_SVG = r"""<svg class="hero-art" viewBox="0 0 1200 220" preserveAspectRatio="xMidYMax slice" aria-hidden="true" focusable="false">
      <circle class="glow" cx="760" cy="74" r="64"/><circle class="sun" cx="760" cy="74" r="34"/>
      <g class="drift"><path class="cloud" d="M60 84a16 16 0 0 1 30-8a20 20 0 0 1 36 6a13 13 0 0 1 4 26h-66a14 14 0 0 1-4-24z"/></g>
      <g class="drift2"><path class="cloud" d="M880 30a14 14 0 0 1 26-6a18 18 0 0 1 32 6a11 11 0 0 1 3 22h-58a12 12 0 0 1-3-22z"/><path class="cloud" d="M640 64a10 10 0 0 1 18-4a12 12 0 0 1 22 4a8 8 0 0 1 2 15h-40a8 8 0 0 1-2-15z"/></g>
      <g class="bird"><path d="M842 40q6-6 12 0q6-6 12 0"/><path d="M872 26q5-5 10 0q5-5 10 0"/><path d="M898 46q4-4 8 0q4-4 8 0"/></g>
      <path class="m1" d="M0 120L70 108L140 94L210 104L280 84L340 92L410 76L480 90L560 78L640 92L720 84L820 98L905 100L985 42Q1000 34 1015 36L1030 42L1112 100L1200 108V220H0Z"/>
      <g class="puff"><circle class="smoke" cx="1006" cy="26" r="7"/><circle class="smoke" cx="1020" cy="15" r="9"/><circle class="smoke" cx="1040" cy="8" r="6"/></g>
      <path class="m2" d="M0 152C60 142 120 134 170 130L250 98L268 93L282 102L298 93L318 97L392 130C440 138 500 134 540 132C600 128 660 142 720 140C800 136 860 148 920 152C1000 152 1100 142 1200 148V220H0Z"/>
      <g class="puff"><circle class="smoke" cx="283" cy="88" r="5"/><circle class="smoke" cx="292" cy="78" r="6"/></g>
      <g class="candi"><rect x="534" y="114" width="52" height="20" rx="2"/><rect x="541" y="100" width="38" height="16" rx="2"/><rect x="547" y="88" width="26" height="14" rx="2"/><rect x="553" y="78" width="14" height="12" rx="2"/><path d="M556 78L560 62L564 78Z"/></g>
      <path class="sea" d="M760 168C860 160 1000 158 1200 160V220H760Z"/>
      <path class="wave" d="M880 184q10-6 20 0t20 0M980 196q10-6 20 0t20 0M1090 180q10-6 20 0t20 0"/>
      <rect class="tower" x="898" y="128" width="6" height="42" rx="1"/><rect class="tower" x="1058" y="128" width="6" height="42" rx="1"/>
      <path class="bridge" d="M812 166Q860 150 901 130Q981 170 1061 130Q1110 150 1170 166M812 166H1180M921 140V166M941 150V166M961 157V166M1001 157V166M1021 150V166M1041 140V166"/>
      <g class="bob"><path class="hull" d="M1096 196h40l-6 8h-28z"/><path class="sail" d="M1116 194V170l16 24z"/><path class="sail" d="M1113 194V176l-11 18z" opacity=".75"/></g>
      <path class="m3" d="M330 220C380 176 440 160 520 158C600 156 680 164 740 172C780 178 810 190 830 220Z"/>
      <g><rect class="wall" x="612" y="160" width="34" height="18"/><path class="roof" d="M604 162L616 146H642L654 162Z"/><path class="roof" d="M620 146L629 136L638 146Z"/><rect class="door" x="625" y="166" width="8" height="12"/>
        <rect class="wall" x="666" y="166" width="26" height="14"/><path class="roof" d="M660 168L670 154H688L698 168Z"/><rect class="door" x="676" y="170" width="6" height="10"/></g>
      <path class="trunk" d="M732 178Q736 160 730 144"/><g class="frond"><path d="M730 144q-16-2-24 8q12-6 24-4z"/><path d="M730 144q16-4 26 4q-14-2-26 0z"/><path d="M730 144q-6-12 2-20q-2 10 0 20z"/><path d="M730 144q10-10 22-8q-12 2-22 8z"/></g>
      <path class="m4" d="M0 220V168C80 158 160 156 240 162C320 168 380 176 460 174C520 172 560 184 600 220Z"/>
      <path class="terr" d="M20 188C100 178 180 178 260 184C330 189 390 196 450 196M40 204C120 196 200 196 280 200C340 204 400 210 460 212"/>
      <path class="trunk" d="M190 170Q196 148 188 128"/><g class="frond"><path d="M188 128q-18-2-26 10q14-7 26-5z"/><path d="M188 128q18-5 28 4q-15-2-28 1z"/><path d="M188 128q-7-14 3-22q-3 11-1 22z"/><path d="M188 128q12-11 24-8q-13 2-24 8z"/></g>
    </svg>"""

OMBAK_SVG = r"""<svg class="ombak" viewBox="0 0 1200 34" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path class="w1" d="M0 20q25-12 50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0"/><path class="w2" d="M0 28q25-10 50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0t50 0"/></svg>"""

ICON_JS = r"""
  // Ilustrasi ikon kartu
  const ILL = {
    agenda: ['--c1', '<rect x="7" y="10" width="34" height="31" rx="6" class="p sk"/><path d="M7 16a6 6 0 0 1 6-6h22a6 6 0 0 1 6 6v5H7z" class="a"/><rect x="14" y="6" width="4" height="9" rx="2" class="f"/><rect x="30" y="6" width="4" height="9" rx="2" class="f"/><g class="m"><rect x="12" y="25" width="6" height="5" rx="1.5"/><rect x="21" y="25" width="6" height="5" rx="1.5"/><rect x="12" y="32" width="6" height="5" rx="1.5"/><rect x="21" y="32" width="6" height="5" rx="1.5"/></g><rect x="30" y="25" width="6" height="5" rx="1.5" class="b"/><circle cx="36" cy="37" r="8" class="c ps"/><path d="M32.5 37l2.5 2.5 4.5-5" class="ck"/>'],
    tim: ['--c3', '<circle cx="14" cy="19" r="5" class="c"/><path d="M5 38c0-6 4-10 9-10s9 4 9 10z" class="c"/><circle cx="34" cy="19" r="5" class="b"/><path d="M25 38c0-6 4-10 9-10s9 4 9 10z" class="b"/><circle cx="24" cy="15" r="6" class="a ps"/><path d="M12 42c0-7 5-12 12-12s12 5 12 12z" class="a ps"/>'],
    geopark: ['--c3', '<circle cx="21" cy="10" r="3" class="m"/><circle cx="27" cy="6.5" r="3.6" class="m"/><circle cx="33" cy="4.5" r="2.6" class="m"/><path d="M3 41L18 18Q20 15 23 15H25Q28 15 30 18L45 41Z" class="c"/><path d="M11.5 29H36.5L40 34H8Z" class="d"/><path d="M8 34H40L45 41H3Z" class="b"/><path d="M19.5 17.6Q24 22.5 28.5 17.6Q26.5 15 24 15Q21.5 15 19.5 17.6Z" class="b"/>'],
    kunjungan: ['--c2', '<path d="M7 15Q15 5 27 9" class="dash"/><rect x="7" y="21" width="26" height="20" rx="4" class="b"/><path d="M15 21v-4a3 3 0 0 1 3-3h4a3 3 0 0 1 3 3v4" class="sf"/><rect x="12" y="21" width="3" height="20" class="p" opacity=".5"/><rect x="25" y="21" width="3" height="20" class="p" opacity=".5"/><g transform="translate(27 3) scale(.8) rotate(45 12 12)"><path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 0 0-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5z" class="a"/></g>'],
    dtw: ['--c1', '<path d="M4 15L16 11L32 15L44 11V37L32 41L16 37L4 41Z" class="p sk"/><path d="M4 31Q11 25 17 29T32 27T44 23V37L32 41L16 37L4 41Z" class="c" opacity=".7"/><path d="M16 11V37M32 15V41" class="ln"/><path d="M24 4a8.5 8.5 0 0 1 8.5 8.5C32.5 19 24 27 24 27S15.5 19 15.5 12.5A8.5 8.5 0 0 1 24 4z" class="b"/><circle cx="24" cy="12.5" r="3.2" class="p"/>'],
    dw2025: ['--c3', '<circle cx="11" cy="10" r="4" class="d"/><path d="M2 40Q24 30 46 40V46H2Z" class="c"/><rect x="8" y="25" width="15" height="12" class="p sk"/><path d="M5 26L11.5 17H19.5L26 26Z" class="b"/><rect x="13.5" y="29" width="4" height="8" class="d"/><rect x="29" y="28" width="11" height="10" class="p sk"/><path d="M27 29L32 22H37L42 29Z" class="a"/><rect x="40.5" y="16" width="2" height="10" class="m"/><circle cx="41.5" cy="15" r="5" class="c"/>'],
    dw2026: ['--c3', '<path d="M40 3l1.4 3.6L45 8l-3.6 1.4L40 13l-1.4-3.6L35 8l3.6-1.4z" class="d"/><path d="M2 40Q24 30 46 40V46H2Z" class="c"/><rect x="6" y="24" width="16" height="13" class="p sk"/><path d="M3 25L10 15H18L25 25Z" class="a"/><path d="M10 15L14 10L18 15Z" class="a"/><rect x="12" y="29" width="4" height="8" class="d"/><rect x="27" y="27" width="13" height="11" class="p sk"/><path d="M25 28L30.5 20H36.5L42 28Z" class="b"/><rect x="31.5" y="31" width="4" height="7" class="d"/>'],
    kalender: ['--c4', '<path d="M24 4V9M24 23V28M12 16H17M31 16H36M15.5 7.5L19 11M29 21L32.5 24.5M32.5 7.5L29 11M19 21L15.5 24.5" class="sb"/><circle cx="24" cy="16" r="3.2" class="d"/><path d="M38 26V29M38 37V40M31 33H34M42 33H45" class="sa"/><path d="M5 31H29V35A3 3 0 0 0 29 41V45H5V41A3 3 0 0 0 5 35Z" class="c"/><path d="M12 31V45" class="dash" style="stroke:var(--panel)"/>'],
    wbtb: ['--c4', '<path d="M14 11L18 4L22 9L24 3L26 9L30 4L34 11" class="sa"/><path d="M8 14Q24 4 40 14Q42 30 24 45Q6 30 8 14Z" class="d"/><path d="M12 16Q17 12 22 16M26 16Q31 12 36 16" class="sb"/><path d="M13 21Q17 17.5 21 21Q17 24 13 21Z" class="f"/><path d="M27 21Q31 17.5 35 21Q31 24 27 21Z" class="f"/><path d="M24 22V29L22 31" class="sf" style="stroke-width:2"/><path d="M18 35Q24 39 30 35" class="sf"/><circle cx="14" cy="29" r="2.2" class="b"/><circle cx="34" cy="29" r="2.2" class="b"/>'],
    ipkn: ['--c1', '<path d="M24 3.5l2.1 4.4 4.8.6-3.6 3.3 1 4.8L24 14.2l-4.3 2.4 1-4.8-3.6-3.3 4.8-.6z" class="d"/><rect x="18" y="20" width="12" height="22" rx="2" class="a"/><rect x="6" y="27" width="12" height="15" rx="2" class="c"/><rect x="30" y="31" width="12" height="11" rx="2" class="b"/><rect x="4" y="42" width="40" height="2.5" rx="1.2" class="m"/>'],
    imti: ['--c3', '<rect x="5" y="16" width="4" height="27" class="c"/><path d="M4 16L7 9L10 16Z" class="d"/><rect x="39" y="16" width="4" height="27" class="c"/><path d="M38 16L41 9L44 16Z" class="d"/><rect x="12" y="27" width="24" height="16" class="p sk"/><path d="M12 27Q12 15 24 11Q36 15 36 27Z" class="c"/><path d="M20 43V37a4 4 0 0 1 8 0V43Z" class="c"/><path d="M24 11V7" class="sf" style="stroke-width:1.6"/><path d="M24.5 1.5a3 3 0 1 0 2.6 4.6a2.4 2.4 0 1 1-2.6-4.6z" class="d"/>'],
    capaian: ['--c4', '<path d="M14 3H22L27 19H19Z" class="a"/><path d="M34 3H26L21 19H29Z" class="b"/><circle cx="24" cy="30" r="13" class="d"/><circle cx="24" cy="30" r="9.5" class="p" opacity=".35"/><path d="M24 23.5l2 4.1 4.5.6-3.3 3.1.8 4.5L24 33.6l-4 2.2.8-4.5-3.3-3.1 4.5-.6z" class="p"/>']
  };
  Object.keys(ILL).forEach((id) => {
    const ch = document.querySelector('#' + id + ' .ch');
    if (!ch || ch.querySelector('.ill')) return;
    const box = document.createElement('div'); box.className = 'ill'; box.setAttribute('aria-hidden', 'true');
    box.style.setProperty('--tint', 'var(' + ILL[id][0] + ')');
    box.innerHTML = '<svg viewBox="0 0 48 48" focusable="false">' + ILL[id][1] + '</svg>';
    ch.insertBefore(box, ch.firstChild);
  });
"""


def ganti_sekali(teks, lama, baru):
    if teks.count(lama) != 1:
        raise SystemExit("GAGAL: penanda %r ditemukan %d kali" % (lama[:40], teks.count(lama)))
    return teks.replace(lama, baru, 1)


def pasang(teks):
    if PENANDA in teks:
        return teks, False
    teks = ganti_sekali(teks, "\n.foot { font-size", CSS + ".foot { font-size")
    awal = teks.index('<header class="head">')
    akhir = teks.index("</header>", awal)
    isi = teks[awal + len('<header class="head">'):akhir]
    teks = teks[:awal] + '<header class="head hero">\n    ' + HERO_SVG + '\n    <div class="hero-txt">' + isi + '  </div>\n  </header>' + teks[akhir + len("</header>"):]
    teks = ganti_sekali(teks, '  <footer class="foot">', "  " + OMBAK_SVG + '\n  <footer class="foot">')
    if "\n  // Tab\n" in teks:
        teks = ganti_sekali(teks, "\n  // Tab\n", ICON_JS + "\n  // Tab\n")
    else:  # versi lama tanpa tab
        teks = ganti_sekali(teks, "\n  draw();\n  let t;", ICON_JS + "\n  draw();\n  let t;")
    return teks, True


if __name__ == "__main__":
    src, out = sys.argv[1], sys.argv[2]
    teks, ubah = pasang(open(src, encoding="utf-8").read())
    open(out, "w", encoding="utf-8").write(teks)
    print("OK: ilustrasi dipasang" if ubah else "OK: sudah berilustrasi, tidak diubah")
