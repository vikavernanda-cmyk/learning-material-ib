from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

out='/mnt/data/Mechanics_Mock_Test.pdf'
font='/usr/share/fonts/liberation/LiberationSans-Regular.ttf'
bold='/usr/share/fonts/liberation/LiberationSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('DV',font)); pdfmetrics.registerFont(TTFont('DVB',bold))

questions = [
("A cyclist rides half a lap around a circular track of radius 20 m. Her distance and the magnitude of her displacement are:",["40π m; 0","20π m; 20 m","20π m; 40 m","40 m; 20π m"],"C","Distance = πR = 20π m. Displacement = 2R = 40 m.","Kinematics"),
("Which statement about treating an object as a particle is correct?",["The Earth can never be treated as a particle.","A gymnast's body can be treated as a particle when studying her somersault.","A train can be treated as a particle when calculating the time to cross a bridge of similar length.","A marathon runner can be treated as a particle when calculating the time to finish the race."],"D","Only the runner's total time ignores body size and shape.","Kinematics"),
("A car starts from rest with uniform acceleration and reaches 20 m/s in 8 s. Its displacement in these 8 s is:",["160 m","80 m","40 m","100 m"],"B","a = 20/8 = 2.5 m/s², so x = ½ × 2.5 × 8² = 80 m.","Kinematics"),
("A v–t graph of a toy car is a straight line rising from 0 to 6 m/s during 0–2 s, constant at 6 m/s during 2–5 s, then falling uniformly to 0 during 5–7 s. The total displacement is:",["30 m","24 m","36 m","42 m"],"A","Area under the graph = 6 + 18 + 6 = 30 m.","Kinematics"),
("An x–t graph of a car shows uniform motion from x = 0 to x = 6 m during 0–3 s, a horizontal line at x = 6 m during 3–5 s, and a return to x = 0 at t = 8 s. Which statement is correct?",["The speed during 0–3 s is 3 m/s.","The car is at rest during 3–5 s.","The average velocity over 0–8 s is 1.5 m/s.","The car moves in the same direction throughout."],"B","A flat x–t segment means rest. Speed during 0–3 s is 2 m/s. Average velocity over 0–8 s is 0.","Kinematics"),
("An object falls freely from rest from a height of 45 m. The time taken and the speed on reaching the ground are (g = 10 m/s²):",["9 s; 90 m/s","3 s; 15 m/s","4.5 s; 45 m/s","3 s; 30 m/s"],"D","t = √(2 × 45/10) = 3 s, and v = gt = 30 m/s.","Kinematics"),
("A truck travels at 90 km/h. The driver's reaction time is 0.8 s, and the maximum deceleration is 5 m/s². The minimum safe distance to the vehicle ahead is at least:",["62.5 m","100 m","82.5 m","20 m"],"C","v = 25 m/s. Reaction distance = 20 m. Braking distance = 25²/(2 × 5) = 62.5 m. Total = 82.5 m.","Kinematics"),
("An object moves in uniform circular motion with radius 0.2 m and period 4 s. Its linear speed and angular speed are:",["0.8π m/s; 0.5π rad/s","0.1π m/s; 2π rad/s","0.5π m/s; 0.1π rad/s","0.1π m/s; 0.5π rad/s"],"D","v = 2πr/T = 0.1π m/s, and ω = 2π/T = 0.5π rad/s.","Kinematics"),
("A small ball moves in uniform circular motion with angular speed 10 rad/s at a distance of 5 cm from the centre. Its centripetal acceleration is:",["0.5 m/s²","5 m/s²","50 m/s²","500 m/s²"],"B","a = ω²r = 100 × 0.05 = 5 m/s² (convert cm to m first).","Kinematics"),
("An object weighs 90 N on Earth. On a planet where g is one third of Earth's, its weight is:",["270 N","90 N","30 N","10 N"],"C","Mass is unchanged, so the weight is 90/3 = 30 N.","Newton's laws"),
("A spring has natural length 0.4 m and k = 50 N/m. When a 10 N force compresses it, its length becomes:",["0.2 m","0.6 m","0.3 m","0.5 m"],"A","x = F/k = 0.2 m, so the length is 0.4 − 0.2 = 0.2 m.","Newton's laws"),
("Two forces of 6 N and 8 N act on one object. The magnitude of their resultant CANNOT be:",["2 N","10 N","14 N","15 N"],"D","The range is 2 N to 14 N, so 15 N is impossible.","Newton's laws"),
("Which statement is incorrect?",["When a car accelerates on a level road, static friction from the ground on the driving wheels points forward.","A book is pressed against a vertical wall by a hand and stays at rest. Pressing harder increases the friction on the book.","Static friction can act on a moving object.","Kinetic friction has magnitude f = μN."],"B","The friction equals the book's weight and does not depend on the pressing force.","Newton's laws"),
("A 60 kg person stands in an elevator that accelerates downward at 2 m/s². The force the person exerts on the floor is (g = 10 m/s²):",["720 N","600 N","480 N","120 N"],"C","N = m(g − a) = 60 × 8 = 480 N.","Newton's laws"),
("A 4 kg block rests on horizontal ground with coefficient of kinetic friction 0.5. A horizontal force of 30 N pulls it. Its acceleration is (g = 10 m/s²):",["2.5 m/s²","7.5 m/s²","5 m/s²","10 m/s²"],"A","f = 0.5 × 40 = 20 N, so a = (30 − 20)/4 = 2.5 m/s².","Newton's laws"),
("Ball A (mass 2m) hangs from the ceiling by a light string. Ball B (mass m) hangs below A, joined to it by a light spring. Both are at rest. The string is cut. At that instant the accelerations of A and B are, respectively:",["g, 0","3g, 0","1.5g, 0","1.5g, g"],"C","The spring force is unchanged at mg. For A: (2mg + mg)/2m = 1.5g. For B: mg − mg = 0.","Newton's laws"),
("A ball is thrown horizontally at 15 m/s from a cliff 20 m high. Ignoring air resistance, its horizontal distance from the cliff when it lands is (g = 10 m/s²):",["15 m","30 m","45 m","60 m"],"B","t = √(2 × 20/10) = 2 s, so x = 15 × 2 = 30 m.","Projectile motion"),
("A force of 40 N acts at 60° above the horizontal and drags a box 5 m along a horizontal floor. The work done by the force is (cos 60° = 0.5):",["200 J","173 J","100 J","50 J"],"C","W = Fs cos θ = 40 × 5 × 0.5 = 100 J.","Work and energy"),
("A 2 kg object is lifted slowly from the ground to a shelf 3 m high. The work done by gravity and the change in gravitational potential energy are, respectively (g = 10 m/s²):",["+60 J; +60 J","−60 J; +60 J","−60 J; −60 J","+60 J; −60 J"],"B","W_G = −mgh = −60 J, and ΔEp = +60 J.","Work and energy"),
("A ball is thrown from a height of 5 m with speed 10 m/s. Ignoring air resistance, its speed on reaching the ground is (g = 10 m/s²):",["10 m/s","15 m/s","20 m/s","10√2 m/s"],"D","v² = 10² + 2 × 10 × 5 = 200, so v = 10√2 m/s. The launch direction does not matter.","Work and energy"),
("A car with engine power 45 kW moves at a constant 54 km/h on level ground. The resistance force on the car is:",["1.5 × 10³ N","3 × 10³ N","6 × 10³ N","2.5 × 10³ N"],"B","v = 15 m/s, and f = P/v = 45000/15 = 3000 N.","Work and energy"),
("A 2 kg object falls freely from rest. The instantaneous power of gravity at t = 3 s is (g = 10 m/s²):",["60 W","300 W","600 W","1200 W"],"C","v = gt = 30 m/s, so P = mgv = 2 × 10 × 30 = 600 W.","Work and energy"),
("A 0.2 kg ball hits a wall at 10 m/s and rebounds at 6 m/s in the opposite direction. The contact time is 0.02 s. The average force from the wall is:",["40 N","80 N","320 N","160 N"],"D","Δp = 0.2 × (6 − (−10)) = 3.2 kg·m/s. F = 3.2/0.02 = 160 N.","Momentum and impulse"),
("An object of mass 3 kg moves at 4 m/s. Its momentum and kinetic energy are:",["12 kg·m/s; 48 J","24 kg·m/s; 12 J","12 kg·m/s; 24 J","7 kg·m/s; 24 J"],"C","p = mv = 12 kg·m/s, and Ek = ½mv² = 24 J.","Momentum and impulse")]

