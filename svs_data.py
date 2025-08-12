# ============== SELWYN VET SERVICES SYSTEM ==============
# Student Name: 
# Student ID : 
# =============================================================


# * * * * * * * * * ======= WARNING ======= * * * * * * * * * * * 
# * * * Do not add any functions or variables to this file. * * *  
# * * *    It will be deleted and replaced for marking.     * * *
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

from datetime import date,datetime,timedelta

col_customers = {'ID':int,'Name':str,'Telephone':str,'e-mail':str}
db_customers = {394:{'details':['Peter Parker','022975284','pete@arachtech.nz'],
                    'bookings':{date(2025,4,22):[(55,),(),45.78,True]
                            }
                    },
                111:{'details':['Tamsyn Amorogato','0274823801','tamzlovescats@felines.co.nz'],
                    'bookings':{date(2025,9,15):[(57,56),(5,6),631.88,False],
                            date(2025,11,5):[(),(6,),78.09,False]
                            }
                    }
                }

col_services = {'ID':int,'Name':str,'Cost':float}
db_services = {55:['Consultation',45.78],
               56:['Dental Check',55.32],
               57:['Farm Visit',150.67]}

col_treatments = {'ID':int,'Name':str,'Cost':float}
db_treatments = {5:['Anathestic',347.80],
                 6:['Drench',78.09]}

col_invoices = {'Customer':str,'Telephone':str,'Date':datetime.date,'Amount':float}


def unique_id():
    """
    This will return the next available ID as a new integer value
    that is one higher than the current maximum ID number in the list.
    """
    
    return max(list(db_customers.keys())) + 1


def display_formatted_row(row, format_str):
    """
    row is a list or tuple containing the items in a single row.
    format_str uses the following format, with one set of curly braces {} for each column:
       eg, "{: <10}" determines the width of each column, padded with spaces (10 spaces in this example)
       <, ^ and > determine the alignment of the text: < (left aligned), ^ (centre aligned), > (right aligned)
    The following example is for 3 columns of output: left-aligned 5 characters wide; centred 10 characters; right-aligned 15 characters:
        format_str = "{: <5}  {: ^10}  {: >15}"
    Make sure the column is wider than the heading text and the widest entry in that column,
        otherwise the columns won't align correctly.
    You can also pad with something other than a space and put characters between the columns, 
        eg, this pads with full stops '.' and separates the columns with the pipe character '|' :
           format_str = "{:.<5} | {:.^10} | {:.>15}"
    """
    #print(row)
    # Convert a tuple to a list, to allow updating of values
    if type(row) == tuple: 
        row = list(row)
    # Loop through each item in the row, changing to "" (empty string) if value is None and converting all other values to string
    #   (Extra info:  enumerate() places a loop counter value in index to allow updating of the correct item in row)
    for index,item in enumerate(row):
        if item is None:      # Removes any None values from the row_list, which would cause the print(*row_list) to fail
            row[index] = ""       
        else:    
            row[index] = str(item)
    # Apply the formatting in format_str to all items in row
    print(format_str.format(*row))



