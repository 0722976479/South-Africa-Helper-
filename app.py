from flask import Flask
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>South Africa Helper 🇿🇦</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:Arial;background:#0f172a;color:white}
header{background:linear-gradient(90deg,#007749,#FFB81C,#000);padding:15px;text-align:center;position:sticky;top:0;z-index:100}
.logo{font-size:22px;font-weight:bold}
.nav{display:flex;gap:8px;overflow-x:auto;padding:10px;background:#1e293b}
.nav button{padding:10px 16px;border:none;border-radius:20px;background:#334155;color:white;white-space:nowrap}
.nav button.active{background:#007749}
.section{display:none;padding:15px}
.section.active{display:block}
.card{background:#1e293b;border-radius:12px;padding:15px;margin:10px 0;border-left:4px solid #007749}
.btn{padding:12px 20px;background:#007749;color:white;border:none;border-radius:8px;width:100%;margin-top:10px;font-weight:bold}
input,textarea,select{width:100%;padding:12px;margin:8px 0;border-radius:8px;border:none;background:#334155;color:white}
h2{color:#FFB81C;margin-bottom:10px}
.job-title{font-weight:bold;color:#4ade80}
.badge{background:#007749;padding:2px 8px;border-radius:10px;font-size:12px}
</style>
</head>
<body>
<header><div class="logo">🇿🇦 South Africa Helper - ALL-IN-ONE</div><small>Jobs • Learnerships • CV • Bursaries • SASSA • Housing</small></header>
<div class="nav">
<button class="active" onclick="show('jobs')">💼 Jobs</button>
<button onclick="show('learn')">🎓 Learnerships</button>
<button onclick="show('cv')">📄 CV Maker</button>
<button onclick="show('burs')">🎓 Bursaries</button>
<button onclick="show('sassa')">💰 SASSA</button>
<button onclick="show('house')">🏠 RDP Housing</button>
<button onclick="show('ai')">🤖 AI Helper</button>
</div>

<div id="jobs" class="section active">
<h2>🔥 Latest Jobs in South Africa</h2>
<div class="card"><div class="job-title">Shoprite Cashier - Limpopo</div><small>VodaCom • Makhado</small><br><span class="badge">No Matric</span> <span class="badge">R4,500</span><p>Apply in-store with ID and CV.</p><button class="btn" onclick="alert('Go to nearest Shoprite with CV and ID!')">How to Apply</button></div>
<div class="card"><div class="job-title">Boxer Store Assistant</div><small>Thohoyandou / Giyani</small><br><span class="badge">Grade 10 Accepted</span><p>Bring CV to store manager Mon-Fri 8am.</p><button class="btn" onclick="alert('Visit Boxer with certified ID copy!')">Apply Now</button></div>
<div class="card"><div class="job-title">General Worker - Municipality</div><small>All Limpopo Municipalities</small><br><span class="badge">R5,200</span><p>EPWP jobs - Check municipality board.</p><button class="btn" onclick="alert('Check Makhado Municipality notice board!')">View Details</button></div>
<div class="card"><div class="job-title">Domestic Worker / Gardener</div><small>Polokwane, Louis Trichardt</small><br><span class="badge">Immediate</span><p>Families hiring - WhatsApp your CV.</p><button class="btn" onclick="alert('Create CV below and share on Facebook Jobs!')">Create CV First</button></div>
</div>

<div id="learn" class="section">
<h2>🎓 Learnerships 2026</h2>
<div class="card"><b>SETA Learnership - Retail</b><br>Stipend: R2,500/month • 12 months • Grade 10-12<br><button class="btn" onclick="window.open('https://www.sayouth.m