styles=getSampleStyleSheet()
title=ParagraphStyle('title',fontName='DVB',fontSize=22,leading=27,textColor=colors.HexColor('#173A5E'),alignment=TA_CENTER,spaceAfter=8)
meta=ParagraphStyle('meta',fontName='DV',fontSize=10.5,leading=15,textColor=colors.HexColor('#52606D'),alignment=TA_CENTER)
qstyle=ParagraphStyle('q',fontName='DVB',fontSize=10.5,leading=15,textColor=colors.HexColor('#102A43'),spaceAfter=5)
opt=ParagraphStyle('opt',fontName='DV',fontSize=9.8,leading=14,leftIndent=13,firstLineIndent=-13,spaceAfter=2,textColor=colors.HexColor('#243B53'))
sub=ParagraphStyle('sub',fontName='DVB',fontSize=8.3,leading=11,textColor=colors.HexColor('#2B6CB0'),spaceAfter=4)
ans=ParagraphStyle('ans',fontName='DV',fontSize=9.5,leading=14,leftIndent=8,rightIndent=8,spaceAfter=7,backColor=colors.HexColor('#F0F7FF'),borderColor=colors.HexColor('#B7D7F0'),borderWidth=.5,borderPadding=6)
head=ParagraphStyle('head',fontName='DVB',fontSize=15,leading=19,textColor=colors.HexColor('#173A5E'),spaceAfter=12)

