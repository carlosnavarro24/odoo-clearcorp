# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Addons modules by CLEARCORP S.A.
#    Copyright (C) 2009-TODAY CLEARCORP S.A. (<http://clearcorp.co.cr>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
	"name" : "Account Voucher Prepayment",
	"author" : "CLEARCORP S.A",
	"version" : "0.1",
	'category': 'Accounting & Finance',
	"description": """ 
Account Voucher Prepayment:
===============================
Manual Payments:
-------------------------------
This module permits to associate manual payments from a specific invoice. 
""",
	"depends" : [
				"account",
				"account_voucher",
				],
	"data" : [
				'wizard/account_voucher_add_payments.xml',
				'account_invoice.xml'
			],
	'installable': False,
	'auto_install': False,
	'license': 'AGPL-3',
}
