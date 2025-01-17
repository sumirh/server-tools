.. image:: https://img.shields.io/badge/license-LGPL--3-blue.png
   :target: https://www.gnu.org/licenses/lgpl
   :alt: License: LGPL-3

======================
Kanban - Stage Support
======================

This module provides a stage model compatible with Kanban views and the
standard views needed to manage these stages. It also provides the
``base.kanban.abstract`` model, which can be inherited to add support for
Kanban views with stages to any other model. Lastly, it includes a base Kanban
view that can be extended as needed.

Installation
============

To install this module, simply follow the standard install process.

Configuration
=============

No configuration is needed or possible.

Usage
=====

* Inherit from ``base.kanban.abstract`` to add Kanban stage functionality to
  the child model:

  .. code-block:: python

    class MyModel(models.Model):
        _name = 'my.model'
        _inherit = 'base.kanban.abstract'

* Extend the provided base Kanban view (``base_kanban_abstract_view_kanban``)
  as needed by the child model while making sure to set the ``mode`` to
  ``primary`` so that inheritance works properly. The base view has four
  ``name`` attributes intended to provide convenient XPath access to different
  parts of the Kanban  card. They are ``card_dropdown_menu``, ``card_header``,
  ``card_body``, and ``card_footer``:

  .. code-block:: xml

    <record id="my_model_view_kanban" model="ir.ui.view">
        <field name="name">My Model - Kanban View</field>
        <field name="model">my.model</field>
        <field name="mode">primary</field>
        <field name="inherit_id" ref="base_kanban_stage.base_kanban_abstract_view_kanban"/>
        <field name="arch" type="xml">
            <xpath expr="//div[@name='card_header']">
                <!-- Add header content here -->
            </xpath>
            <xpath expr="//div[@name='card_body']">
                <!-- Add body content here -->
            </xpath>
        </field>
    </record>

* To manage stages, go to Settings > Technical > Kanban > Stages.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/162/13.0

Known Issues / Roadmap
======================

* The grouping logic used by ``base.kanban.abstract`` currently does not
  support additional domains and alternate sort orders

Bug Tracker
===========

Bugs are tracked on `GitHub Issue
<https://github.com/OCA/server-tools/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://odoo-community.org/logo.png>`_.

Contributors
------------

* Dave Lasley <dave@laslabs.com>
* Oleg Bulkin <obulkin@laslabs.com>
* Daniel Reis <dreis.pt@hotmail.com>
* Alex Comba <alex.comba@agilebg.com>
* Miquel Raïch <miquel.raich@forgeflow.com>
* Helly kapatel <helly.kapatel@initos.com>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.
