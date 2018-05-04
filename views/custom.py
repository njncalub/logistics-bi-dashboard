from flask import render_template
from sqlalchemy.sql import text

from services.database import db_service


def view_situation_2_1():
    query = """
SELECT
  unit_price,
  name,
  sku,
  shipping_type
FROM
  ims_sales_order_item
WHERE
  id_sales_order_item = 229884
;
    """.strip()
    result = db_service.db_engine.execute(text(query))
    
    context = {}
    context['query'] = query
    context['title'] = 'Situation 2.1'
    context['description'] = (
        "Write a query to display the unit_price, name, SKU, shipping_type of "
        "items with id_sales_order_item = 229884."
    )
    context['headers'] = ['unit_price', 'name', 'sku', 'shipping_type']
    context['rows'] = result.fetchall()
    
    return render_template('custom/situation.html', context=context)


def view_situation_2_2():
    query = """
SELECT
  items.id_sales_order_item,
  items.name,
  items.sku,
  statuses.status
FROM
  ims_sales_order_item AS items,
  ims_sales_order_item_status AS statuses
WHERE
  items.shipping_type = 'warehouse' AND
  statuses.status = 'delivered'
;
    """.strip()
    result = db_service.db_engine.execute(text(query))
    
    context = {}
    context['query'] = query
    context['title'] = 'Situation 2.2'
    context['description'] = (
        "Write a query to display the id_sales_order_item, name, SKU, "
        "sales_order_item_status for all the items with shipping_type = "
        "warehouse and status = delivered."
    )
    context['headers'] = ['id_sales_order_item', 'name', 'sku', 'status']
    context['rows'] = result.fetchall()
    
    return render_template('custom/situation.html', context=context)


def view_situation_2_3():
    query = """
SELECT
  SUM(unit_price) AS total_unit_price
FROM
  ims_sales_order_item
WHERE
  SHIPPING_TYPE = 'cross_docking'
;
    """.strip()
    result = db_service.db_engine.execute(text(query))
    
    context = {}
    context['query'] = query
    context['title'] = 'Situation 2.3'
    context['description'] = (
        "Write a query to display the total unit_price of all items which "
        "have shipping_type = cross_docking."
    )
    context['headers'] = ['total_unit_price']
    context['rows'] = result.fetchall()
    
    return render_template('custom/situation.html', context=context)


def view_situation_2_4():
    query = """
SELECT
  DISTINCT ON (items.id_sales_order_item)
  items.id_sales_order_item,
  items.name,
  items.sku
FROM
  ims_sales_order_item AS items,
  ims_sales_order_item_status AS statuses,
  ims_sales_order_item_status_history AS history
WHERE
  statuses.status = 'picklisted' AND
  history.created_at >= '2013-11-06' AND
  history.created_at < '2013-11-07'
;
    """.strip()
    result = db_service.db_engine.execute(text(query))
    
    context = {}
    context['query'] = query
    context['title'] = 'Situation 2.4'
    context['description'] = (
        "Write a query to display the id_sales_order_item, name, SKU for all "
        "the items that went to status = picklisted on anytime during the day "
        "on 11/6/2013."
    )
    context['headers'] = ['id_sales_order_item', 'name', 'sku']
    context['rows'] = result.fetchall()
    
    return render_template('custom/situation.html', context=context)


def view_situation_2_5():
    query = """
SELECT
  shipping_type,
  COUNT(shipping_type) AS total
FROM
  (
    SELECT
      items.shipping_type AS shipping_type
    FROM
      ims_sales_order_item AS items,
      ims_sales_order_item_status AS statuses,
      ims_sales_order_item_status_history AS history
    WHERE
      items.unit_price >= 50 AND
      items.unit_price <= 100 AND
      statuses.status = 'picklisted' AND
      history.created_at >= '2013-11-06' AND
      history.created_at < '2013-11-07'
    GROUP BY
      items.id_sales_order_item
  ) AS t
GROUP BY
  shipping_type
;
    """.strip()
    result = db_service.db_engine.execute(text(query))
    
    context = {}
    context['query'] = query
    context['title'] = 'Situation 2.5'
    context['description'] = (
        "Write a query to display the total count items for each of the 3 "
        "shipping types - marketplace, cross_docking, warehouse. The count "
        "should include only items which have a unit_price between 50 and "
        "100, and also went to status = picklisted on anytime during the day "
        "on 11/6/2013."
    )
    context['headers'] = ['shipping_type', 'total']
    context['rows'] = result.fetchall()
    
    return render_template('custom/situation.html', context=context)


def view_situation_2_6():
    query = """
SELECT
  items.fk_sales_order,
  items.id_sales_order_item,
  items.name,
  items.sku,
  statuses.status
FROM
  ims_sales_order_item AS items,
  ims_sales_order_item_status AS statuses,
  (
    SELECT
      fk_sales_order_item,
      fk_sales_order_item_status as id_status_before_last,
      created_at,
      ROW_NUMBER() OVER(
        PARTITION BY
          fk_sales_order_item
        ORDER BY
          created_at DESC) AS negative_index
    FROM
      ims_sales_order_item_status_history
  ) AS changes
WHERE
  changes.negative_index = 2 AND
  items.id_sales_order_item = changes.fk_sales_order_item AND
  statuses.id_sales_order_item_status = changes.id_status_before_last
;
    """.strip()
    result = db_service.db_engine.execute(text(query))
    
    context = {}
    context['query'] = query
    context['title'] = 'Situation 2.6'
    context['description'] = (
        "Write an SQL query to display the fk_sales_order, "
        "id_sales_order_item, name, SKU, status before last status for all "
        "the items having at least 2 statuses (eg: Item 1 have status a, b, "
        "c, d, e, f, g. The last status of the item 1 is g and the status "
        "before last status is f that need to be shown)."
    )
    context['headers'] = ['fk_sales_order', 'id_sales_order_item', 'name',
                          'sku', 'status']
    context['rows'] = result.fetchall()
    
    return render_template('custom/situation.html', context=context)
