from datetime import datetime
from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String, DateTime, ForeingnKey, create_engine, insert)

metadata = MetaData()

#Definicion de tabla
cookies = Table("cookies", metadata, 
            Column("cookie_id", Integer(), primary_key=True),
            Column("cookie_name", String(50), index=True),
            Column("cookie_recipe_url", String(255)),
            Column("cookie_sku", String(55)),
            Column("quality", Integer()),
            Column("unit_cost", Integer(15))
)

users = Table("users", metadata, 
            Column("user_id", Integer(), primary_key=True),
            Column("customer_number", Integer(), autoincrement=True),
            Column("username", String(15), nullable=False, unique=True),
            Column("email_address", String(255), nullable=False),
            Column("phone", String(20), nullable=False),
            Column("password", String(25), nullable=False),
            Column("created_on", DateTime(), default=datetime.now),
            Column("update_on", DateTime(), default=datetime.now, onupdate=datetime.now)
)

#Relacion entre tablas
orders = Table("orders", metadata,
            Column("order_id", Integer(), primary_key=True),
            Column("user_id", ForeingnKey("users.user_id"))
)

line_items = Table("line_items", metadata,
            Column("line_items_id", Integer(), primary_key=True),
            Column("order_id", ForeingnKey("orders.order_id")),
            Column("cookie_id", ForeingnKey("cookies.cookie_id")),
            Column("quantity", Integer()),
            Column("extended_cost", String(15))
)

#motor base dato

engine-create_engine('sqlite:///C:\\Users\\abeli\\OneDrive\\Documentos\\CENT35\\python-Flask-Instagram\\igclone\\virtual\\corebase.db')
connection-engine()
metadata.drop_all(engine)
metadata.create_all(engine)