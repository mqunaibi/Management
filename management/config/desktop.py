from frappe import _

def get_data():
    return [
        {
            "module_name": "Management",
            "type": "module",
            "label": _("Management"),
            "color": "#589494",
            "icon": "octicon octicon-briefcase",
            "link": "List/Meeting/List",
            "items": [
                {
                    "type": "doctype",
                    "name": "Meeting",
                    "label": _("Meeting"),
                    "description": _("Manage meetings"),
                },
                {
                    "type": "doctype",
                    "name": "Permit",
                    "label": _("Permit"),
                    "description": _("Request or track permits"),
                }
            ]
        }
    ]