def footer(canvas, doc):
    canvas.saveState(); canvas.setFont('DV',8); canvas.setFillColor(colors.HexColor('#7B8794'))
    canvas.drawString(18*mm,10*mm,'Mechanics Mock Test')
    canvas.drawRightString(A4[0]-18*mm,10*mm,f'Page {doc.page}'); canvas.restoreState()

doc=SimpleDocTemplate(out,pagesize=A4,rightMargin=18*mm,leftMargin=18*mm,topMargin=18*mm,bottomMargin=18*mm,title='Mechanics Mock Test')
story=[Spacer(1,28*mm),Paragraph('Mechanics Mock Test',title),Paragraph('Topic: Mechanics',meta),Paragraph('Duration: 40 minutes  |  24 multiple-choice questions',meta),Spacer(1,12*mm),Paragraph('Instructions',head),Paragraph('Choose the best answer for each question. Mark one option: A, B, C, or D. The answer key and worked solutions are provided after the question section.',ParagraphStyle('instr',parent=meta,alignment=0,fontSize=10.5,leading=16)),PageBreak()]
letters='ABCD'
for i,(text,opts,a,sol,topic) in enumerate(questions,1):
    block=[Paragraph(topic.upper(),sub),Paragraph(f'{i}. {text}',qstyle)]
    for l,o in zip(letters,opts): block.append(Paragraph(f'{l}. {o}',opt))
    block.append(Spacer(1,3))
    story.append(KeepTogether(block))
story += [PageBreak(),Paragraph('Answer Key & Solutions',head)]
for i,(text,opts,a,sol,topic) in enumerate(questions,1):
    story.append(KeepTogether([Paragraph(f'{i}. Answer: <b>{a}</b>',qstyle),Paragraph(f'<b>Solution:</b> {sol}',ans)]))
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(out)
