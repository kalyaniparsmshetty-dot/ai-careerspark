"""Custom CSS for the AI CareerSpark interface (injected with st.markdown)."""

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
:root{--navy:#0F1B3D;--blue:#2563EB;--violet:#6D5BD0;--muted:#52607F;--line:#DDE7F7;--soft:#EEF4FF;--bg:#F4F8FF;
--good:#0E8A5F;--warn:#9A6700;--bad:#B42318;}
html,body,[class*="css"],.stApp{font-family:'Plus Jakarta Sans',-apple-system,'Segoe UI',Roboto,Arial,sans-serif;color:var(--navy);}
.stApp{background:linear-gradient(180deg,#FFFFFF 0%,var(--bg) 320px);}
.block-container{max-width:1080px;padding-top:2.2rem;padding-bottom:3rem;}
h1,h2,h3{color:var(--navy);letter-spacing:-0.01em;}
header[data-testid="stHeader"]{background:transparent;}
:focus-visible{outline:3px solid #93B4FF!important;outline-offset:2px;}

/* sidebar */
[data-testid="stSidebar"]{background:#FFFFFF;border-right:1px solid var(--line);}
.brand{display:flex;align-items:center;gap:.6rem;font-weight:800;font-size:1.15rem;margin:.2rem 0 1rem;}
.brand .logo{width:34px;height:34px;border-radius:10px;background:linear-gradient(135deg,var(--blue),var(--violet));display:grid;place-items:center;}
.brand svg{width:20px;height:20px;stroke:#fff;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;}
[data-testid="stSidebar"] .stButton>button{justify-content:flex-start;border:0;background:transparent;color:var(--navy);font-weight:600;border-radius:10px;padding:.55rem .8rem;}
[data-testid="stSidebar"] .stButton>button:hover{background:var(--soft);color:var(--blue);}
[data-testid="stSidebar"] .stButton>button>div,[data-testid="stSidebar"] .stButton>button p{justify-content:flex-start!important;text-align:left!important;}
[data-testid="stSidebar"] .stButton>button{justify-content:flex-start!important;}
[data-testid="stSidebar"] [data-testid="stBaseButton-primary"]{background:#E3ECFF!important;color:var(--blue)!important;border:0!important;box-shadow:none!important;}
[data-testid="stSidebar"] [data-testid="stBaseButton-primary"] p{font-weight:700;}

/* buttons */
.stButton>button,.stDownloadButton>button{border-radius:10px;font-weight:600;border:1px solid var(--line);padding:.5rem 1.1rem;}
.main [data-testid="stBaseButton-primary"]{background:linear-gradient(135deg,var(--blue),var(--violet));border:0;color:#fff;box-shadow:0 6px 16px rgba(37,99,235,.25);}
.main [data-testid="stBaseButton-primary"]:hover{filter:brightness(1.06);color:#fff;}
.main [data-testid="stBaseButton-secondary"]:hover{border-color:var(--blue);color:var(--blue);}

/* inputs */
textarea,input{border-radius:12px!important;}
[data-testid="stTextArea"] textarea,[data-testid="stTextInput"] input{background:#fff;border:1px solid var(--line);}

/* hero */
.hero{background:#fff;border:1px solid var(--line);border-radius:24px;padding:clamp(1.5rem,4vw,3rem);box-shadow:0 12px 40px rgba(37,99,235,.08);margin-bottom:1.2rem;}
.hero h1{font-size:clamp(2rem,5vw,3.1rem);line-height:1.1;font-weight:800;margin:.8rem 0 .6rem;}
.hero .tag{font-size:1.15rem;font-weight:600;color:var(--blue);margin-bottom:.8rem;}
.hero p{color:var(--muted);font-size:1.05rem;line-height:1.65;max-width:62ch;}
.pill{display:inline-flex;align-items:center;gap:.4rem;background:var(--soft);color:var(--blue);border-radius:999px;padding:.25rem .8rem;font-size:.82rem;font-weight:700;}

/* cards */
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:1rem;margin:.6rem 0 1rem;}
.card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:1.1rem 1.2rem;box-shadow:0 4px 14px rgba(15,27,61,.05);}
.card.fixed{min-height:190px;margin-bottom:.6rem;}
.card h4{margin:.6rem 0 .3rem;font-size:1.02rem;font-weight:700;}
.card p{margin:0;color:var(--muted);font-size:.92rem;line-height:1.55;}
.ico{width:40px;height:40px;border-radius:12px;background:linear-gradient(135deg,#E3EDFF,#ECE8FF);display:grid;place-items:center;}
.ico svg{width:21px;height:21px;stroke:var(--blue);fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;}
.page-head{margin-bottom:1rem;}
.page-head h1{font-size:clamp(1.6rem,3.5vw,2.2rem);font-weight:800;margin:0 0 .25rem;}
.page-head p{color:var(--muted);margin:0;font-size:1rem;}
.notice{background:#fff;border:1px solid var(--line);border-left:4px solid var(--violet);border-radius:12px;padding:.8rem 1rem;color:var(--muted);font-size:.9rem;margin:.6rem 0 1rem;}
.empty{background:#fff;border:1.5px dashed #BFD0EE;border-radius:16px;padding:1.6rem;text-align:center;color:var(--muted);}
.section-title{font-size:1.05rem;font-weight:700;margin:1.2rem 0 .5rem;}

/* chips */
.chip{display:inline-block;border-radius:999px;padding:.22rem .75rem;margin:.18rem .25rem .18rem 0;font-size:.84rem;font-weight:600;border:1px solid var(--line);background:#fff;}
.chip.blue{background:#E8F0FF;color:#1D4FD7;border-color:#CFE0FF;}
.chip.good{background:#E6F7F0;color:var(--good);border-color:#BDE8D6;}
.chip.warn{background:#FFF4DB;color:var(--warn);border-color:#F3DFA5;}
.chip.violet{background:#EEEBFF;color:#5645B8;border-color:#D9D3FF;}
.chip.gray{background:#F1F4FA;color:var(--muted);}
.diff{font-size:.75rem;font-weight:700;border-radius:6px;padding:.1rem .5rem;margin-right:.4rem;}
.diff.Beginner{background:#E6F7F0;color:var(--good);} .diff.Intermediate{background:#FFF4DB;color:var(--warn);} .diff.Advanced{background:#FDE8E6;color:var(--bad);}

/* ring and bars */
.ring{width:150px;height:150px;border-radius:50%;background:conic-gradient(var(--blue) calc(var(--p)*1%),#E4ECFA 0);display:grid;place-items:center;margin:auto;}
.ring-in{width:112px;height:112px;border-radius:50%;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;}
.ring-in b{font-size:1.9rem;font-weight:800;line-height:1;} .ring-in span{font-size:.72rem;color:var(--muted);margin-top:.2rem;text-align:center;padding:0 .4rem;}
.bar-row{display:flex;align-items:center;gap:.7rem;margin:.4rem 0;font-size:.88rem;}
.bar-row .name{width:46%;color:var(--navy);font-weight:600;} .bar{flex:1;height:9px;background:#E4ECFA;border-radius:99px;overflow:hidden;}
.bar>i{display:block;height:100%;background:linear-gradient(90deg,var(--blue),var(--violet));border-radius:99px;} .bar-row .n{width:1.6rem;text-align:right;color:var(--muted);}
.steps{counter-reset:s;list-style:none;padding:0;margin:0;}
.steps li{counter-increment:s;position:relative;padding:.4rem 0 .4rem 2.6rem;color:var(--muted);}
.steps li::before{content:counter(s);position:absolute;left:0;top:.25rem;width:1.9rem;height:1.9rem;border-radius:50%;background:var(--soft);color:var(--blue);font-weight:800;display:grid;place-items:center;font-size:.85rem;}
.steps li b{color:var(--navy);}
.footer{margin-top:2.5rem;padding-top:1rem;border-top:1px solid var(--line);color:var(--muted);font-size:.84rem;text-align:center;}
@media (max-width:640px){.block-container{padding-left:1rem;padding-right:1rem;}.bar-row .name{width:40%;}}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important;}}
</style>
"""

HIDE_SIDEBAR = """
<style>[data-testid="stSidebar"],[data-testid="stSidebarCollapsedControl"],[data-testid="collapsedControl"]{display:none!important;}</style>
"""
