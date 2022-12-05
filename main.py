from menu.menuPrincipal import mainMenu
from queries.tables import delete_tables, create_tables

#delete_tables("LP2Final.db")

create_tables("LP2Final.db")

mainMenu()