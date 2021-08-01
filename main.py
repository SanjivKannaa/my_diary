import os
import time
import pickle



def start():
    while True:
        dashboard()



def dashboard():
    '''
        shit still need to be done here
    '''
    print('1. today entry\n2. search\n3. exit')
    choice = input('>>')
    if choice == '1':
        entry()
    elif choice == '2':
        search()
    elif choice == '3':
        exit()
    else:
        print('invalid choice.')
        time.sleep(3)
        start()


def get_date():
    date = time.ctime(time.time())[8:10]
    if date[0] == ' ':
        date = '0' + date[1]
    month = time.ctime(time.time())[4:7]
    year = time.ctime(time.time())[-4:]
    if month == 'Jan':
        month = '01'
    elif month == 'Feb':
        month = '02'
    elif month == 'Mar':
        month = '03'
    elif month == 'Apr':
        month = '04'
    elif month == 'May':
        month = '05'
    elif month == 'Jun':
        month = '06'
    elif month == 'Jul':
        month = '07'
    elif month == 'Aug':
        month = '08'
    elif month == 'Sep':
        month = '09'
    elif month == 'Oct':
        month = '10'
    elif month == 'Nov':
        month = '11'
    elif month == 'Dec':
        month = '12'
    else:
        '00'
    return str(date)+' '+str(month)+' '+str(year)


def entry():
    content = list()
    date = get_date()
    while True:
        content.append(input('\n>>'))
        if input('add more lines?[y/n]') == 'n':
            break
    f = open('data.bin', 'rb')
    old = pickle.load(f)
    f.close()
    old[str(date)] = content
    f = open('data.bin', 'wb')
    pickle.dump(old, f)
    f.close()
    print('done')
    time.sleep(3)


def search():
    print('1. search by exact date\n2. search by #label\n3. search by @tag\n4. see all data\n5. return to dashboard\n')
    choice = input('>>')
    if choice == '1':
        search_by_date()
    elif choice == '2':
        search_by_label()
    elif choice == '3':
        search_by_tag()
    elif choice == '4':
        see_all_data()
    elif choice == '5':
        dashboard()
    else:
        print('ínvalid choice')


def search_by_date():
    date = input('enter the date in this format "24 01 2020"')
    f = open('data.bin', 'rb')
    content = pickle.load(f)
    f.close()
    try:
        for i in content[date]:
            print(i, end='\n')
    except:
        print('invalid date')
        dashboard()
    time.sleep(3)

def search_by_label():
    label = '#' + input('enter the label you eant to search : #')
    f = open('data.bin', 'rb')
    content = dict(pickle.load(f))
    f.close()
    for i in content.keys():
        for j in content[i]:
            if label in j:
                print(i)
                for x in content[i]:
                    print('\t' + x)
    input()



def search_by_tag():
    tag = '@' + input('enter the tag : @')
    f = open('data.bin', 'rb')
    content = dict(pickle.load(f))
    f.close()
    for i in content.keys():
        for j in content[i]:
            if tag in j:
                print(i)
                for x in content[i]:
                    print('\t' + x)
    input()


def see_all_data():
    f = open('data.bin', 'rb')
    content = dict(pickle.load(f))
    f.close()
    for i in content.keys():
        print(i)
        for j in content[i]:
            print('\t' + j)



start()