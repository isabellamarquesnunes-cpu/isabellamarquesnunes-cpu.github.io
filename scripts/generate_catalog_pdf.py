from pathlib import Path
import shutil

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "output" / "pdf"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_PDF = OUTPUT_DIR / "Catalogo-Isabella-Marques.pdf"
SITE_PDF = ROOT / "Catalogo-Isabella-Marques.pdf"

BURGUNDY = colors.HexColor("#78334D")
PINK = colors.HexColor("#B75F83")
BLUSH = colors.HexColor("#FBF0F4")
LINE = colors.HexColor("#E9CBD7")
GOLD = colors.HexColor("#BD803F")
GREEN = colors.HexColor("#4F6649")
INK = colors.HexColor("#322B31")
MUTED = colors.HexColor("#7B7077")
WHITE = colors.white

pdfmetrics.registerFont(TTFont("Georgia", r"C:\Windows\Fonts\georgia.ttf"))
pdfmetrics.registerFont(TTFont("Georgia-Italic", r"C:\Windows\Fonts\georgiai.ttf"))
pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))

styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="Brand",
        fontName="Georgia-Italic",
        fontSize=27,
        leading=31,
        textColor=BURGUNDY,
    )
)
styles.add(
    ParagraphStyle(
        name="Eyebrow",
        fontName="Arial-Bold",
        fontSize=8.5,
        leading=11,
        tracking=2.4,
        textColor=PINK,
    )
)
styles.add(
    ParagraphStyle(
        name="Section",
        fontName="Arial-Bold",
        fontSize=9,
        leading=11,
        textColor=GOLD,
        spaceAfter=2,
    )
)
styles.add(
    ParagraphStyle(
        name="SectionDesc",
        fontName="Arial",
        fontSize=8.4,
        leading=11,
        textColor=MUTED,
    )
)
styles.add(
    ParagraphStyle(
        name="ServiceTitle",
        fontName="Georgia",
        fontSize=12.2,
        leading=15,
        textColor=BURGUNDY,
    )
)
styles.add(
    ParagraphStyle(
        name="Tagline",
        fontName="Arial-Bold",
        fontSize=7.6,
        leading=9.5,
        textColor=GOLD,
        spaceBefore=2,
    )
)
styles.add(
    ParagraphStyle(
        name="Body",
        fontName="Arial",
        fontSize=8.1,
        leading=11,
        textColor=MUTED,
    )
)
styles.add(
    ParagraphStyle(
        name="Price",
        fontName="Arial-Bold",
        fontSize=11,
        leading=13,
        textColor=GREEN,
    )
)
styles.add(
    ParagraphStyle(
        name="PriceDetail",
        fontName="Arial",
        fontSize=7.9,
        leading=10,
        textColor=MUTED,
        alignment=TA_RIGHT,
    )
)
styles.add(
    ParagraphStyle(
        name="Consult",
        fontName="Georgia-Italic",
        fontSize=10,
        leading=13,
        textColor=MUTED,
    )
)
styles.add(
    ParagraphStyle(
        name="Small",
        fontName="Arial",
        fontSize=7.4,
        leading=9.5,
        textColor=MUTED,
    )
)
styles.add(
    ParagraphStyle(
        name="ContactTitle",
        fontName="Georgia-Italic",
        fontSize=16,
        leading=19,
        textColor=BURGUNDY,
    )
)


