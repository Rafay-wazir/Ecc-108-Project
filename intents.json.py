import json

intents = [
    {
        "tag": "greeting",     # Tags are used to categorize the different types of user inputs or queries. They act as labels for a specific type of conversation or intent.
        "patterns": [          # Patterns represent various ways a user might express the same intent or query.
            "Hi",
            "Hi there",
            "How are you",
            "Hey",
            "Hello"
        ],
        "responses": [         # Responses are the bot's replies or actions corresponding to a specific tag or user input pattern.
            "Hello",
            "Good to see you again",
            "Hi there, how can I help?"
        ],
        "context": [""]        # the "context" field in your JSON structure can be used to maintain context in a conversation
    },
    {
        "tag": "goodbye",
        "patterns": [
            "Bye",
            "See you later",
            "Goodbye",
            "Nice chatting to you, bye"
        ],
        "responses": [
            "See you!",
            "Have a nice day",
            "Bye! Come back again soon."
        ],
        "context": [""]
    },
    {
        "tag": "thanks",
        "patterns": [
            "Thanks",
            "Thank you",
            "That's helpful",
            "Awesome, thanks",
            "Thanks for helping me"
        ],
        "responses": [
            "My pleasure",
            "You're Welcome"
        ],
        "context": [""]
    },
    {
        "tag": "query",
        "patterns": [
            "What are you",
            "Who are you",
            "Tell me about yourself"
        ],
        "responses": [
            "I'm a chatbot designed to assist you with your questions.",
            "I'm here to help you with anything you need!"
        ],
        "context": [""]
    },
    {
        "tag": "jokes",
        "patterns": [
            "Tell me a joke",
            "I need a laugh",
            "Can you make me laugh?"
        ],
        "responses": [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call fake spaghetti? An impasta!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ],
        "context": [""]
    },
    {
        "tag": "random",
        "patterns": [
            "Tell me something random",
            "Give me a random fact",
            "I want to hear something unexpected"
        ],
        "responses": [
            "A group of flamingos is called a flamboyance.",
            "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
            "The shortest war in history was between Zanzibar and England in 1896. Zanzibar surrendered after just 38 minutes."
        ],
        "context": [""]
    },
    {
        "tag": "books",
        "patterns": [
            "Recommend me a book",
            "What book should I read?",
            "Any good books you know?"
        ],
        "responses": [
          "The Alchemist:- By Paulo Coelho - A timeless tale of self-discovery and personal legend, following a young shepherd boy named Santiago on his journey to fulfill his dreams and find his treasure.",
          "Ikigai - The Japanese Secret to a Long and Happy Life By Héctor García and Francesc Miralles, A guide to finding purpose, joy, and fulfillment in life by uncovering one's ikigai, or 'reason for being,' based on Japanese philosophy.",
          "Rich Dad Poor Dad:- By Robert T. Kiyosaki - A personal finance classic that challenges conventional wisdom about money and offers practical insights into building wealth and financial independence, What the Rich Teach Their Kids About Money That the Poor and Middle Class Do Not!.",
          "The Power of Now:- by Eckhart Tolle - A spiritual guide to help you live in the present moment and find inner peace.",
          "The Kite Runner:- by Khaled Hosseini - A gripping tale of friendship, betrayal, and redemption set against the backdrop of Afghanistan.",
          "The Night Circus:- by Erin Morgenstern - A mesmerizing fantasy novel about a magical competition between two young illusionists.",
          "The Shadow of the Wind:- by Carlos Ruiz Zafón - A mysterious and enchanting story set in post-war Barcelona, revolving around a secret library and a cursed book.",
          "Life of Pi:- by Yann Martel - A remarkable tale of survival and faith, following a young boy stranded on a lifeboat with a Bengal tiger.",
          "The Secret Life of Bees:- by Sue Monk Kidd - A heartwarming story of a young girl's journey to uncover the truth about her mother's past, set in the American South in the 1960s",
          "The Time Traveler's Wife:- by Audrey Niffenegger - A unique love story that transcends time and space, exploring themes of fate, destiny, and the power of love.",
          "The Curious Incident of the Dog in the Night-Time:- by Mark Haddon - A captivating novel narrated by a teenage boy with autism, who sets out to solve the mystery of a neighbor's murdered dog.",
          "The Book Thief:- by Markus Zusak - A poignant and unforgettable story set in Nazi Germany, told from the perspective of Death and centered around a young girl's love for books.",
          "Norwegian Wood:- by Haruki Murakami - A melancholic yet beautiful coming-of-age novel set in 1960s Japan, exploring themes of love, loss, and the search for meaning."

      ],
        "context": [""]
    },
    {
        "tag": "restaurant_recommendation",
        "patterns": [
            "Can you recommend a good restaurant?",
            "I'm hungry, any restaurant suggestions?",
            "Where should I eat?",
            "Recommend me a restaurant"
        ],
        "responses": [
            "Sure, what type of cuisine are you in the mood for?",
            "I'd be happy to help! Do you have a preference for a specific type of cuisine?",
            "Of course! Is there a particular type of food you're interested in?"
        ],
        "context": [""]
    },
    {
        "tag": "feedback",
        "patterns": [
            "I have feedback",
            "Feedback",
            "I want to give feedback",
            "Feedback for you"
        ],
        "responses": [
            "Thank you for your feedback! We appreciate your input.",
            "Feedback is valuable to us. Please share your thoughts.",
            "We're always looking for ways to improve. Your feedback helps us do that."
        ],
        "context": [""]
    },
    {
        "tag": "compliment",
        "patterns": [
            "You're doing a great job",
            "I'm impressed",
            "Good job",
            "Well done"
        ],
        "responses": [
            "Thank you! I'm here to assist you.",
            "I'm glad I could help!",
            "Appreciate the compliment! Let me know if you need anything else."
        ],
        "context": [""]
    },
    {
        "tag": "complaint",
        "patterns": [
            "I have a complaint",
            "Complaint",
            "I want to complain",
            "This is unacceptable"
        ],
        "responses": [
            "I'm sorry to hear that. Please tell me more about the issue.",
            "Your feedback is important. Can you please elaborate on the complaint?",
            "I apologize for any inconvenience. Let's address the problem. What happened?"
        ],
        "context": [""]
    },
    {
        "tag": "product_information",
        "patterns": [
            "Tell me about your products",
            "What products do you offer?",
            "Product information",
            "I want to know about your offerings"
        ],
        "responses": [
            "We offer a variety of products. Is there a specific product you're interested in?",
            "Our product range includes various options. What are you looking for?",
            "I can provide information about our products. What type of product are you interested in?"
        ],
        "context": [""]
    },
    {
        "tag": "technical_support",
        "patterns": [
            "I'm having technical issues",
            "Help with technical problem",
            "Technical support needed",
            "My device isn't working"
        ],
        "responses": [
            "I'm sorry to hear that. Let's troubleshoot the issue. What seems to be the problem?",
            "I'll do my best to assist you with the technical issue. Can you provide more details?",
            "Technical problems can be frustrating. What exactly is happening?"
        ],
        "context": [""]
    },
]

# Save the intents dictionary as JSON
file_path = "intents.json"
with open(file_path, "w") as file:  
    json.dump(intents, file, indent=4)