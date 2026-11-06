# Copyright (c) 2025, ERPGulf and Contributors
# See license.txt

# import frappe
try:
	from frappe.tests import IntegrationTestCase
except ImportError:  # Frappe v15
	from frappe.tests.utils import FrappeTestCase as IntegrationTestCase


class TestLHDNSuccessLog(IntegrationTestCase):
	pass
