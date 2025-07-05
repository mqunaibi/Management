# Copyright (c) 2025, Best Performance and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Meeting(Document):
    def on_submit(self):
        self.send_invitation_emails()

    def send_invitation_emails(self):
        attendees = frappe.get_all(
            'Meeting Attendance',
            filters={'parent': self.name},
            fields=['attendee_name', 'email']
        )

        for attendee in attendees:
            if attendee.get("email"):
                html = f"""
<div style="border:1px solid #ddd; padding:20px; font-family:'Arial'; direction:rtl; text-align:right;">
    <h3 style="color:#007bff;">دعوة لحضور اجتماع</h3>
    <p>مرحبًا،<br><br>
    يوجد لديكم موعد اجتماع:</p>
    <table style="width:100%; border-collapse:collapse;">
        <tr><td style="padding:5px;"><strong>التاريخ:</strong></td><td>{self.meeting_date or 'غير محدد'}</td></tr>
        <tr><td style="padding:5px;"><strong>الوقت:</strong></td><td>{self.meeting_time or 'غير محدد'} - {self.end_time or ''}</td></tr>
        <tr><td style="padding:5px;"><strong>الموقع:</strong></td><td>{self.location or 'غير محدد'}</td></tr>
        <tr><td style="padding:5px;"><strong>رابط الاجتماع:</strong></td><td><a href="{self.meeting_url}">{self.meeting_url}</a></td></tr>
        <tr><td style="padding:5px;"><strong>الموضوع:</strong></td><td>{self.meeting_subject or 'غير محدد'}</td></tr>
        <tr><td style="padding:5px;"><strong>الحضور:</strong></td><td>{attendee.attendee_name}</td></tr>
        <tr><td style="padding:5px;"><strong>اسم مدير الاجتماع:</strong></td><td>{self.meeting_manager or 'غير محدد'}</td></tr>
    </table>
    <p style="margin-top:20px;">يرجى التأكيد على الحضور أو التواصل في حال وجود أي استفسارات.<br><br>
    شكرًا لكم،</p>
</div>
"""


                frappe.sendmail(
                    recipients=[attendee.email],
                    subject=f"دعوة لحضور الاجتماع: {self.meeting_subject}",
                    message=html
                )

