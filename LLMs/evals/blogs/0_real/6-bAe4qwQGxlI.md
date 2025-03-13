# I Built an AI App in 4 Days — Here’s How I Did It.
#### (as a data scientist with no web dev experience)

Technology makes the world move faster. We are seeing this (yet again) today
with AI. Using tools like Cursor, **developers can build 5–10X faster than
before**. I personally experienced this recently when building my first-ever
web application. In this post, I’ll walk through this experience and the tools
to deploy this app in just 4 days.

![](https://cdn-images-1.medium.com/max/800/1*AQxpS8eSQzM5S0swo0i-aw.png)Image from Canva.

* * *

Although most data scientists use Python to process data and train models,
**creating consumer software is a different ballgame**. This is a problem for
me because, as a solo entrepreneur, I don’t have a team (or capital) to
compensate for my inability.

With my savings on track to hit $0 this quarter, I was more motivated than
ever to learn this skill set. To do this, I set the goal of launching 1
product every month this quarter.

The first such product is a tool to convert YouTube videos into blog posts
(called y2b). **I launched the initial prototype for this app in 4 days** ,
and here, I will share exactly how I did it.

### **Day 1: Idea & Design**

My **guiding principle for picking a product idea** came from advice I got
from [Stephen Wolfram](https://x.com/ShawhinT/status/1810673990823719049),
which was basically to “**solve your own problems**.” This led me to 3 product
ideas: a YouTube Thumbnail generator, a YouTube clip finder, and a YouTube
video-to-blog converter.

After some research and seeing an Upwork job post paying a few hundred dollars
for blog writing based on YouTube videos, I decided to go with the latter.

My first step was to design the website and user interface (UI). Since I had
no web development experience, **I started with the design** **rather than
coding**.

![](https://cdn-images-1.medium.com/max/800/1*skWWcuE5P49_YBZpeBwK8Q.png)Brand blueprint for y2b. Image by author.

For that, I created a brand blueprint, which included choosing a color palette
and fonts and designing a logo. I used [**Coolers**](https://coolors.co/) for
color selection and [**Canva**](https://www.canva.com/) for everything else.

This made it easy to design a simple web UI in Canva. By the end of the day,
my design looked like this.

![](https://cdn-images-1.medium.com/max/800/1*NEcbMnP_sJqokzXiPVr0DA.png)Initial UI design.
Image by author.

### **Day 2: Frontend**

With my design in hand, it was time to implement the front end. Since I’m most
comfortable with Python, I opted for a new library called
[**FastHTML**](https://fastht.ml/), which allows developers to **build modern
web apps using (only) Python**.

I spent the morning learning FastHTML by watching a
[tutorial](https://youtu.be/ptRaku0zyeA?si=UgaVg0RpkF5rhq7b) from its
developers and reading through their [documentation](https://docs.fastht.ml/).
In the afternoon, I started implementing my front-end design from Canva.

My first step was to paste a screenshot into Cursor’s AI chat and ask it to
replicate the design in FastHTML. Although it wasn’t perfect, it was **easier
to start by editing this code than coding something from scratch**.

This was my first project using [**Cursor**](https://www.cursor.com/), and I
was sold on it. For things that Cursor seemed to get confused about, I’d go to
ChatGPT. This combination worked well, and by the end of the day, I had a
front end that mirrored my initial design (as shown below).

![](https://cdn-images-1.medium.com/max/800/1*e_1OUiJRAB8gEDKOF-5XIA.png)Screenshot of front
end at the end of Day 1. Image by author.

### **Day 3: Backend**

By Day 3, I had coded my website, but it didn’t do anything. The next step was
to implement the backend.

I needed to develop a process for generating blog posts from YouTube video
transcripts. **Using ChatGPT, I crafted a prompt to generate blogs** and
tinkered with it until I was satisfied.

Then, I moved the process from ChatGPT to Python. The two main libraries I
used for this were the [**YouTube Transcript API**](https://pypi.org/project/youtube-transcript-api/) and [**OpenAI’s Python API**](https://pypi.org/project/openai/). Since I had previously used
these libraries, I repurposed existing code to speed up development. You can
find such examples on my [GitHub repository,](https://github.com/ShawhinT/YouTube-Blog) e.g., [transcript extraction](https://github.com/ShawhinT/YouTube-Blog/blob/main/full-stack-data-science/data-engineering/2_get-transcripts.ipynb) and [OpenAI automation](https://github.com/ShawhinT/YouTube-Blog/blob/main/LLMs/ai-assistant-openai/assistants-api.ipynb).

By the end of day three, I had a functioning website running locally on my
machine!

### **Day 4: Deployment**

The final day was focused on deploying my app. I set up [**Google OAuth**](https://developers.google.com/identity/protocols/oauth2) to **manage
user sign-ins without handling sensitive information** like passwords and
**ensure users are human**. While this may sound straightforward, it took most
of the morning to get it working 😅

Next, I purchased a custom domain for $70 through
[Squarespace](https://domains.squarespace.com/) and deployed my app using
[**Railway**](https://railway.app/). I chose Railway because there was an
[example code](https://docs.fastht.ml/tutorials/by_example.html#deploying-your-app) on FastHTML’s documentation for doing this.

To test the app, I used it to create a blog post based on a
[podcast](https://youtu.be/VKLLyv9cJSQ?si=zFLnJoTBOvKuic5D) I hosted last
year. While it would typically take me 5–6 hours to write an article like this
from scratch, **using this tool took me 1 hour**. I posted the resulting [blog on Medium](https://medium.com/the-data-entrepreneurs/how-to-freelance-as-a-data-scientist-ca9182999595), and (so far) it’s made me $41.52!

![](https://cdn-images-1.medium.com/max/800/1*MVmbzj7pDuN0drLUUihR2A.png)Screenshot of blog
statistics. Image by author.

### **Limitations**

While it took me just four days to push this app to production (i.e., working
and available on the internet), it was still just a prototype. Here were some
of its **key limitations**.

  1. OAuth Users had to be manually set in the Google Cloud Console
  2. The app had no database, so users could use it without limit
  3. No stripe integration, thus no way to make money from it

It took me another **8 days to make an MVP version** for which…

  * Any Google user could use
  * Usage metrics were stored in a SQLite database
  * Stripe integration was set up
  * The landing page featured a demo, FAQ, and pricing.

You can **try out the latest version for free** : <https://y2b.io/>

### **Conclusion**

While data scientists don’t typically build complete apps from scratch,
today’s technological landscape makes this **more accessible than ever**.
Thanks to tools like FastHTML, Cursor, and Railway, I could quickly build and
deploy my 1st web app without any web dev experience.

For those considering something similar, I’d encourage you to **dive right in
and build a project**. This, in my opinion, is the best way to learn AI and
software development. If you have any questions about my process or the tools
I used, please let me know in the comments :)