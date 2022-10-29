import socket
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

    # doc_ref = db.collection(u'stories').document(u'firststory')
    # doc_ref.set({
    # u'title': u'helloworld',
    # u'story': u'this is my story'
    # })

    client, address = server.accept()
    print(f'Connection Established - {address[0]}:{address[1]}')
    print()

    new_story = client.recv(1024)
    new_story = new_story.decode('utf-8')
    string = ''
    story = ''
    
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
        completed_story = {'title': title, 
                           'story': story}
        result = db.collection('stories').document(title).get()
        if result.exists:
            print('story already exists')
        db.collection('stories').document(title).set(completed_story) 
        client.close()

    elif new_story == 'N':
        old_story = client.recv(1024)
        old_story = old_story.decode('utf-8')
        result = db.collection('stories').document(old_story).get()
        data = result.to_dict()
        current_story = data['story']
        
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
        completed_story = {'title': data['title'],
                           'story': current_story}
        db.collection('stories').document(old_story).set(completed_story) # story is not being updated properly
        client.close() 