from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Types"
    _order = "sequence asc, property_ids desc"
    name = fields.Char(string="Name", required=True)
    property_ids = fields.One2many("estate.property", "property_type_id", string="Property")
    sequence = fields.Integer(string="Sequence", default=1)
    offer_ids = fields.Many2many("estate.property.offer", string="Offers", compute="_compute_offer")
    offer_count = fields.Integer(string="Offers Count", compute="_compute_offer")

    _sql_constraints = [
        ('unique_property_type_name', 'UNIQUE(name)', 'El nombre de la propiedad ya existe!'),
    ]

    def _compute_offer(self):
        # This solution is quite complex. It is likely that the trainee would have done a search in
        # a loop.
        data = self.env["estate.property.offer"].read_group(
            [("property_id.state", "!=", "canceled"), ("property_type_id", "!=", False)],
            ["ids:array_agg(id)", "property_type_id"],
            ["property_type_id"],
        )
        mapped_count = {d["property_type_id"][0]: d["property_type_id_count"] for d in data}
        mapped_ids = {d["property_type_id"][0]: d["ids"] for d in data}
        for prop_type in self:
            prop_type.offer_count = mapped_count.get(prop_type.id, 0)
            prop_type.offer_ids = mapped_ids.get(prop_type.id, [])

    def action_view_offers(self):
        res = self.env.ref("estate_property_offer_action_filter").read()[0]
        res["domain"] = [("id", "in", self.offer_ids.ids)]
        return res
