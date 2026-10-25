"""Rebuild the two-page public CV. Requires reportlab; source data is owner-supplied."""
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
FONT = Path('/usr/share/fonts/truetype/dejavu')
for name, file in [('CV','DejaVuSans.ttf'),('CV-Bold','DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT / file)))
pdfmetrics.registerFontFamily('CV',normal='CV',bold='CV-Bold',italic='CV',boldItalic='CV-Bold')
ink=colors.HexColor('#173b34');soft=colors.HexColor('#40534d');accent=colors.HexColor('#087b66')
styles={
 'name':ParagraphStyle('name',fontName='CV-Bold',fontSize=23,leading=28,textColor=ink,spaceAfter=7),
 'subtitle':ParagraphStyle('subtitle',fontName='CV',fontSize=11,leading=15,textColor=accent,spaceAfter=10),
 'body':ParagraphStyle('body',fontName='CV',fontSize=9.2,leading=13,textColor=soft,spaceAfter=8),
 'section':ParagraphStyle('section',fontName='CV-Bold',fontSize=10,leading=14,textColor=accent,spaceBefore=12,spaceAfter=8),
 'project':ParagraphStyle('project',fontName='CV-Bold',fontSize=10.5,leading=15,textColor=ink,spaceBefore=4,spaceAfter=6),
 'small':ParagraphStyle('small',fontName='CV',fontSize=8,leading=11,textColor=soft,spaceAfter=7),
 'bullet':ParagraphStyle('bullet',fontName='CV',fontSize=9.1,leading=13,textColor=soft,leftIndent=11,firstLineIndent=-9,spaceAfter=3),
}
content=[]
def p(text,kind='body'):return Paragraph(text,styles[kind])
def add(text,kind='body'):content.append(p(text,kind))
def section(text):add(text.upper(),'section')
def project(title,stack,bullets,repo):
 block=[p(title,'project'),p(stack,'small')]
 block += [p('• '+escape(text),'bullet') for text in bullets]
 block += [p('<link href="https://github.com/blesszaglago-cmd/'+repo+'" color="#087b66">github.com/blesszaglago-cmd/'+repo+'</link>','small')]
 content.append(KeepTogether(block))
add('BLESS MAWUMENYO ZAGLAGO','name')
add('Computer Science Student | Software & Machine Learning','subtitle')
add('Ghana  |  +233 55 375 1453  |  <link href="mailto:blesszaglago@gmail.com">blesszaglago@gmail.com</link><br/><link href="https://bless-zaglago.vercel.app/">bless-zaglago.vercel.app</link>  |  <link href="https://github.com/blesszaglago-cmd">github.com/blesszaglago-cmd</link><br/><link href="https://www.linkedin.com/in/bless-mawumenyo-zaglago">linkedin.com/in/bless-mawumenyo-zaglago</link>','small')
section('Profile')
add('Level 300 BSc Computer Science student at Ghana Communication Technology University, with a cumulative GPA of 3.64. Build machine-learning pipelines, Python APIs and full-stack applications. Projects include a neural network implemented in NumPy, a fraud-detection model and a live Ghana-focused opportunity platform. Interested in software and machine-learning internships.')
section('Technical skills')
for label,value in [
 ('Languages','Python, SQL, C++, JavaScript, PHP, HTML, CSS.'),
 ('Machine learning','Neural networks, backpropagation, gradient descent, regression, classification, SMOTE, ROC-AUC, precision, recall and F1.'),
 ('Libraries & data','NumPy, pandas, scikit-learn, Matplotlib, Power BI, Excel.'),
 ('Engineering','FastAPI, REST APIs, Next.js, React, PostgreSQL, MySQL, Supabase, Vercel, Git/GitHub. Docker: currently learning.')]:
 add('<b>'+escape(label)+':</b> '+escape(value))
section('Selected projects')
project('ZagJobSearch, now jobs.ac.ghana','Next.js / React | FastAPI | Supabase / PostgreSQL | Vercel',[
 'Built a live Ghana-focused platform for jobs, internships, remote roles explicitly open to Ghana-based applicants, and eligible scholarships/research funding.',
 'Implemented accounts and a private application tracker with statuses, notes and follow-up dates. Apply redirects to the original source after sign-in.',
 'Improved deadline checks, source retry queues, account security, cookie preferences and search discovery. Live: zagjobsearch.vercel.app.'
],'zagjobsearch')
project('Credit Card Fraud Detection','Python | scikit-learn | SMOTE | FastAPI',[
 'Built a classification pipeline on 284,807 transactions with 0.172% fraud. Applied SMOTE to training data only and retained the test-set class distribution.',
 'Random Forest achieved 98.26% ROC-AUC on 56,962 test transactions, identifying 82 of 98 frauds with 40 false positives. Added a local FastAPI prediction service.'
],'fraud-detection-ml')
content.append(PageBreak())
add('BLESS MAWUMENYO ZAGLAGO','project')
add('Projects, education and credentials','small')
project('Neural Network from Scratch','Python | NumPy | Iris dataset',[
 'Implemented a 4-8-3 feedforward network with ReLU, Softmax, cross-entropy loss, backpropagation and gradient descent.',
 'Reached 100% accuracy on the project’s Iris test split, with training loss falling to 0.06 over 1,000 epochs.'
],'nn-from-scratch')
project('Student Grade Predictor','Python | pandas | scikit-learn | Linear regression',[
 'Built a pipeline from generated study data to training, evaluation, prediction and coefficient visualisation.',
 'Predicted final grades from study hours, attendance and previous scores. Reported MAE 3.99 and R² 0.84 on the project test split.'
],'student-grade-predictor')
project('SmartEvents | Team Lead, group of four','HTML | CSS | JavaScript | PHP | MySQL | GCTU team project',[
 'Led a four-person team on an event-management and ticketing project covering registration, tiered tickets, QR check-in and reporting workflows.',
 'Contributed to SRS requirements, UML, ER/database modelling and web development with a PHP/MySQL backend.'
],'smartevents-system')
section('Education')
add('<b>BSc Computer Science</b> | Ghana Communication Technology University<br/>Level 300 | Expected graduation: 2028<br/>Cumulative GPA: 3.64 | First-year GPA: 3.68')
add('<b>A-grade coursework:</b> Linear Algebra, Probability &amp; Statistics, Calculus, Physics for Computing Systems, Logic in Computer Science, Discrete Mathematics.','small')
add('<b>WASSCE, General Science</b> | Anlo Senior High School | 2024')
section('Certifications & course credentials | 2026')
for text in [
 'Oracle Cloud Infrastructure AI Foundations Associate | Oracle | September 2026',
 'Oracle Certified Foundations Associate, Agentic AI | Oracle | August 2026',
 'Introduction to Modern AI | Cisco | September 2026',
 'Data Science Essentials with Python | Cisco | September 2026',
 'SQL and Relational Databases 101 | IBM | September 2026',
 'AWS for Beginners | Simplilearn | September 2026']:
 add('• '+escape(text),'bullet')
def footer(canvas,doc):
 canvas.setStrokeColor(colors.HexColor('#d5e3da'));canvas.line(42,35,A4[0]-42,35)
 canvas.setFont('CV',7);canvas.setFillColor(soft)
 canvas.drawString(42,23,'Bless Mawumenyo Zaglago | Updated October 2026')
 canvas.drawRightString(A4[0]-42,23,str(doc.page))
doc=SimpleDocTemplate(str(ROOT/'resume.pdf'),pagesize=A4,rightMargin=43,leftMargin=43,topMargin=37,bottomMargin=49,title='Bless Mawumenyo Zaglago - CV',author='Bless Mawumenyo Zaglago')
doc.build(content,onFirstPage=footer,onLaterPages=footer)
print('Updated resume.pdf')
