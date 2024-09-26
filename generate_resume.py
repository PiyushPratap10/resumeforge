from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from typing import List, Dict

def generate_resume(name: str, email: str, phone: str, linkedin: str,
                    education: List[Dict], experience: List[str], skills: List[str],
                    projects: List[Dict], certifications: List[Dict], file_path: str):
    # Create the PDF document
    doc = SimpleDocTemplate(file_path, pagesize=letter)
    styles = getSampleStyleSheet()

    # Add title style
    title_style = styles['Heading1']
    title_style.alignment = TA_CENTER

    # Add heading style for sections
    heading_style = styles['Heading2']

    # Add normal text style
    normal_style = styles['BodyText']

    # Elements to be added to the PDF
    elements = []

    # Add Name
    elements.append(Paragraph(name, title_style))
    elements.append(Spacer(1, 12))

    # Add Contact Information
    contact_info = f"Email: {email} | Phone: {phone} | LinkedIn: {linkedin}"
    elements.append(Paragraph(contact_info, normal_style))
    elements.append(Spacer(1, 12))

    # Add Education Section
    elements.append(Paragraph("Education", heading_style))
    for edu in education:
        edu_text = f"{edu['degree']} in {edu['field']}, {edu['institution']}, {edu['duration']} - {edu['percentage']}%"
        elements.append(Paragraph(edu_text, normal_style))
        elements.append(Spacer(1, 6))

    elements.append(Spacer(1, 12))

    # Add Work Experience Section
    elements.append(Paragraph("Work Experience", heading_style))
    for exp in experience:
        elements.append(Paragraph(exp, normal_style))
        elements.append(Spacer(1, 6))

    elements.append(Spacer(1, 12))

    # Add Skills Section
    elements.append(Paragraph("Skills", heading_style))
    elements.append(Paragraph(', '.join(skills), normal_style))
    elements.append(Spacer(1, 12))

    # Add Projects Section
    elements.append(Paragraph("Projects", heading_style))
    for proj in projects:
        # Add Project Title
        elements.append(Paragraph(proj['title'], normal_style))
        # Add Project Link separately
        proj_link = f"<a href='{proj['link']}' color='blue'>{proj['link']}</a>"
        elements.append(Paragraph(proj_link, normal_style))
        # Add Project Description
        elements.append(Paragraph(proj['description'], normal_style))
        elements.append(Spacer(1, 6))

    elements.append(Spacer(1, 12))

    # Add Certifications Section
    elements.append(Paragraph("Certifications", heading_style))
    for cert in certifications:
        # Add Certification Name and Issuing Organization
        cert_text = f"{cert['name']} (Issued by: {cert['organization']})"
        elements.append(Paragraph(cert_text, normal_style))
        # Add Certification Link
        cert_link = f"<a href='{cert['link']}' color='blue'>{cert['link']}</a>"
        elements.append(Paragraph(cert_link, normal_style))
        elements.append(Spacer(1, 6))

    elements.append(Spacer(1, 12))

    # Build the PDF
    doc.build(elements)