SERVICES = [
    {
        "name": "Corte Estratégico + Finalização + Secagem",
        "tagline": "",
        "items": "Corte estratégico · Finalização · Secagem",
        "price": "R$ 100",
        "card": "Cartão R$ 106  ·  ou 3x R$ 36 no crédito",
    },
    {
        "name": "Tratamento HNR + Vapor de Ozônio",
        "tagline": "HIDRATAÇÃO, NUTRIÇÃO E RECONSTRUÇÃO - 3 EM 1",
        "items": "Blend de óleos vegetais · Vapor de ozônio · Finalização estruturada + secagem · Consultoria + avaliação capilar",
        "price": "R$ 140",
        "card": "Cartão R$ 149  ·  ou 3x R$ 50 no crédito",
    },
    {
        "name": "Corte Estratégico + Tratamento HNR + Vapor de Ozônio",
        "tagline": "HIDRATAÇÃO, NUTRIÇÃO E RECONSTRUÇÃO - 3 EM 1",
        "items": "Corte estratégico · Blend de óleos vegetais · Vapor de ozônio · Finalização estruturada + secagem · Consultoria + avaliação capilar",
        "price": "R$ 170",
        "card": "Cartão R$ 180  ·  ou 3x R$ 61 no crédito",
    },
    {
        "name": "Combo Profundo",
        "tagline": "CORTE E TRATAMENTO COM CONSULTORIA PERSONALIZADA",
        "items": "Corte estratégico · Acidificação · HNR · Vapor de ozônio · Finalização + secagem · Consultoria capilar",
        "price": "R$ 250",
        "card": "Cartão R$ 265  ·  ou 3x R$ 89 no crédito",
    },
    {
        "name": "Combo Umectação Profissional (Lipidioterapia)",
        "tagline": "NUTRIÇÃO PROFUNDA COM ÓLEOS VEGETAIS",
        "items": "Corte estratégico · Manteiga de murumuru · Óleo de semente de uva · Óleo de pimenta rosa",
        "consult": "Valor definido após avaliar comprimento, densidade e volume dos fios.",
    },
    {
        "name": "Peeling Capilar com Argila Preta & Carvão Ativado",
        "tagline": "LIMPEZA PROFUNDA E CUIDADO TÉCNICO DO COURO CABELUDO",
        "items": "Peeling capilar detox · Acidificação com vitaminas e aminoácidos · Vapor de ozônio · Finalização · Avaliação e consultoria capilar",
        "note": "Protocolo cosmético. Não substitui avaliação dermatológica.",
        "price": "R$ 250",
        "card": "Cartão R$ 265  ·  ou 3x R$ 90 no crédito",
    },
]


def service_card(service):
    rows = [[Paragraph(service["name"], styles["ServiceTitle"])]]
    if service.get("tagline"):
        rows.append([Paragraph(service["tagline"], styles["Tagline"])])
    rows.append([Paragraph(service["items"], styles["Body"])])
    if service.get("note"):
        rows.append([Paragraph(service["note"], styles["Small"])])

    if service.get("consult"):
        rows.append([Paragraph(service["consult"], styles["Consult"])])
    else:
        price = Paragraph(f'{service["price"]} <font name="Arial" size="7.8" color="#7B7077">à vista (PIX/dinheiro)</font>', styles["Price"])
        detail = Paragraph(service["card"], styles["PriceDetail"])
        price_table = Table([[price, detail]], colWidths=[65 * mm, 101 * mm])
        price_table.setStyle(
            TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                    ("TOPPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ]
            )
        )
        rows.append([price_table])

    table = Table(rows, colWidths=[166 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), WHITE),
                ("BOX", (0, 0), (-1, -1), 0.8, LINE),
                ("LINEABOVE", (0, 0), (0, 0), 2.4, PINK),
                ("LEFTPADDING", (0, 0), (-1, -1), 8 * mm),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8 * mm),
                ("TOPPADDING", (0, 0), (-1, 0), 4 * mm),
                ("BOTTOMPADDING", (0, -1), (-1, -1), 4 * mm),
                ("TOPPADDING", (0, 1), (-1, -1), 1.2 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -2), 1.2 * mm),
            ]
        )
    )
    return KeepTogether([table, Spacer(1, 4.5 * mm)])


def section_header(title, description):
    table = Table(
        [
            [Paragraph(title, styles["Section"])],
            [Paragraph(description, styles["SectionDesc"])],
        ],
        colWidths=[166 * mm],
    )
    table.setStyle(
        TableStyle(
            [
                ("LINEBELOW", (0, -1), (-1, -1), 0.5, LINE),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, -1), (-1, -1), 3 * mm),
            ]
        )
    )
    return KeepTogether([table, Spacer(1, 4 * mm)])


