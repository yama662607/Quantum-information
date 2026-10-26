export function phaseClock(phase_degrees) {
  const t = phase_degrees * Math.PI / 180;
  const pc = (1 + Math.cos(t))/2, ps = (1 + Math.sin(t))/2;
  const ex = 170 + 110*(1 + Math.cos(t))/2, ey = 140 - 110*Math.sin(t)/2;
  const path = (sine) => Array.from({length:181}, (_,i) => {
    const p = (1 + (sine ? Math.sin(i*Math.PI/90) : Math.cos(i*Math.PI/90)))/2;
    return `${i ? "L" : "M"}${40+i*1.6},${210-150*p}`;
  }).join(" ");
  const node = document.createElement("div");
  node.innerHTML = `<div class="phase-clock-panels" style="display:flex;flex-wrap:wrap;gap:1rem">
    <svg viewBox="0 0 360 290" style="width:100%;max-width:360px;height:auto" role="img" aria-label="基準の振幅と回転する振幅のベクトル和">
      <defs><marker id="phase-arrow" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="context-stroke"/></marker></defs>
      <text x="12" y="22" fill="currentColor">振幅の和（青）の長さ² = ${pc.toFixed(3)}</text>
      <circle cx="170" cy="140" r="110" fill="none" stroke="#94a3b8"/>
      <path d="M50,140 H290 M170,30 V250" stroke="#cbd5e1"/>
      <line x1="170" y1="140" x2="225" y2="140" stroke="#64748b" stroke-width="3" marker-end="url(#phase-arrow)"/>
      <line x1="225" y1="140" x2=${ex} y2=${ey} stroke="#dc2626" stroke-width="3" marker-end="url(#phase-arrow)"/>
      <line x1="170" y1="140" x2=${ex} y2=${ey} stroke="#2563eb" stroke-width="3" marker-end="url(#phase-arrow)"/>
      <text x="12" y="280" fill="currentColor">灰：1/2　赤：exp(iθ)/2　青：和</text>
    </svg>
    <svg viewBox="0 0 360 290" style="width:100%;max-width:360px;height:auto" role="img" aria-label="余弦型と正弦型の測定確率">
      <text x="12" y="22" fill="currentColor">青 cos：${pc.toFixed(3)} / 橙 sin：${ps.toFixed(3)}</text>
      <path d="M40,50 V210 H328" stroke="#94a3b8" fill="none"/>
      <text x="12" y="66" fill="currentColor">1</text><text x="12" y="214" fill="currentColor">0</text>
      <path d="${path(false)}" stroke="#2563eb" fill="none" stroke-width="2.5"/>
      <path d="${path(true)}" stroke="#d97706" fill="none" stroke-width="2.5" stroke-dasharray="6 3"/>
      <line x1=${40+phase_degrees*.8} x2=${40+phase_degrees*.8} y1="50" y2="210" stroke="#64748b"/>
      <circle cx=${40+phase_degrees*.8} cy=${210-150*pc} r="5" fill="#2563eb"/>
      <circle cx=${40+phase_degrees*.8} cy=${210-150*ps} r="5" fill="#d97706"/>
      <text x="35" y="237" fill="currentColor">0°</text><text x="169" y="237" fill="currentColor">180°</text><text x="296" y="237" fill="currentColor">360°</text>
      <text x="12" y="280" fill="currentColor">縦軸：プローブで0を測る確率</text>
    </svg>
  </div>`;
  return node;
}
