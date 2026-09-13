from flask import Flask
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>South Africa Helper - Jobs, SASSA, RDP</title>
<style>
body{margin:0;font-family:Arial;background:#0f0f0f;color:white}
header{background:linear-gradient(90deg,#007A4D,#FFB612);padding:20px;text-align:center}
nav{display:flex;gap:8px;overflow:auto;padding:12px;background:#1a1a1a;position:sticky;top:0}
nav button{white-space:nowrap;padding:10px 14px;border-radius:20px;border:none;background:#2a2a2a;color:white}
nav button.active{background:#007A4D}
.card{background:#1e1e1e;padding:16px;border-radius:12px;margin:12px}
.btn{background:#007A4D;color:white;padding:12px 20px;border:none;border-radius:8px;width:100%;font-weight:bold}
input,textarea,select{width:100%;padding:12px;margin:6px 0;border-radius:8px;border:1px solid #333;background:#2a2a2a;color:white;box-sizing:border-box}
.section{display:none;padding:10px} .section.active{display:block}
a{color:#FFB612}
</style>
</head>
<body>
<header><h2>🇿🇦 South Africa Helper</h2><p>Jobs • Learnerships • CV Maker • SASSA • RDP • Bursaries</p></header>
<nav>
<button onclick="show('jobs')" id="b-jobs" class="active">💼 Jobs</button>
<button onclick="show('learn')" id="b-learn">🎓 Learnerships</button>
<button onclick="show('cv')" id="b-cv">📄 CV Maker</button>
<button onclick="show('burs')" id="b-burs">🎓 Bursaries</button>
<button onclick="show('sassa')" id="b-sassa">💰 SASSA</button>
<button onclick="show('rdp')" id="b-rdp">🏠 RDP</button>
</nav>

<div id="jobs" class="section active">
<div class="card"><h3>Shoprite Cashier - Makhado</h3><p>Grade 11/12 • No experience • R5 500</p><a href="https://www.shopriteholdings.co.za/careers.html" target="_blank">Apply on Shoprite</a></div>
<div class="card"><h3>Boxer Store Assistant</h3><p>Grade 12 • Retail experience advantage</p><a href="https://boxer.co.za/careers" target="_blank">Apply on Boxer</a></div>
<div class="card"><h3>General Worker - Municipality</h3><p>Makhado Local Municipality</p><a href="https://www.makhado.gov.za" target="_blank">Check Municipality Site</a></div>
</div>

<div id="learn" class="section">
<div class="card"><h3>What is Learnership?</h3><p>12 months paid learning. You get stipend + qualification.</p></div>
<div class="card"><h3>Where to Apply</h3><p>• sayouth.mobi (FREE) • Dept Labour • SETA websites</p><a href="https://sayouth.mobi" target="_blank">Open SAYouth.mobi</a></div>
</div>

<div id="cv" class="section">
<div class="card"><h3>Create Your CV</h3>
<input id="n" placeholder="Full Names: e.g. John Smith">
<input id="p" placeholder="Phone: e.g. 072 123 4567">
<input id="e" placeholder="Email">
<textarea id="x" placeholder="Experience & Education"></textarea>
<button class="btn" onclick="makeCV()">Generate CV Text</button>
<textarea id="out" style="height:200px;margin-top:10px" placeholder="Your CV will appear here..."></textarea>
</div></div>

<div id="burs" class="section">
<div class="card"><h3>NSFAS Bursary</h3><p>For TVET & University. Household income under R350k.</p><a href="https://www.nsfas.org.za" target="_blank">Apply on NSFAS</a></div>
<div class="card"><h3>Funza Lushaka - Teaching</h3><a href="https://www.funzalushaka.doe.gov.za" target="_blank">Apply Here</a></div>
</div>

<div id="sassa" class="section">
<div class="card"><h3>SRD R370 Grant Status</h3><p>Check on official site:</p><a href="https://srd.sassa.gov.za/sc19/status" target="_blank">Check SRD Status</a></div>
<div class="card"><h3>SASSA Offices Limpopo</h3><p>Makhado: 015 519 3000 • Thohoyandou: 015 960 3200</p></div>
</div>

<div id="rdp" class="section">
<div class="card"><h3>RDP Housing Application</h3><p>Go to your Local Municipality with: ID, Proof of income, Proof of residence.</p><p>Makhado Municipality Housing: 015 519 3000</p></div>
</div>

<script>
function show(id){
 document.querySelectorAll('.section').forEach(s=>s.classList.remove('active'));
 document.getElementById(id).classList.add('active');
 document.querySelectorAll('nav button').forEach(b=>b.classList.remove('active'));
 document.getElementById('b-'+id).classList.add('active');
}
function makeCV(){
 let name=document.getElementById('n').value;
 let phone=document.getElementById('p').value;
 let email=document.getElementById('e').value;
 let exp=document.getElementById('x').value;
 let cv="CURRICULUM VITAE\\n\\nName: "+name+"\\nPhone: "+phone+"\\nEmail: "+email+"\\n\\nEDUCATION & EXPERIENCE:\\n"+exp+"\\n\\nReferences available on request";
 document.getElementById('out').value=cv;
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return HTML

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
