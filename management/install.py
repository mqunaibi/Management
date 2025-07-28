import os
import shutil
import frappe

def after_install():
    # copy to erpnext و hrms
    try:
        shutil.copyfile('management/translations/ar_erpnext.csv', '/home/frappe/frappe-bench/apps/erpnext/erpnext/translations/ar.csv')
        shutil.copyfile('management/translations/ar_hrms.csv', '/home/frappe/frappe-bench/apps/hrms/hrms/translations/ar.csv')
        print("✔ Done")
    except Exception as e:
        print(f"❌ Error: {e}")

def copy_translation_files():
    base_path = "/home/frappe/frappe-bench/apps"
    app_path = os.path.dirname(os.path.abspath(__file__))

    files = {
        "erpnext": {
            "src": os.path.join(app_path, "translation_resources", "erpnext", "ar.csv"),
            "dst": os.path.join(base_path, "erpnext", "erpnext", "translations", "ar.csv"),
        },
        "hrms": {
            "src": os.path.join(app_path, "translation_resources", "hrms", "ar.csv"),
            "dst": os.path.join(base_path, "hrms", "hrms", "translations", "ar.csv"),
        }
    }

    for app, paths in files.items():
        try:
            shutil.copyfile(paths["src"], paths["dst"])
            print(f"[✓] Updated translation for {app}: {paths['dst']}")
        except Exception as e:
            print(f"[✗] Failed to update translation for {app}: {e}")
