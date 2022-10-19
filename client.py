import socket

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))

    new_story = input('Do you want to start a new story?(Y/N): ')
    server.send(bytes(new_story, 'utf-8'))

    if new_story == 'Y':
        string = ''
        while string != 'QUIT':
            string = input('Enter the next word in the story(enter QUIT to quit the program): ')
            print()
            server.send(bytes(string, 'utf-8'))
            if string != 'QUIT':
                buffer = server.recv(1024)
                buffer = buffer.decode('utf-8')
                print(f'Story: {buffer}')
        title = input('What do you want to name the story: ')
        server.send(bytes(string, 'utf-8'))

    elif new_story == 'N':
        old_story = input('What is the name of the story you want to continue writing: ')
        server.send(bytes(old_story, 'utf-8'))
        current_story = server.recv(1024)
        current_story = current_story.decode('utf-8')
        print(current_story)
        print()
        string = ''
        while string != 'QUIT':
            string = input('Enter the next word in the story(enter QUIT to quit the program): ')
            print()
            server.send(bytes(string, 'utf-8'))
            if string != 'QUIT':
                buffer = server.recv(1024)
                buffer = buffer.decode('utf-8')
                print(f'Story: {buffer}')