def page_frame(canvas, doc):
    width, height = A4
    canvas.saveState()
    canvas.setFillColor(BLUSH)
    canvas.rect(0, height - 25 * mm, width, 25 * mm, fill=1, stroke=0)
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(0.8)
    canvas.line(23 * mm, height - 25 * mm, width - 23 * mm, height - 25 * mm)
    canvas.setFont("Georgia-Italic", 15)
    canvas.setFillColor(BURGUNDY)
    canvas.drawString(23 * mm, height - 16 * mm, "Isabella Marques")
    canvas.setFont("Arial", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawRightString(width - 23 * mm, height - 16 * mm, "Catálogo de Serviços · Unaí/MG")
    canvas.setFont("Arial", 7)
    canvas.drawCentredString(
        width / 2,
        10 * mm,
        f"Isabella Marques · Especialista em cabelos ondulados, cacheados e crespos · {doc.page}",
    )
    canvas.restoreState()


def first_page_frame(canvas, doc):
    width, height = A4
    canvas.saveState()
    canvas.setFillColor(BLUSH)
    canvas.rect(0, height - 53 * mm, width, 53 * mm, fill=1, stroke=0)
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(0.8)
    canvas.line(23 * mm, height - 53 * mm, width - 23 * mm, height - 53 * mm)
    canvas.setFont("Georgia-Italic", 27)
    canvas.setFillColor(BURGUNDY)
    canvas.drawString(23 * mm, height - 25 * mm, "Isabella Marques")
    canvas.setFont("Arial-Bold", 8.5)
    canvas.setFillColor(PINK)
    canvas.drawString(23 * mm, height - 33 * mm, "E S P E C I A L I S T A   E M   C A C H O S")
    canvas.setFont("Arial", 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(23 * mm, height - 42 * mm, "Unaí/MG  ·  5,0 no Google com 278 avaliações")
    canvas.setFont("Georgia-Italic", 15)
    canvas.setFillColor(GOLD)
    canvas.drawRightString(width - 23 * mm, height - 25 * mm, "Catálogo de Serviços")
    canvas.setFont("Arial", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawRightString(width - 23 * mm, height - 34 * mm, "Atendimentos com avaliação capilar")
    canvas.drawRightString(width - 23 * mm, height - 39 * mm, "e orientação personalizada")
    canvas.setFont("Arial", 7)
    canvas.drawCentredString(
        width / 2,
        10 * mm,
        f"Isabella Marques · Especialista em cabelos ondulados, cacheados e crespos · {doc.page}",
    )
    canvas.restoreState()


def contact_card():
    whatsapp = '<link href="https://wa.me/5538999117983"><b>(38) 99911-7983</b></link>'
    instagram = '<link href="https://www.instagram.com/isabellacachos_/">Instagram: @isabellacachos_</link>'
    site = '<link href="https://isabellamarquesnunes-cpu.github.io/">Ver catálogo virtual</link>'
    rows = [
        [Paragraph("Agende pelo WhatsApp", styles["ContactTitle"])],
        [Paragraph(whatsapp, styles["Body"])],
        [Paragraph("R. Santa Luzia, 283 - Cachoeira · Unaí/MG · CEP 38610-280", styles["Body"])],
        [Paragraph(f"Seg a Sex: 13h às 18h  |  Sáb: 08h às 16h  |  {instagram}", styles["Body"])],
        [Paragraph(site, styles["Body"])],
        [Paragraph("Valores sujeitos a alteração sem aviso prévio.", styles["Small"])],
    ]
    table = Table(rows, colWidths=[166 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), BLUSH),
                ("BOX", (0, 0), (-1, -1), 0.8, LINE),
                ("LEFTPADDING", (0, 0), (-1, -1), 8 * mm),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8 * mm),
                ("TOPPADDING", (0, 0), (-1, 0), 5 * mm),
                ("BOTTOMPADDING", (0, -1), (-1, -1), 5 * mm),
                ("TOPPADDING", (0, 1), (-1, -1), 1 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -2), 1 * mm),
            ]
        )
    )
    return table


def build():
    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=A4,
        leftMargin=22 * mm,
        rightMargin=22 * mm,
        topMargin=59 * mm,
        bottomMargin=17 * mm,
        title="Catálogo de Serviços - Isabella Marques",
        author="Isabella Marques - Especialista em Cachos",
    )

    story = [
        section_header(
            "SERVIÇOS SIMPLES",
            "Para objetivos pontuais, com técnica e orientação em cada etapa",
        ),
        service_card(SERVICES[0]),
        service_card(SERVICES[1]),
        service_card(SERVICES[2]),
        PageBreak(),
        section_header(
            "COMBOS",
            "Experiências completas que unem corte, tratamento e finalização",
        ),
        service_card(SERVICES[3]),
        service_card(SERVICES[4]),
        section_header(
            "CUIDADO PROFUNDO",
            "Protocolo cosmético para o couro cabeludo e os fios",
        ),
        service_card(SERVICES[5]),
        Spacer(1, 1 * mm),
        contact_card(),
    ]
    doc.build(story, onFirstPage=first_page_frame, onLaterPages=page_frame)
    shutil.copyfile(OUTPUT_PDF, SITE_PDF)
    print(OUTPUT_PDF)
    print(SITE_PDF)


if __name__ == "__main__":
    build()
