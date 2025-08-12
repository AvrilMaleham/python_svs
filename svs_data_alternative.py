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
db_customers = {100:{'details':['Nate Li','024993001','nateli888@limail.co.nz'],
                    'bookings':{date(2025,3,24):[(22,),(),78.00,True],
                            date(2025,6,2):[(23,),(3,),94.45,True]
                            }
                    },
                121:{'details':['Hine Arapata','0226340991','hines@geemail.com'],
                    'bookings':{date(2025,7,7):[(22,24),(2,5),252.59,False],
                            date(2025,10,8):[(23,),(3,),94.95,True],
                            date(2025,11,6):[(),(5,),33.95,False]
                            }
                    },
                129:{'details':['Jane Jones','021123321','janeyj@jonesy.nz'],
                    'bookings':{date(2025,4,22):[(),(3,),28.95,False]}
                    }
                }

col_services = {'ID':int,'Name':str,'Cost':float}
db_services = {22:['Consultation',78.00],
               23:['Grooming',65.50],
               24:['Dental Check',52.84],
               }

col_treatments = {'ID':int,'Name':str,'Cost':float}
db_treatments = {2:['Vaccination',87.80],
                 3:['Shampoo',28.95],
                 5:['Flea treatment',33.95]
                 }

col_invoices = {'Customer':str,'Telephone':str,'Date':datetime.date,'Amount':float}


def unique_id():
    """
    This will return the next available ID as a new integer value
    that is one higher than the current maximum ID number in the list."""
    
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



