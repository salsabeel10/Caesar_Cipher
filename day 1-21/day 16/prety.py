from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon",["Pikachu","Dragon","Minion"])
table.add_column("Type",["Electric","Fire","Water"])
table.align="r"

print(table)