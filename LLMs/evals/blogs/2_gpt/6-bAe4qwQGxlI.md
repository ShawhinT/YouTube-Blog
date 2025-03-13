# Building a YouTube Video to Blog Post Converter in Just Four Days
### How I Transformed an Idea into a Working Prototype with Minimal Experience

As a data scientist, I often find myself knee-deep in data processing and machine learning, but when it comes to building consumer software, I felt like a fish out of water. However, with my savings dwindling, I decided to tackle this challenge head-on by creating a web app that converts YouTube videos into blog posts. Surprisingly, I managed to build and deploy the initial prototype in just four days! In this post, I’ll share my journey, the tools I used, and the lessons I learned along the way.

![Building a Web App](https://example.com/image.jpg) *Image by Author*

* * *

### Day 1: Ideation and Design

On the first day, I was starting from scratch. My goal was clear: ship a product in less than a month, but I needed a solid idea. Drawing inspiration from Steven Wolfram's advice to "build a product that solves your own problems," I brainstormed three potential projects:

- A YouTube thumbnail generator
- A YouTube clip finder
- A YouTube video to blog converter

After some quick research, I decided on the last idea, as it seemed the most feasible to implement quickly. With my concept in place, I pivoted to designing the website and user interface. 

Since I lacked coding skills, I began by creating a brand blueprint, which included:

- A color palette (using [Cooler](https://coolors.co))
- Font selections
- A logo designed in [Canva](https://www.canva.com)

By the end of Day 1, I had a clear vision of the app's interface.

* * *

### Day 2: Frontend Development

Day 2 was dedicated to implementing the frontend based on my Canva design. Given my limited experience with web development, I opted to use **Fast HTML**, a Python library that allows developers to build web applications without diving deep into HTML and JavaScript. 

I spent the morning learning Fast HTML through a lecture and its documentation. In the afternoon, I began coding the frontend, using a screenshot of my design as a reference. My workflow involved:

1. Using [Cursor](https://cursor.so) to assist with coding.
2. Occasionally consulting ChatGPT for CSS styling help.

By the end of the day, I had a frontend that closely resembled my initial design.

```python
# Example of a simple Fast HTML structure
from fasthtml import FastHTML

app = FastHTML()

@app.route('/')
def home():
    return "<h1>Welcome to YouTube to Blog Converter</h1>"

app.run()
```

* * *

### Day 3: Backend Implementation

With the frontend ready, Day 3 focused on implementing the backend functionality. I utilized the **YouTube Transcript API** and OpenAI's Python API to generate blog posts from video transcripts. My approach involved:

- Crafting a prompt in ChatGPT to create blog posts based on transcripts.
- Experimenting with various YouTube videos to refine the output.

The beauty of this approach was that I could repurpose existing code from previous projects, which accelerated the development process. 

While I could have added more sophisticated features, such as user-uploaded PDFs or fine-tuning a model on my own content, I chose to keep it simple for the prototype.

* * *

### Day 4: Deployment

The final day was all about deployment. To make the app accessible, I set up **Google OAuth** for user authentication, allowing users to sign in with their Google accounts. This saved me from managing sensitive information like passwords. 

After several attempts, I successfully deployed the app using [Railway](https://railway.app), a platform that simplifies app deployment. I also purchased a custom domain for the app, which added a professional touch.

By the end of Day 4, I had a working prototype that allowed users to create blog posts from YouTube videos in mere minutes. I even monetized the first blog post on Medium, earning $112 within a day!

* * *

### Key Takeaways and Next Steps

Reflecting on this whirlwind experience, here are three essential tips for aspiring developers:

1. **Build with What You Know**: Leverage your existing skills to minimize learning curves. If I had to learn JavaScript or React, I would still be stuck in tutorials.
   
2. **Utilize AI Tools**: Coding assistants like Cursor and ChatGPT can significantly speed up your development process, making you more efficient.

3. **Focus on Ideas and Marketing**: While building is crucial, the idea's viability and effective marketing strategies are equally important.

If you're interested in trying out the latest version of my app, you can find it linked below. Remember, the barriers to building software are lower than ever, and with the right tools, you can turn your ideas into reality faster than you think!

* * *

Building an app in just four days may have seemed daunting, but with the right mindset and tools, it's entirely achievable. What idea will you bring to life next?