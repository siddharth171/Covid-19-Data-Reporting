import xlwt
from reports import covid_statewise_stats


def generate_xls_report(data):
    '''Generating XLS sheet'''
    if not isinstance(data, dict):
        print("API data not in dictionary")
        return
    
    all_states = data.keys()
    state_stats_map = {}
    for state_name in all_states:
        total_cases = covid_statewise_stats.get_total_cases(state_name, data)
        state_stats_map.update({state_name: total_cases})
        
    print(state_stats_map)
    
    XLS_REPORT_FILENAME = "statewise_covid_reports.xls"
    create_xls(state_stats_map, XLS_REPORT_FILENAME)
    return XLS_REPORT_FILENAME

def create_xls(state_stats_map, xls_report_filename):
    '''Creating xls file
    '''
    print("creating xls....")
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet("All States")
    worksheet.write(0,0,"STATE")
    worksheet.write(0,1,"ACTIVE")
    
    for row, (state, count) in enumerate(state_stats_map.items(), 1):
        col = 0
        worksheet.write(row, col, state)
        worksheet.write(row, col+1, count)
        
    workbook.save(xls_report_filename)
        
    
    