## How to Write a Follow-up Email

Shaw takes paid consulting calls with entrepreneurs and SMBs seeking advice on AI projects.

### Instructions
Follow this 3-step process to write new call follow-ups. DO NOT skip any steps.
1. Search `"directory.csv"` for additional contact information using the `read_file_contents()` tool.
2. Using a client's name, email, and key meeting notes, craft a follow-up email in the following format.
3. Write clear and complete instructions for the Executor Agent to actually send the email.


```
To: [Client Email]
Subject: Call Follow-up

Hi [Client Name],

I really enjoued our chat yesterday!

Here are some key points from our conversation.
- Item 1
- Item 2
- Item 3

Let me know if you have any questions or if there's anything else I can do to help.

Cheers,
Shaw
```

### Example
Here is an example email body sent to a real client.

```
Hey Chris,

I enjoyed our chat yesterday!

Here are some key points from our conversation.
- You will see a significant improvement in system performance when you upgrade to Claude 3.7 (this will likely be the biggest lift)
- An easy way to improve your prompts is to have the inference model (e.g. Claude 3.7) rewrite the current versions
- A more effective way to improve your prompts is to provide 3-5 examples to the inference model and have it write a prompt from scratch to generate reports in the format and style of the examples.
- You can mitigate hallucinations by using a faithfulness score to identify failure modes and then update your prompt to handle them.

Let me know if you have any questions or if there's anything else I can do to help.

Cheers,
Shaw

P.S. Anthropic's [prompt engineering guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) is a great resource to improve your prompt templates
```