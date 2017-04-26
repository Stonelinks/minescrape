import os
import shutil
import time
import csv
from subprocess import check_output
from pyquery import PyQuery as pq

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY', 'AS', 'DC', 'Fm', 'GU', 'MH', 'MP', 'PW', 'UM']

headers = ['State', 'Mine ID', 'Operator', 'Mine Name', 'Type', 'Status', 'Commodity', 'Opr. Begin Date', 'Current Controller', 'Controller Start Date', 'Status Date', 'Mined Material', 'Location', 'Address of Record']

with open("output.csv", "wb") as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(headers)
    for state in states:
        print 'downloading state ' + state
        state_index = check_output(["./download_state.sh", state])
        table = pq(state_index)('table:last')
        for row in table('tr')[:-1]:
            cols = row.findall('td')
            if len(cols):
                out_row = [state]
                for col in cols[:6]:
                    field = pq(col).text()
                    out_row.append(field)
                mine_id = out_row[1]
                print 'downloading mine ' + mine_id
                mine_index = check_output(["./download_mine.sh", mine_id])
                for header in headers[7:]:
                    mine_col = pq(mine_index)("td:contains('" + header + ":')").parent().find('td')
                    mine_col_text = 'Unknown'
                    if len(mine_col) > 1:
                        mine_col_text = pq(mine_col[1]).text().encode('utf-8')
                    out_row.append(mine_col_text.strip())
                print out_row
                writer.writerow(out_row)
