Here is the NEW full code — COPY ALL:

Tap HOLD on the code below → Select All → Copy → Go to GitHub and Paste!

---
from flask import Flask
app = Flask(*name*)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>South Africa Helper 🇿🇦</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:Arial;background:#0f172a;color:white}
header{background:linear-gradient(90deg,#007749,#FFB81C,#000);padding:15px;text-align:center;position:sticky;top:0}
.logo{font-size:22px;font-weight:bold}
.nav{display:flex;gap:8px;overflow-x:auto;padding:10px;background:#1e293b}
.nav button{padding:10px 16px;border:none;border-radius:20px;background:#334155;color:white;white-space:nowrap}
.nav http://button.active{background:#007749}
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
<h2>🔥 Latest Jobs</h2>
<div class="card"><div class="job-title">Shoprite Cashier - Limpopo</div><small>Makhado</small><br><span class="badge">No Matric</span><p>Apply in-store with ID and CV.</p><button class="btn" onclick="alert('Go to nearest Shoprite with CV and ID!')">How to Apply</button></div>
<div class="card"><div class="job-title">Boxer Store Assistant</div><small>Thohoyandou / Giyani</small><br><span class="badge">Grade 10 Accepted</span><p>Bring CV to manager.</p><button class="btn" onclick="alert('Visit Boxer with certified ID copy!')">Apply Now</button></div>
<div class="card"><div class="job-title">General Worker - Municipality</div><small>All Limpopo</small><br><span class="badge">R5,200</span><p>EPWP jobs.</p><button class="btn" onclick="alert('Check Makhado Municipality board!')">View</button></div>
</div>

<div id="learn" class="section">
<h2>🎓 Learnerships 2026</h2>
<div class="card"><b>SETA Learnership - Retail</b><br>Stipend: R2,500/month<br><button class="btn" onclick="window.open('https://www.sayouth.mobi','_blank')">Apply on SA http://Youth.mobi</button></div>
<div class="card"><b>Transnet Learnership</b><br>Stipend: R4,500<br><button class="btn" onclick="window.open('https://www.sayouth.mobi','_blank')">Apply Now</button></div>
</div>

<div id="cv" class="section">
<h2>📄 CV Maker</h2>
<input id="name" placeholder="Full Name">
<input id="phone" placeholder="Phone e.g. 072 297 6479">
<input id="loc" placeholder="Location e.g. Makhado">
<select id="edu"><option>Grade 10</option><option>Grade 11</option><option>Grade 12 / Matric</option><option>Certificate</option><option>Diploma</option></select>
<textarea id="exp" placeholder="Experience"></textarea>
<button class="btn" onclick="makeCV()">Generate CV</button>
<div id="cvout" class="card" style="display:none;white-space:pre-line;background:white;color:black"></div>
<button id="copyBtn" class="btn" style="display:none;background:#FFB81C;color:black" onclick="copyCV()">Copy CV</button>
</div>

<div id="burs" class="section">
<h2>🎓 NSFAS</h2>
<div class="card"><b>NSFAS Application</b><br>For University & TVET<br><button class="btn" onclick="window.open('https://www.nsfas.org.za','_blank')">Apply on http://nsfas.org.za</button></div>
</div>

<div id="sassa" class="section">
<h2>💰 SASSA</h2>
<div class="card">SRD R370 Grant<br><button class="btn" onclick="window.open('https://srd.sassa.gov.za/sc19/status','_blank')">Open SASSA Status Page</button></div>
</div>

<div id="house" class="section">
<h2>🏠 RDP Housing</h2>
<div class="card"><b>How to Apply</b><br>Go to municipality with ID.<br><button class="btn" onclick="alert('Visit Makhado Municipality Housing Dept!')">Where to Apply</button></div>
</div>

<div id="ai" class="section">
<h2>🤖 AI Helper</h2>
<textarea id="q" placeholder="Ask: Help me write letter for cashier job"></textarea>
<button class="btn" onclick="askAI()">Ask AI</button>
<div id="aiout" class="card" style="display:none"></div>
</div>

<script>
function show(id){document.querySelectorAll('.section').forEach(s=>s.classList.remove('active'));document.querySelectorAll('.nav button').forEach(b=>b.classList.remove('active'));document.getElementById(id).classList.add('active');event.target.classList.add('active')}
function makeCV(){
let n=document.getElementById('name').value||'Your Name';
let p=document.getElementById('phone').value||'072...';
let l=document.getElementById('loc').value||'Makhado';
let e=document.getElementById('edu').value;
let ex=document.getElementById('exp').value||'Hardworking';
let cv=`CURRICULUM VITAE\n\nName: ${n}\nPhone: ${p}\nLocation: ${l}\nEducation: ${e}\n\nEXPERIENCE:\n${ex}\n\nSKILLS:\n- Hardworking\n- Team work\n\nREFERENCES:\nAvailable on request`;
http://document.getElementById('cvout').style.display='block';document.getElementById('cvout').innerText=cv;
http://document.getElementById('copyBtn').style.display='block';
}
function copyCV(){navigator.clipboard.writeText(document.getElementById('cvout').innerText);alert('CV Copied!')}
function askAI(){
let qq=document.getElementById('q').value;
let ans="Dear Manager, I am applying for cashier. I am hardworking, good with customers, available immediately. Thank you.";
if(qq.toLowerCase().includes('cv')) ans="Use CV Maker tab! Fill name and phone then Generate.";
http://document.getElementById('aiout').style.display='block';document.getElementById('aiout').innerText=ans;
}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML

if *name* == '*main*':
    http://app.run()
---
After pasting → Scroll down → Tap green *Commit changes...* → Tap *Commit changes*

Then tell me!
