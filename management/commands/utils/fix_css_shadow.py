import os
import click
from frappe.commands import pass_context

search_term = "#0000001a"
replacement = "rgba(0, 0, 0, 0.1)"
file_extensions = (".css", ".scss", ".js", ".html")
base_dirs = ["apps", "sites/assets"]

@click.command("fix-css-shadow")
@pass_context
def execute(ctx):
    click.echo("🔍 جاري البحث عن القيم الخاطئة واستبدالها...")
    modified_files = []

    for base_dir in base_dirs:
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                if file.endswith(file_extensions):
                    full_path = os.path.join(root, file)
                    try:
                        with open(full_path, encoding="utf-8") as f:
                            content = f.read()
                        if search_term in content:
                            content = content.replace(search_term, replacement)
                            with open(full_path, "w", encoding="utf-8") as f:
                                f.write(content)
                            modified_files.append(full_path)
                    except Exception:
                        continue

    if modified_files:
        click.echo("✔ تم تعديل الملفات التالية:")
        for path in modified_files:
            click.echo(f"  - {path}")
    else:
        click.echo("❌ لم يتم العثور على أي ملفات تحتوي على القيمة.")
