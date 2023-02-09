# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import tagged

from .common import Common


# Use post_install to get all models loaded more info: odoo/odoo#13458
@tagged("post_install", "-at_install")
class TestCleanupPurgeLineModule(Common):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # create a nonexistent module
        cls.module = cls.env["ir.module.module"].create(
            {
                "name": "database_cleanup_test",
                "state": "to upgrade",
            }
        )

    def test_remove_to_upgrade_module(self):
        wizard = self.env["cleanup.purge.wizard.module"].create({})
        module_names = wizard.purge_line_ids.filtered(lambda x: not x.purged).mapped(
            "name"
        )
        self.assertTrue("database_cleanup_test" in module_names)
