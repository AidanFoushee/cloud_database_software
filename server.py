import socket
import json
import firebase_admin
from firebase_admin import firestore, credentials

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(2)

    # Use the application default credentials.
    cred = credentials.Certificate("story-builder-83e85-4390758674a9.json")
    firebase_admin.initialize_app(cred, {'projectId': 'story-builder-83e85',})
    db = firestore.client()

    doc_ref = db.collection(u'stories').document(u'firststory')
    doc_ref.set({
    u'title': u'helloworld',
    u'story': u'this is my story'
    })

    client, address = server.accept()
    print(f'Connection Established - {address[0]}:{address[1]}')
    print()

    new_story = client.recv(1024)
    new_story = new_story.decode('utf-8')
    story = ''
    string = ''
    
    if new_story == 'Y':
        while string != 'QUIT':
            string = client.recv(1024)
            string = string.decode('utf-8')
            if string != 'QUIT':
                string = string.title()
                story = story + ' ' + string
                print(story)
                client.send(bytes(story, 'utf-8'))
        title = client.recv(1024)
        title = title.decode('utf-8')
        # with open ("stories.json", "r") as saved_stories:
        #     stories = json.load(saved_stories)
        with open ("stories.json", "w") as saved_stories:
            completed_story = {title: story}
            json.dump(completed_story, saved_stories)
        client.close()

    elif new_story == 'N':
        old_story = client.recv(1024)
        old_story = old_story.decode('utf-8')
        with open ("stories.json", "r") as old_stories:
            stories = json.load(old_stories)
            current_story = stories[old_story]
            print(current_story)
            print()
            client.send(bytes(current_story, 'utf-8'))
        while string != 'QUIT':
            string = client.recv(1024)
            string = string.decode('utf-8')
            if string != 'QUIT':
                string = string.title()
                current_story = current_story + ' ' + string
                print(current_story)
                client.send(bytes(current_story, 'utf-8'))
        with open ("stories.json", "w") as saved_stories:
            stories[old_story] = current_story
            json.dump(stories, saved_stories)
        client.close()
