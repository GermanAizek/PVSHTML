from tabulate import tabulate

table = {"Code": [], "Message": [], "File": [], "Line": []}

#parsing log file
with open('p.tasks', 'r') as f:
    nums = f.read().splitlines()

html = """<html>
    <button>High</button>
    <button>Medium</button>
    <button>Low</button>
    <button>General</button>
    <button>Optimization</button>
    <button>64-bit</button>
    <button>Ru</button>
    <button>En</button>
"""

html += "<table><tbody>"

for line in nums:
    code = line.split('\t')[3].split()[0]
    html += '<tr><td><a href="https://pvs-studio.com/ru/docs/warnings/{0}">{0}</a></td></tr>'.format(code)
    table["Code"].append(code)
    message = line.split('\t')[3].replace(code, '')
    table["Message"].append(message)
    table["File"].append(line.split('\t')[0])
    table["Line"].append(line.split('\t')[1])

html += "</table></tbody>"

html += tabulate(table, headers="keys", tablefmt='html', stralign='center').replace('<table', '<table cellspacing="5" cellpadding="10" border="1" ').replace('<td', '<td style="text-align:left"')

with open('out.html', 'w') as f:
    f.write(html)

#with open('out.html', 'r') as f:
#    nums = f.read().splitlines()

#for line in nums:
#    line = line.replace('<tr>','<tr><a href="https://pvs-studio.com/ru/docs/warnings/{0}">{0}</a>'.format(code))
#    print(line)

#with open('out.html', 'w') as f:
#    f.write(html)

