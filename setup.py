from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="management",
    version="2.0.1",
    description="Management App for managing meetings and related tasks in ERPNext",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Best Performance",
    author_email="info@best-performance.co.uk",
    license="GPL-3.0",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
    entry_points={
        'frappe.commands': [
            'fix-css-shadow = management.management.commands.utils.fix_css_shadow:execute',
        ]
    },
)
