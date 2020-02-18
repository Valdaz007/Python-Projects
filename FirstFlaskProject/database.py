import csv
class Posts:
    NoOfPosts = 0
    posts = []

    def __init__(self):
        self.GetDatabase()

    def GetDatabase(self):
        with open("C:\\00CS_Python\Flask\Project01\data.csv", "r") as database:
            reader = csv.DictReader(database)
            for row in reader:
                Posts.posts.append(row)
                Posts.NoOfPosts += 1
    
    def StoreDatabase(self):
        with open("data.csv ", "a") as database:
            writer = csv.writer(database)
            post = Posts.posts[len(Posts.posts)-1] #Get the last Element of the list
            writer.writerow((post['author'], post['title'], post['content'], post['date_posted']))

    def get_Dict(self, Author, Title, Content, Date):
        if self.check(Content):
            post = {
                'author': Author,
                'title': Title,
                'content': Content,
                'date_posted': Date
            }
            Posts.posts.append(post)
            Posts.NoOfPosts += 1

    def check(self, content):
        if len(Posts.posts) > 0:
            for post in Posts.posts:  # Linear Search
                if content == post['content']:
                    return False
                else:
                    return True
        return True
