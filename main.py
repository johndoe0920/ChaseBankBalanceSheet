import csv, sys

def read_csv(csv_file_loc):
    print("Using csv file located at %s" % csv_file_loc)
    transactions = []
    with open(csv_file_loc) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        firstline = True        
        for row in csv_reader:
            if firstline:
                firstline = False
                continue
            transactions.append(row)
    return transactions

def balance_sheet(transactions, cur_bal):
    print ("Balancing sheet")
    cur_bal = cur_bal.replace(',', '')
    print ("Current Balance = %s" % cur_bal)

    categories = ['Transaction Date', 'Post Date', 'Description', 'Category', 'Type', 'Amount', 'Running Balance']
    with open('balanced_sheet.csv', mode='w') as bal_csv_file:
        bal_csv_writer = csv.writer(bal_csv_file, delimiter=',')
        bal_csv_writer.writerow(categories)
        firstline = True
        for trans in transactions:
            if firstline:
                bal_csv_writer.writerow([trans[0], trans[1], trans[2], trans[3], trans[4], trans[5], str(cur_bal)])
                firstline = False
                continue
            cur_bal = float(cur_bal) + float(trans[5])
            bal_csv_writer.writerow([trans[0], trans[1], trans[2], trans[3], trans[4], trans[5], str.format('{0:.2f}', cur_bal)])

if __name__ == "__main__":
    transactions = []
    transactions = read_csv(sys.argv[1])
    balance_sheet(transactions, sys.argv[2])