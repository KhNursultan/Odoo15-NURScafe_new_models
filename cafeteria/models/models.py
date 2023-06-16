# -*- coding: utf-8 -*-

from odoo import models, fields, api



class employee_order(models.Model):
    _name = 'cafeteria.employee_order'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    products_id = fields.Many2one('cafeteria.product', string='product', domain=[('state_id', '=', 'Accessible')], required=True)
    price = fields.Integer(string='Product price',  compute='_quant')
    quantity = fields.Integer(string='Product quantity')
    order_date = fields.Date(string='order_date', default=fields.Datetime.now)

    def _quant(self):
        for record in self:
            record.price = record.products_id.price * record.quantity


class product(models.Model):
    _name = 'cafeteria.product'

    name = fields.Char(string='Name', size=64, required=True, translate=True)
    description = fields.Text(string='Description', required=True, translate=True)
    barcode = fields.Text(string='Barcode', required=True, translate=True)
    price = fields.Integer(string='Product price')
    quantity = fields.Integer(string='Product quantity')
    provider_id = fields.Many2one('cafeteria.provider', string='provider')
    type_id = fields.Many2one('cafeteria.type', string='type')
    state_id = fields.Many2one('cafeteria.state', string='state')
    product_id = fields.One2many('cafeteria.employee_order', 'products_id', string='products')
    expiry_date = fields.Date()

    _sql_constraints = [('name_uniq', 'unique (name)', "Title name already exists !"), ('barcode_uniq', 'unique (barcode)', "Barcode code already exists !")]




class provider(models.Model):
    _name = 'cafeteria.provider'

    name = fields.Char(string='Name', size=64, required=True, translate=True)
    provider_ids = fields.One2many('cafeteria.product', 'provider_id', string='providers')

    _sql_constraints = [('name2_uniq', 'unique (name)', "Title name already exists !")]


class state(models.Model):
    _name = 'cafeteria.state'

    name = fields.Char(string='Name', size=64, required=True, translate=True)
    state_id = fields.One2many('cafeteria.product', 'state_id', string='states')

    _sql_constraints = [('name3_uniq', 'unique (name)', "Title name already exists !")]


class typeProduct(models.Model):
    _name = 'cafeteria.type'

    name = fields.Char(string='Name', size=64, required=True, translate=True)
    type_products_ids = fields.One2many('cafeteria.product', 'type_id', string='products')

    _sql_constraints = [('name3_uniq', 'unique (name)', "Title name already exists !")]


class admin(models.Model):
    _name = "cafeteria.admin"
    _description = "Cafeteria Admin"
    _rec_name = "cafeterianame"

    cafeterianame = fields.Char(string='Cafeteria name', required=True)
    adminname = fields.Char(string='Administrator name', required=True)
    address = fields.Char(string='Address of Cafeteria')
    menu = fields.Text(string="Menu")
    menus_id = fields.Many2many('cafeteria.menus', 'cafeteria_id', string="GHJK")
    product_first = fields.Text(string='First', related="menus_id.product_first")
    product_second = fields.Text(string='Second', related="menus_id.product_second")
    product_salat = fields.Text(string='Salat', related="menus_id.product_salat")

    user_id = fields.Many2one(
        'res.users', string='Created by', index=True, tracking=True,
        default=lambda self: self.env.user, check_company=True)

    menu_clients = fields.Many2many('cafeteria.client', string="Cafeteria name")

    def copy(self, default=None):
         default = dict(default or {})
         if default is None:
             default = {}
         return super(admin, self).copy(default=default)

    def add_to_cart(self):
        return True


class menu(models.Model):
    _name = "cafeteria.menus"
    _description = "Menu Cafeteria"
    _rec_name = "menu_lines"
    menu = fields.Text(string="Menu")
    cafeteria_data = fields.Many2one('cafeteria.admin', string="Menu Lines")
    menu_lines = fields.One2many('cafeteria.menu', 'cafeteria_id', string="Menu Lines")
    product_first = fields.Text(string='First')
    product_second = fields.Text(string='Second')
    product_salat = fields.Text(string='Salat')
    cafeteria_id = fields.Many2one('cafeteria.admin', string='Cafeteria ID')
    menu_lines = fields.Many2one('cafeteria.admin', string="Menu Lines")
    menus_id = fields.One2many('cafeteria.menus', 'cafeteria_id', string="GHJK")
    cafeterianame = fields.Char(string='Cafeteria name', related="menu_lines.cafeterianame", required=True)
    menulike = fields.Char(string="Liked")


class client(models.Model):
    _name = "cafeteria.client"
    _description = "Client Survey"
    _rec_name = "cafeterianame"


    menu_lines = fields.Many2one('cafeteria.admin', string="Cafeteria")
    id = fields.Integer(string='Id', required=True)
    cafeterianame = fields.Char(string='Cafeteria name', related="menu_lines.cafeterianame", required=True)
    adminname = fields.Char(string='Administrator name', related="menu_lines.adminname", required=True)
    address = fields.Char(string='Address of Cafeteria', related="menu_lines.address")

    # Menu fields
    menus_choose = fields.Many2one('cafeteria.menus', string="Menu")
    product_first = fields.Text(string='First', related="menus_choose.product_first")
    product_second = fields.Text(string='Second', related="menus_choose.product_second")
    product_salat = fields.Text(string='Salat', related="menus_choose.product_salat")


    user = fields.Char(string="User")

    def like_menu(self):
        return True

    menu = fields.Text(string="Menu")

    menus_id = fields.One2many('cafeteria.menus', 'cafeteria_id', string="GHJK")

    def get_data(self):
        fetched_data = self.env['cafeteria.admin'].search([])
        return fetched_data






