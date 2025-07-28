import os
import shutil

def after_install():
    print("Running after_install script for Management app...")

    translation_targets = [
        {
            "app": "erpnext",
            "target_path": "/home/frappe/frappe-bench/apps/erpnext/erpnext/translations/ar.csv",
            "source_path": "/home/frappe/frappe-bench/apps/management/management/translation_resources/erpnext/ar.csv"
        },
        {
            "app": "hrms",
            "target_path": "/home/frappe/frappe-bench/apps/hrms/hrms/translations/ar.csv",
            "source_path": "/home/frappe/frappe-bench/apps/management/management/translation_resources/hrms/ar.csv"
        }
    ]

    for t in translation_targets:
        try:
            if os.path.exists(t["source_path"]):
                shutil.copyfile(t["source_path"], t["target_path"])
                print(f"✅ Copied translation for {t['app']} successfully.")
            else:
                print(f"❌ Source file not found → {t['source_path']}")
        except Exception as e:
            print(f"❌ Failed to copy translation for {t['app']}: {e}")
