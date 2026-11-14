import json
import os
import shutil

dist_dir = "./dist"
if os.path.exists(dist_dir):
    shutil.rmtree(dist_dir)
os.makedirs(dist_dir, exist_ok=True)
os.makedirs(f"{dist_dir}/role", exist_ok=True)
os.makedirs(f"{dist_dir}/country", exist_ok=True)
os.makedirs(f"{dist_dir}/compare", exist_ok=True)

with open("./data/matrix.json") as f:
    matrix = json.load(f)

with open("./data/roles.json") as f:
    roles = json.load(f)

with open("./data/countries.json") as f:
    countries = json.load(f)

# Product audit: no evidence supports the historic country risk grades.
for row in countries + matrix:
    row['eor_risk'] = 'Not assessed'

# Common Header & Footer
def render_header(title, desc, canonical):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:creator" content="@alexyuan01">
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body {{ background-color: #0b0f17; color: #e2e8f0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
    .glass-card {{ background: rgba(18, 24, 38, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.08); }}
    .brand-gradient {{ background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
  </style>
</head>
<body class="min-h-screen flex flex-col justify-between selection:bg-indigo-500 selection:text-white">
  <header class="border-b border-slate-800 bg-slate-900/60 sticky top-0 z-50 backdrop-blur-md">
    <div class="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
      <a href="/" class="flex items-center gap-2 text-xl font-bold tracking-tight">
        <span class="p-1.5 rounded-lg bg-indigo-600/20 text-indigo-400 border border-indigo-500/30">🌐</span>
        <span class="text-white">Remote<span class="text-indigo-400">Salary</span> Matrix</span>
      </a>
      <nav class="flex items-center gap-6 text-sm font-medium text-slate-300">
        <a href="/#calculator" class="hover:text-white transition">Calculator</a>
        <a href="/#roles" class="hover:text-white transition">Tech Roles</a>
        <a href="/#countries" class="hover:text-white transition">Talent Hubs</a>
        <a href="/#hiring-kit-status" target="_blank" class="px-3.5 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-medium transition shadow-sm">Kit sales paused</a>
      </nav>
    </div>
  </header>
  <main class="flex-grow">
    <section id="hiring-kit-status" class="max-w-6xl mx-auto px-4 py-5 border-b border-slate-800">
      <strong>Hiring kit sales paused — November 14, 2026.</strong>
      The package advertised 25 jurisdictions but contained notes for six countries, and its contract examples have not received local legal review. We have stopped new sales. Existing purchasers can use their Gumroad receipt for downloads or support. Do not treat the examples as validated legal agreements. Reopening requires corrected scope, sources, professional review and user task testing.
    </section>
    <div class="max-w-6xl mx-auto px-4 py-4 text-sm text-slate-300 border-b border-slate-800">
      <strong>How estimates work:</strong> annual pay = a manually selected US role baseline × a fixed country multiplier. Monthly pay = annual pay ÷ 12; hourly pay = annual pay ÷ 2,080. These are illustrative USD budgets, not survey results or current job offers. Tax and contractor notes are simplified references, not legal determinations.
    </div>
"""

def render_footer():
    return """
  </main>
  <footer class="border-t border-slate-800/80 bg-slate-950 py-12 mt-20 text-slate-400 text-sm">
    <div class="max-w-6xl mx-auto px-4 grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
      <div>
        <div class="flex items-center gap-2 text-base font-bold text-white mb-3">
          <span>🌐</span> RemoteSalary Matrix
        </div>
        <p class="text-xs leading-relaxed text-slate-500">
          Illustrative global hiring budgets using fixed country multipliers. These estimates are not surveyed salaries or legal advice.
        </p>
      </div>
      <div>
        <h4 class="text-white text-xs font-semibold uppercase tracking-wider mb-3">Top Engineering Roles</h4>
        <ul class="space-y-2 text-xs">
          <li><a href="/role/senior-frontend-engineer.html" class="hover:text-slate-200">Senior Frontend Engineer</a></li>
          <li><a href="/role/senior-backend-engineer.html" class="hover:text-slate-200">Senior Backend Engineer</a></li>
          <li><a href="/role/ai-machine-learning-engineer.html" class="hover:text-slate-200">AI / Machine Learning Engineer</a></li>
          <li><a href="/role/devops-cloud-architect.html" class="hover:text-slate-200">DevOps & Cloud Architect</a></li>
        </ul>
      </div>
      <div>
        <h4 class="text-white text-xs font-semibold uppercase tracking-wider mb-3">Prime Talent Hubs</h4>
        <ul class="space-y-2 text-xs">
          <li><a href="/country/PL.html" class="hover:text-slate-200">Poland Tech Salaries & B2B</a></li>
          <li><a href="/country/RO.html" class="hover:text-slate-200">Romania Micro-Enterprise Guide</a></li>
          <li><a href="/country/BR.html" class="hover:text-slate-200">Brazil CLT vs PJ Compliance</a></li>
          <li><a href="/country/IN.html" class="hover:text-slate-200">India Independent Consultancy</a></li>
        </ul>
      </div>
      <div>
        <h4 class="text-white text-xs font-semibold uppercase tracking-wider mb-3">Sister Matrix Tools</h4>
        <ul class="space-y-2 text-xs">
          <li><a href="https://nomad.apexcraftweb.com" target="_blank" class="hover:text-indigo-400">NomadMatrix — Digital Nomad Visas</a></li>
          <li><a href="https://stackcost.apexcraftweb.com" target="_blank" class="hover:text-indigo-400">StackCost Matrix — Cloud Hidden Traps</a></li>
          <li><a href="https://x.com/alexyuan01" target="_blank" class="hover:text-sky-400">Follow on X (@alexyuan01)</a></li>
        </ul>
      </div>
    </div>
    <div class="max-w-6xl mx-auto px-4 pt-6 border-t border-slate-900 text-center text-xs text-slate-600">
      &copy; 2026 RemoteSalary Matrix. Illustrative estimates, not audited market data. Confirm local compensation and regulations independently.
    </div>
  </footer>
</body>
</html>
"""

# 1. Render Homepage with Interactive Global Hiring Calculator
home_html = render_header(
    "RemoteSalary Matrix — Global Tech Salary Benchmarks & Contractor Compliance 2026",
    "Compare remote developer salaries, contractor taxes, and EOR legal compliance across 25 countries. Save 50-80% on US tech talent legally.",
    "https://salary.apexcraftweb.com/"
) + f"""
<section class="max-w-6xl mx-auto px-4 pt-16 pb-12 text-center">
  <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-950/80 border border-indigo-800/60 text-indigo-300 text-xs font-medium mb-6">
    <span>✨</span> Illustrative Hiring Budget Model
  </div>
  <h1 class="text-4xl md:text-6xl font-extrabold tracking-tight text-white mb-6 leading-tight">
    Hire Top Global Engineers.<br>
    <span class="brand-gradient">Explore Estimated Hiring Budgets.</span>
  </h1>
  <p class="max-w-2xl mx-auto text-slate-400 text-base md:text-lg mb-10 leading-relaxed">
    Compare illustrative hiring budgets using a selected US baseline and fixed country multipliers. These estimates are not observed market salaries. Country legal and tax notes require independent verification.
  </p>

  <!-- Interactive Hiring Calculator -->
  <div id="calculator" class="max-w-3xl mx-auto glass-card rounded-2xl p-6 md:p-8 text-left shadow-2xl border border-slate-700/60 mb-16">
    <div class="flex items-center justify-between border-b border-slate-800 pb-4 mb-6">
      <h3 class="text-lg font-bold text-white flex items-center gap-2">
        <span>⚡</span> Interactive Remote Salary & Savings Calculator
      </h3>
      <span class="text-xs text-slate-400">Fixed assumptions · no live data feed</span>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
      <div>
        <label class="block text-xs font-semibold text-slate-400 mb-2 uppercase tracking-wider">Select Tech Role</label>
        <select id="roleSelect" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3.5 py-2.5 text-sm text-white focus:outline-none focus:border-indigo-500">
          {"".join([f'<option value="{r["slug"]}" data-base="{r["us_base"]}">{r["title"]} (US Base: ${r["us_base"]:,}/yr)</option>' for r in roles])}
        </select>
      </div>
      <div>
        <label class="block text-xs font-semibold text-slate-400 mb-2 uppercase tracking-wider">Select Destination Country</label>
        <select id="countrySelect" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3.5 py-2.5 text-sm text-white focus:outline-none focus:border-indigo-500">
          {"".join([f'<option value="{c["code"]}" data-ratio="{c["ratio"]}" data-risk="{c["eor_risk"]}" data-eor="{c["best_eor"]}">{c["country"]} (Assumed Ratio: {int(c["ratio"]*100)}%)</option>' for c in countries])}
        </select>
      </div>
    </div>

    <!-- Output Box -->
    <div class="bg-slate-950/80 rounded-xl p-5 border border-slate-800 grid grid-cols-2 md:grid-cols-4 gap-4 text-center mb-6">
      <div>
        <div class="text-xs text-slate-500 uppercase tracking-wider mb-1">Estimated Pay Budget</div>
        <div id="outLocal" class="text-xl md:text-2xl font-bold text-indigo-400">$74,400</div>
        <div class="text-xs text-slate-500">per year</div>
      </div>
      <div>
        <div class="text-xs text-slate-500 uppercase tracking-wider mb-1">Hourly Rate</div>
        <div id="outHourly" class="text-xl md:text-2xl font-bold text-sky-400">$35.77</div>
        <div class="text-xs text-slate-500">USD / hr</div>
      </div>
      <div>
        <div class="text-xs text-slate-500 uppercase tracking-wider mb-1">Illustrative Annual Difference</div>
        <div id="outSavings" class="text-xl md:text-2xl font-bold text-emerald-400">$80,600</div>
        <div id="outPct" class="text-xs text-emerald-500">52% below selected US baseline</div>
      </div>
      <div>
        <div class="text-xs text-slate-500 uppercase tracking-wider mb-1">Legal Review</div>
        <div id="outRisk" class="text-sm font-semibold text-slate-300 mt-1">Not assessed</div>
        <div id="outEor" class="text-[10px] text-slate-500 mt-0.5">Deel / Remote.com</div>
      </div>
    </div>

    <div class="flex items-center justify-between">
      <span class="text-xs text-slate-400">Review the assumptions and seek local professional advice.</span>
      <a id="compareLink" href="/compare/senior-frontend-engineer-in-PL.html" class="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold rounded-lg transition">
        View reference notes &rarr;
      </a>
    </div>
  </div>
</section>

<!-- Matrix Directory Section -->
<section id="roles" class="max-w-6xl mx-auto px-4 py-12">
  <div class="flex items-center justify-between mb-8">
    <div>
      <h2 class="text-2xl font-bold text-white">Browse By Engineering Role</h2>
      <p class="text-slate-400 text-sm">US Baseline vs Global Pay Benchmarks across 12 disciplines</p>
    </div>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
    {"".join([f'''
    <a href="/role/{r["slug"]}.html" class="glass-card rounded-xl p-5 hover:border-indigo-500/50 transition group">
      <div class="flex items-center justify-between mb-3">
        <h4 class="text-white font-semibold group-hover:text-indigo-400 transition text-base">{r["title"]}</h4>
        <span class="text-xs px-2 py-0.5 rounded bg-slate-800 text-slate-400 font-mono">${r["us_base"]:,}/yr</span>
      </div>
      <div class="flex flex-wrap gap-1.5 mb-3">
        {"".join([f'<span class="text-[11px] bg-slate-900 border border-slate-800 text-slate-400 px-2 py-0.5 rounded">{sk}</span>' for sk in r["skills"]])}
      </div>
      <div class="text-xs text-indigo-400 flex items-center gap-1 group-hover:translate-x-1 transition duration-200">
        Compare 25 Countries &rarr;
      </div>
    </a>
    ''' for r in roles])}
  </div>
</section>

<section id="countries" class="max-w-6xl mx-auto px-4 py-12">
  <div class="flex items-center justify-between mb-8">
    <div>
      <h2 class="text-2xl font-bold text-white">Top 25 Global Talent Markets</h2>
      <p class="text-slate-400 text-sm">Illustrative cost multipliers and unverified country reference notes</p>
    </div>
  </div>
  <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
    {"".join([f'''
    <a href="/country/{c["code"]}.html" class="glass-card rounded-xl p-4 hover:border-indigo-500/50 transition">
      <div class="flex items-center justify-between mb-2">
        <span class="text-white font-medium text-sm">{c["country"]}</span>
        <span class="text-xs font-mono px-1.5 py-0.5 rounded {"bg-emerald-950 text-emerald-400 border border-emerald-800/40" if "Low" in c["eor_risk"] else "bg-amber-950 text-amber-400 border border-amber-800/40" if "Medium" in c["eor_risk"] else "bg-rose-950 text-rose-400 border border-rose-800/40"}">{c["eor_risk"].split()[0]}</span>
      </div>
      <div class="text-xs text-slate-400 space-y-1">
        <div>Cost vs US: <span class="text-slate-200 font-semibold">{int(c["ratio"]*100)}%</span></div>
        <div>Contract: <span class="text-slate-300 truncate block">{c["contract_mode"].split("or")[0]}</span></div>
      </div>
    </a>
    ''' for c in countries])}
  </div>
</section>

<script>
  const roles = {json.dumps(roles)};
  const countries = {json.dumps(countries)};

  const roleEl = document.getElementById('roleSelect');
  const countryEl = document.getElementById('countrySelect');
  const outLocal = document.getElementById('outLocal');
  const outHourly = document.getElementById('outHourly');
  const outSavings = document.getElementById('outSavings');
  const outPct = document.getElementById('outPct');
  const outRisk = document.getElementById('outRisk');
  const outEor = document.getElementById('outEor');
  const compareLink = document.getElementById('compareLink');

  function updateCalc() {{
    const rSlug = roleEl.value;
    const cCode = countryEl.value;
    const r = roles.find(x => x.slug === rSlug);
    const c = countries.find(x => x.code === cCode);

    const localAnnual = Math.round(r.us_base * c.ratio);
    const hourly = (localAnnual / 2080).toFixed(2);
    const savings = r.us_base - localAnnual;
    const pct = Math.round((savings / r.us_base) * 100);

    outLocal.innerText = '$' + localAnnual.toLocaleString();
    outHourly.innerText = '$' + hourly;
    outSavings.innerText = '$' + savings.toLocaleString();
    outPct.innerText = pct + '% below selected US baseline';
    outRisk.innerText = 'Not assessed';
    outEor.innerText = c.best_eor;
    compareLink.href = '/compare/' + rSlug + '-in-' + cCode + '.html';
  }}

  roleEl.addEventListener('change', updateCalc);
  countryEl.addEventListener('change', updateCalc);
  updateCalc();
</script>
""" + render_footer()

with open(f"{dist_dir}/index.html", "w") as f:
    f.write(home_html)

# 2. Render 12 Role Pages
for r in roles:
    role_benchmarks = [m for m in matrix if m["role_slug"] == r["slug"]]
    role_html = render_header(
        f"{r['title']} Salary Benchmarks Across 25 Countries (2026)",
        f"Detailed salary comparison for {r['title']} across Poland, Romania, Brazil, India, and more. US baseline: ${r['us_base']:,}/yr.",
        f"https://salary.apexcraftweb.com/role/{r['slug']}.html"
    ) + f"""
    <div class="max-w-6xl mx-auto px-4 py-12">
      <div class="mb-8">
        <a href="/" class="text-xs text-indigo-400 hover:underline mb-2 inline-block">&larr; Back to Matrix Home</a>
        <h1 class="text-3xl md:text-5xl font-extrabold text-white mb-3">{r['title']} Global Salary Benchmarks</h1>
        <p class="text-slate-400 text-base max-w-3xl leading-relaxed">
          The median US market base for a {r['title']} is <strong>${r['us_base']:,}/year</strong>. Compare what top engineering candidates earn across international offshore hubs, along with local B2B contractor rates and annual savings.
        </p>
      </div>

      <div class="glass-card rounded-2xl p-6 border border-slate-800 overflow-x-auto mb-12">
        <table class="w-full text-left text-sm text-slate-300">
          <thead class="text-xs uppercase bg-slate-900/80 text-slate-400 border-b border-slate-800">
            <tr>
              <th class="py-3 px-4">Country</th>
              <th class="py-3 px-4">Local Annual (USD)</th>
              <th class="py-3 px-4">Hourly Rate</th>
              <th class="py-3 px-4">Illustrative Annual Difference</th>
              <th class="py-3 px-4">EOR / Misclass Risk</th>
              <th class="py-3 px-4">Action</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-800/60 font-mono text-xs">
            {"".join([f'''
            <tr class="hover:bg-slate-800/40 transition">
              <td class="py-3 px-4 font-sans font-medium text-white flex items-center gap-2">
                <span>{b["country_name"]}</span>
              </td>
              <td class="py-3 px-4 text-indigo-300 font-bold">${b["local_annual_usd"]:,}</td>
              <td class="py-3 px-4 text-sky-300">${b["hourly_usd"]}/hr</td>
              <td class="py-3 px-4 text-emerald-400 font-semibold">${b["annual_savings_usd"]:,} ({b["savings_pct"]}%)</td>
              <td class="py-3 px-4 font-sans text-slate-400">{b["eor_risk"]}</td>
              <td class="py-3 px-4 font-sans">
                <a href="/compare/{b['role_slug']}-in-{b['country_code']}.html" class="text-indigo-400 hover:text-indigo-300 font-medium">Breakdown &rarr;</a>
              </td>
            </tr>
            ''' for b in role_benchmarks])}
          </tbody>
        </table>
      </div>
    </div>
    """ + render_footer()

    with open(f"{dist_dir}/role/{r['slug']}.html", "w") as f:
        f.write(role_html)

# 3. Render 25 Country Pages
for c in countries:
    country_benchmarks = [m for m in matrix if m["country_code"] == c["code"]]
    c_html = render_header(
        f"Hiring Tech Talent in {c['country']} (2026): Salary, Taxes & EOR Compliance",
        f"Comprehensive hiring guide for {c['country']}. Average developer salary rates, B2B flat tax regulations, labor law risks, and EOR solutions.",
        f"https://salary.apexcraftweb.com/country/{c['code']}.html"
    ) + f"""
    <div class="max-w-6xl mx-auto px-4 py-12">
      <div class="mb-8">
        <a href="/" class="text-xs text-indigo-400 hover:underline mb-2 inline-block">&larr; Back to Matrix Home</a>
        <h1 class="text-3xl md:text-5xl font-extrabold text-white mb-3">Hiring Remote Tech Talent in {c['country']}</h1>
        <p class="text-slate-400 text-base max-w-3xl leading-relaxed">
          Engineers in {c['country']} trade at approximately <strong>{int(c['ratio']*100)}% of US market rates</strong>. Below is the full salary breakdown across 12 software disciplines, along with labor classification rules and IP transfer requirements.
        </p>
      </div>

      <!-- Legal Summary Card -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
        <div class="glass-card rounded-xl p-5 border border-slate-800">
          <div class="text-xs uppercase text-slate-500 font-semibold mb-1">Contractor Model</div>
          <div class="text-white font-medium text-sm mb-2">{c['contract_mode']}</div>
          <div class="text-xs text-slate-400">Effective tax rate: approx {c['tax_pct']}%</div>
        </div>
        <div class="glass-card rounded-xl p-5 border border-slate-800">
          <div class="text-xs uppercase text-slate-500 font-semibold mb-1">Misclassification Risk</div>
          <div class="text-white font-medium text-sm mb-2">{c['eor_risk']}</div>
          <div class="text-xs text-slate-400">Recommended EOR: {c['best_eor']}</div>
        </div>
        <div class="glass-card rounded-xl p-5 border border-slate-800">
          <div class="text-xs uppercase text-slate-500 font-semibold mb-1">IP Assignment</div>
          <div class="text-white font-medium text-sm mb-2">{c['ip_protection']}</div>
          <div class="text-xs text-slate-400">Requires written bilateral transfer agreement</div>
        </div>
      </div>

      <div class="glass-card rounded-2xl p-6 border border-slate-800 overflow-x-auto">
        <h3 class="text-lg font-bold text-white mb-4">Tech Salary Table in {c['country']}</h3>
        <table class="w-full text-left text-sm text-slate-300">
          <thead class="text-xs uppercase bg-slate-900/80 text-slate-400 border-b border-slate-800">
            <tr>
              <th class="py-3 px-4">Role</th>
              <th class="py-3 px-4">Local Annual</th>
              <th class="py-3 px-4">Hourly</th>
              <th class="py-3 px-4">Illustrative Annual Difference vs US</th>
              <th class="py-3 px-4">Details</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-800/60 font-mono text-xs">
            {"".join([f'''
            <tr class="hover:bg-slate-800/40 transition">
              <td class="py-3 px-4 font-sans font-medium text-white">{b["role_title"]}</td>
              <td class="py-3 px-4 text-indigo-300 font-bold">${b["local_annual_usd"]:,}</td>
              <td class="py-3 px-4 text-sky-300">${b["hourly_usd"]}/hr</td>
              <td class="py-3 px-4 text-emerald-400 font-semibold">${b["annual_savings_usd"]:,} ({b["savings_pct"]}%)</td>
              <td class="py-3 px-4 font-sans">
                <a href="/compare/{b['role_slug']}-in-{b['country_code']}.html" class="text-indigo-400 hover:text-indigo-300">View Legal Specs &rarr;</a>
              </td>
            </tr>
            ''' for b in country_benchmarks])}
          </tbody>
        </table>
      </div>
    </div>
    """ + render_footer()

    with open(f"{dist_dir}/country/{c['code']}.html", "w") as f:
        f.write(c_html)

# 4. Render 300 Deep Comparison Pages
for b in matrix:
    comp_html = render_header(
        f"{b['role_title']} in {b['country_name']}: 2026 Salary & Hiring Guide",
        f"Detailed {b['role_title']} salary in {b['country_name']}. Local pay: ${b['local_annual_usd']:,}/yr (${b['hourly_usd']}/hr). Save ${b['annual_savings_usd']:,} vs US market.",
        f"https://salary.apexcraftweb.com/compare/{b['role_slug']}-in-{b['country_code']}.html"
    ) + f"""
    <div class="max-w-4xl mx-auto px-4 py-12">
      <div class="mb-6">
        <a href="/role/{b['role_slug']}.html" class="text-xs text-indigo-400 hover:underline">&larr; Back to {b['role_title']} Benchmarks</a>
      </div>

      <div class="glass-card rounded-2xl p-6 md:p-8 border border-slate-700/80 mb-8 shadow-2xl">
        <div class="flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-950 border border-indigo-800/50 text-indigo-300 text-xs w-max mb-4">
          <span>🎯</span> Formula-Based Budget Estimate
        </div>
        <h1 class="text-3xl md:text-4xl font-extrabold text-white mb-4">
          Hiring a {b['role_title']} in {b['country_name']}
        </h1>
        <p class="text-slate-400 text-base leading-relaxed mb-6">
          A US company hiring a <strong>{b['role_title']}</strong> in <strong>{b['country_name']}</strong> can expect an average annual base of <strong>${b['local_annual_usd']:,} USD</strong>, saving approximately <strong>${b['annual_savings_usd']:,} USD ({b['savings_pct']}%)</strong> per year compared to equivalent US talent.
        </p>

        <!-- Metric Grid -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 bg-slate-950/70 p-4 rounded-xl border border-slate-800 mb-8">
          <div>
            <div class="text-xs text-slate-500 uppercase">Local Base</div>
            <div class="text-xl font-bold text-indigo-400">${b['local_annual_usd']:,}</div>
            <div class="text-[11px] text-slate-500">per annum</div>
          </div>
          <div>
            <div class="text-xs text-slate-500 uppercase">Hourly Rate</div>
            <div class="text-xl font-bold text-sky-400">${b['hourly_usd']}</div>
            <div class="text-[11px] text-slate-500">USD / hour</div>
          </div>
          <div>
            <div class="text-xs text-slate-500 uppercase">US Benchmark</div>
            <div class="text-xl font-bold text-slate-400">${b['us_base_annual']:,}</div>
            <div class="text-[11px] text-slate-500">SF / NYC avg</div>
          </div>
          <div>
            <div class="text-xs text-slate-500 uppercase">Net Savings</div>
            <div class="text-xl font-bold text-emerald-400">${b['annual_savings_usd']:,}</div>
            <div class="text-[11px] text-emerald-500">{b['savings_pct']}% budget saved</div>
          </div>
        </div>

        <!-- Compliance & Legal Architecture -->
        <h3 class="text-lg font-bold text-white mb-4">Legal & Compliance Breakdown</h3>
        <div class="space-y-4 text-sm text-slate-300 mb-8">
          <div class="p-4 rounded-lg bg-slate-900/60 border border-slate-800">
            <span class="text-indigo-400 font-semibold block mb-1">Contractor Hiring vs Misclassification:</span>
            <span>{b['contract_mode']}. Classification risk has not been independently assessed. Historical note: <strong class="text-white">{b['eor_risk']}</strong>.</span>
          </div>
          <div class="p-4 rounded-lg bg-slate-900/60 border border-slate-800">
            <span class="text-indigo-400 font-semibold block mb-1">Intellectual Property (IP) Protection:</span>
            <span>{b['ip_protection']}. US companies must ensure a clear, written IP assignment clause is executed in accordance with local labor and civil code.</span>
          </div>
          <div class="p-4 rounded-lg bg-slate-900/60 border border-slate-800">
            <span class="text-indigo-400 font-semibold block mb-1">Recommended Employer of Record (EOR):</span>
            <span>An EOR does not remove every employment risk. Research provider options with local advice. Historical provider reference: <strong class="text-white">{b['best_eor']}</strong>.</span>
          </div>
        </div>

        <!-- Conversion / Monetization CTA -->
        <div class="p-5 rounded-xl bg-gradient-to-r from-indigo-950 to-slate-900 border border-indigo-700/60 flex flex-col md:flex-row items-center justify-between gap-4">
          <div>
            <div class="text-white font-bold text-sm mb-1">Hiring kit sales paused</div>
            <div class="text-xs text-slate-400">The package did not deliver its advertised jurisdiction coverage and has not received jurisdiction-specific legal review. New sales have stopped.</div>
          </div>
          <a href="/#hiring-kit-status" target="_blank" class="px-5 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold rounded-lg shadow-md transition whitespace-nowrap">
            Kit sales paused — details &rarr;
          </a>
        </div>
      </div>
    </div>
    """ + render_footer()

    with open(f"{dist_dir}/compare/{b['role_slug']}-in-{b['country_code']}.html", "w") as f:
        f.write(comp_html)

# 5. Generate XML Sitemap
total_pages = 1 + len(roles) + len(countries) + len(matrix)
sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
sitemap_xml.append('  <url><loc>https://salary.apexcraftweb.com/</loc><changefreq>weekly</changefreq><priority>1.0</priority></url>')
for r in roles:
    sitemap_xml.append(f'  <url><loc>https://salary.apexcraftweb.com/role/{r["slug"]}.html</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>')
for c in countries:
    sitemap_xml.append(f'  <url><loc>https://salary.apexcraftweb.com/country/{c["code"]}.html</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>')
for b in matrix:
    sitemap_xml.append(f'  <url><loc>https://salary.apexcraftweb.com/compare/{b["role_slug"]}-in-{b["country_code"]}.html</loc><changefreq>monthly</changefreq><priority>0.6</priority></url>')
sitemap_xml.append('</urlset>')

with open(f"{dist_dir}/sitemap.xml", "w") as f:
    f.write("\n".join(sitemap_xml))

# 6. Generate robots.txt
robots_txt = """User-agent: *
Allow: /
Sitemap: https://salary.apexcraftweb.com/sitemap.xml
"""
with open(f"{dist_dir}/robots.txt", "w") as f:
    f.write(robots_txt)

print(f"Successfully generated full site at {dist_dir} with {total_pages} pages!")
