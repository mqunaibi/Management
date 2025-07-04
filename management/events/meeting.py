import frappe

def before_save(doc, method=None):
    if doc.status == "Confirmed":
        send_invitation_email(doc)

def send_invitation_email(doc):
    recipients = [att.attendee for att in doc.attendees if att.attendee]
    if not recipients:
        return

    frappe.sendmail(
        recipients=recipients,
        subject=f"Meeting Confirmation: {doc.title}",
        message=f"Dear all, your meeting '{doc.title}' is confirmed and will be held on {doc.date}."
    )
