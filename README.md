**🇲🇾 Malaysia LHDN E-Invoicing – A Frappe ERPNext App**

A Frappe ERPNext app designed to help businesses in Malaysia comply with LHDN e-Invoicing regulations,
 supporting both versions of the standard.

**🚀 Features**

✅ Compliance with LHDN E-Invoicing for Version 1.0 and Version 1.1

✅ Seamless integration with LHDN APIs for integration, submission, validation & cancellation

✅ Secure digital certificate management for Version 1.1 and XML signing for both versions

✅ Automatic access token retrieval & renewal

✅ Support for a wide range of document types:

    Standard Invoices
    Credit Notes
    Debit Notes
    Refund Notes
    Self-Billed Invoices
    Self-Billed Credit Notes
    Self-Billed Debit Notes
    Self-Billed Refund Notes

✅ QR Code generation and attachment to invoices

✅ Automatic submission to LHDN for both submission and validation

✅ Comprehensive success logging and error handling for audit trails

✅ Reports comparing ERPNext invoices with LHDN portal statistics

✅ Integrated LHDN Dashboard System for real-time insights and monitoring

**🧾 Invoice Consolidation Support:**

✅ Merge multiple standard Sales Invoices into one consolidated invoice

✅ Generate valid XML for consolidated invoice and submit it to LHDN as a standard invoice

✅ Automatically assign QR code and attach it to the consolidated invoice

✅ Track source invoice references via a link field for complete audit traceability

**🔹 Compatibility**

🌐 ERPNext Versions: 15 and 16


# Get the app from GitHub
bench get-app https://github.com/matiyas-solutions/myinvois-erp.git

# Install the app on your site
bench --site yoursite.com install-app myinvois_erpgulf

# Apply necessary migrations
bench --site yoursite.com migrate

# Restart bench or supervisor

bench restart
# OR

sudo service supervisor restart


**🔹 Verify Installation**

1️⃣ Log in to ERPNext

2️⃣ Navigate to Help → About

3️⃣ Confirm the LHDN app is listed

**📈 Project Status**

Feature Details 🔓 License MIT (Or another license)

**🛠 Maintenance**

✅ Actively Maintained

🔄 PRs Welcome

✅ Contributions Encouraged

🏆 Open Source ✅

🎥 Watch our step-by-step tutorial on YouTube:https://youtu.be/ExhjZv2zHaY

**🌟 Development & Contributions**

We welcome contributions! To contribute:

1️⃣ Fork this repository

2️⃣ Improve the code, add features, or fix bugs

3️⃣ Submit a Pull Request for review

4️⃣ Report issues via the Issues section

Your contributions make this project better! 🙌

**📩 Support & Customization**

For implementation support or customization, contact: 📧 business@matiyas.com (Matiyas Solutions LLP)

**👥 Social**

Stay connected and join the community! 🚀

With this app, you're ready to be fully LHDN-compliant! 🎯

