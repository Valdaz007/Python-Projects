import csv

def main():
    posts = []
    posts = read()
    display(posts)
    
def add(thelist, author, title, content, date_posted):
    if check(thelist, author):
         post = {
            'author': author,'title': title,'content': content,'date_posted': date_posted
         }
    if post:
        return post

def read():
    thelist = []
    with open("C:\\00CS_Python\Flask\Project01\data.csv", "r") as database:
        reader = csv.DictReader(database)
        for row in reader:
            thelist.append(row)
    return thelist

def write(thelist):
    with open("data.csv ", "a") as database:
        writer = csv.writer(database)
        for post in thelist: #Get Each Element of the List which are Dictionaries
            writer.writerow((post['author'], post['title'], post['content'], post['date_posted']))

def check(thelist, author_name):
    if len(thelist) > 0:
        for row in thelist:  # Linear Search
            if author_name == row['author']:
                print("Data Already Exist")
                return False
            else:
                return True
    return True

def display(thelist):
    for post in thelist:
        print(f"{post['author']} {post['title']} {post['content']} {post['date_posted']}")

if __name__ == "__main__":
    main()

    