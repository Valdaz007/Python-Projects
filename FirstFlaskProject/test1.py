def main():
    posts = []

    add(posts, 'victor', '1', 'Test', 'TestContent')

    with open("data.txt", "w") as db:
        for post in posts:
            db.writelines(f"{post['a']} {post['b']} {post['c']} {post['d']}")

    print(read())

    
        

def add(p, a, b, c, d):
    p.append({
        'a': a,
        'b': b,
        'c': c,
        'd': d
    })

def read():
    with open("data.txt", "r") as db_out:
        while db_out != "":
            return db_out.readlines()

if __name__ == "__main__":
    main()