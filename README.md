# Overview

Through this project I am trying to learn about cloud databases to further my learning and understanding about different ways to store data in programs.

I integrated a cloud database into a networking project I have done in the past. Once the server is running, the client is then able to connect to the server. While the connection is active the client can tell the server whether they want to start writing a new story or if they want to continue writing one that has been saved to the cloud. The server retrieves and uploads all stories to the cloud and sends that to the client. Once the client has selected an option on what they want to do, they can then repeatedly add words to the story and type 'QUIT' to end the addition of words to the story. Every time the client adds a word to the story it is sent to the server, the server capitalizes the first letter and adds it on the end of the rest of the story. The server then returns the story so far to the client.

I wanted to learn how to integrate a cloud database into software I have written to experiement with different ways of storing data.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of the cloud database.}

[Software Demo Video](https://www.youtube.com/watch?v=wr6nW5AV9rk)

# Cloud Database

Firebase

collection: stories -> (different stories) -> each sotory has a title, and the story itself

# Development Environment

VS Code

Python

Libraries: socket and firebase_admin
# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Fire Base](https://console.firebase.google.com/)
* [Cloud Firestore Tutorial](https://firebase.google.com/docs/firestore)

# Future Work

* Fix bug that names the story QUIT instead of the title you give it
* Add more error handlers