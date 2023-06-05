# Word Embedding Analogies Project

Hello and welcome to our exciting Word Embedding Analogies Project! We've built an interactive web application to explore and learn about the fascinating world of Natural Language Processing (NLP). It's kind of like having a conversation with your computer, but instead of just typing out responses, we're actually manipulating language in ways that resemble how humans understand and use words.

## 1. What's the Project About?

Let's break down the science-y stuff. In NLP, there's a cool technique called Word Embeddings. Basically, it's a way of representing words as lists of numbers (aka vectors) that encapsulate the meanings and relationships between words. It's kind of like mapping a city, but instead of streets and buildings, we're mapping words and their meanings!

This project uses these word vectors to solve word analogies. Remember those questions from English class? "Man is to King as Woman is to...?" Well, our application can answer those, and not by memorizing a dictionary, but by understanding the relationships between the words, just like a human would!

## 2. How Does it Work?

Our application is split into two parts, the front-end (what you interact with) and the back-end (the behind-the-scenes magic).

When you input three words for the analogy into the front-end, they are sent as a request to the back-end, kind of like sending a letter. The back-end receives the "letter", solves the analogy, and sends back a "reply" with the answer, which is then displayed on the front-end.

In addition, all your analogy queries are logged and saved into a database. You can request to see all your past queries and their answers at any time, kind of like viewing your conversation history!

## 3. The Back-End

This is where the heavy lifting happens! The back-end takes your inputs, processes them using pre-trained word embeddings, and computes the analogies. Think of it as a sort of "word factory" that takes in raw words and churns out polished analogies!

We've used Python, Flask (a lightweight web framework), and Annoy (a fast library to search for nearest neighbors) to handle all these tasks. Don't worry if these sound intimidating, they're just our magical tools to make this all possible!

## 4. The Front-End

This is the part you interact with - the website itself! It's been designed to be clean, user-friendly, and fun to use. You input your words, click a button, and voila, the answers appear!

We've crafted this using HTML, CSS, and JavaScript. These are like the skeleton, skin, and muscles of our website body, respectively.

## 5. Getting Started

Ready to dive in? Clone this project, follow the setup instructions in our handy installation guide (`server/README/md`), and get exploring! This is your journey into the exciting landscape of NLP and web development. Remember, the purpose of this project is to learn, explore, and most importantly, have fun!

And that's it! So what are you waiting for? Dive in and start playing with words in a way you never have before!

Happy exploring! 🚀 🌟 🎉
