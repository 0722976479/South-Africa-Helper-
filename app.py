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
header{background:linear-gradient(90deg,#007749,#FFB81C,#000);padding:15px;text-align:center}
.logo{font-size:22px;font-weight:bold}
.nav{display:flex;gap:8px;overflow-x:auto;padding:10px;background:#1e293b}
.nav button{padding:10px 16px;border:none;border-radius:20px;background:#334155;color:white}
.nav button.active{background:#007749}
.section{display:none;padding:15px}
.section.active{display:block}
.card{background:#1e293b;border-radius:12px;padding:15px;margin:10px 0;border-left:4px solid #007749}
.btn{padding:12px 20px;background:#007749;color:white;border:none;border-radius:8px;width:100%;margin-top:10px;font-weight:bold}
input,textarea,select{width:100%;padding:12px;margin:8px 0;border-radius:8px;border:none;background:#334155;color:white}
h2{color:#FFB81C;margin-bottom:10px}
.badge{background:#007749;padding:2px 8px;border-radius:10px;font-size:12px}
</style>
</head>
<body>
<header><div class="logo">🇿🇦 South Africa Helper</div><small>Jobs • Learnerships • CV • SASSA</small></header>
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
<div class="card"><b>Shoprite Cashier - Limpopo</b><br><span class="badge">No Matric</span><p>Apply in-store</p><button class="btn" onclick="alert('Go to Shoprite with CV!')">How to Apply</button></div>
<div class="card"><b>Boxer Store Assistant</b><br><span class="badge">Grade 10</span><button class="btn" onclick="alert('Visit Boxer!')">Apply Now</button></div>
<div class="card"><b>General Worker</b><br><span class="badge">R5,200</span><button class="btn" onclick="alert('Check Municipality!')">View</button></div>
</div>
<div id="learn" class="section">
<h2>🎓 Learnerships</h2>
<div class="card"><b>SETA Learnership</b><br>R2,500/month<br><button class="btn" onclick="window.open('https://www.sayouth.mobi','_blank')">Apply on SA Youth.mobi</button></div>
</div>
<div id="cv" class="section">
<h2>📄 CV Maker</h2>
<input id="name" placeholder="Full Name">
<input id="phone" placeholder="Phone">
<input id="loc" placeholder="Location">
<select id="edu"><option>Grade 10</option><option>Grade 12 / Matric</option><option>Certificate</option></select>
<textarea id="exp" placeholder="Experience"></textarea>
<button class="btn" onclick="makeCV()">Generate CV</button>
<div id="cvout" class="card" style="display:none;white-space:pre-line;background:white;color:black"></div>
<button id="copyBtn" class="btn" style="display:none;background:#FFB81C;color:black" onclick="copyCV()">Copy CV</button>
</div>
<div id="burs" class="section">
<h2>🎓 NSFAS</h2>
<div class="card"><b>NSFAS Application</b><br><button class="btn" onclick="window.open('https://www.nsfas.org.za','_blank')">Apply on nsfas.org.za</button></div>
</div>
<div id="sassa" class="section">
<h2>💰 SASSA</h2>
<div class="card">SRD R370 Grant<br><button class="btn" onclick="window.open('https://srd.sassa.gov.za/sc19/status','_blank')">Check Status</button></div>
</div>
<div id="house" class="section">
<h2>🏠 RDP Housing</h2>
<div class="card"><b>How to Apply</b><br>Go to municipality with ID.<br><button class="btn" onclick="alert('Visit Makhado Municipality!')">Where to Apply</button></div>
</div>
<div id="ai" class="section">
<h2>🤖 AI Helper</h2>
<textarea id="q" placeholder="Ask: Help me write letter"></textarea>
<button class="btn" onclick="askAI()">Ask AI</button>
<div id="aiout" class="card" style="display:none"></div>
</div>
<script>
function show(id){
document.querySelectorAll('.section').forEach(s=>s.classList.remove('active'));
document.querySelectorAll('.nav button').forEach(b=>b.classList.remove('active'));
document.getElementById(id).classList.add('active');
event.target.classList.add('active')
}
function makeCV(){
let n=document.getElementById('name').value||'Your Name';
let p=document.getElementById('phone').value||'072...';
let l=document.getElementById('loc').value||'Makhado';
let e=document.getElementById('edu').value;
let ex=document.getElementById('exp').value||'Hardworking';
let cv=`CURRICULUM VITAE\n\nName: ${n}\nPhone: ${p}\nLocation: ${l}\nEducation: ${e}\n\nEXPERIENCE:\n${ex}\n\nSKILLS:\n- Hardworking\n- Team work\n\nREFERENCES:\nAvailable on request`;
document.getElementById('cvout').style.display='block';
document.getElementById('cvout').innerText=cv;
document.getElementById('copyBtn').style.display='block';
}
function copyCV(){
navigator.clipboard.writeText(document.getElementById('cvout').innerText);
alert('CV Copied!')
}
function askAI(){
let qq=document.getElementById('q').value;
let ans="Dear Manager, I am applying for cashier. I am hardworking, good with customers, available immediately. Thank you.";
if(qq.toLowerCase().includes('cv')) ans="Use CV Maker tab! Fill name and phone then Generate.";
document.getElementById('aiout').style.display='block';
document.getElementById('aiout').innerText=ans;
}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML

if __name__ == '__main__':
    app.run()
