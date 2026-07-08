---
title: "Don’t Forget the Fundamentals: How I Leveraged Subgoal Analysis to Overcome Procrastination and Dread"
date: 2024-05-31
postTags: [productivity]
---

As a student, many things are thrust upon me to do. Things on my to-do list include reading textbooks, and research articles, analyzing datasets, and writing up and distilling my research. These things can sometimes feel overwhelming and recently, I felt the full force of this overwhelm.

Let me give you some context. I am writing my master’s thesis at the University of Iceland. In brief, I am analyzing a dataset that has multiple measurement instances including pre-treatment screening, post-treatment assessment, 12-month and 24-month follow-up measures, as well as monthly assessment data between the post-treatment assessment and 24-month follow-up measure.

The topic of the thesis is somewhat irrelevant to the topic of this blog post (and I will elaborate on its topic and the results at a later date when it becomes appropriate to do so), but mainly I am evaluating predictors of treatment dropout, rates of treatment dropout, as well as comparing research participants who were provided with a treatment booster protocol against those who did not receive one.

# I Had a Problem

One of the analyses that is pertinent to my thesis is a so-called _survival analysis_ (i.e., analyzing the expected duration of time until one event occurs, which in my case is treatment dropout). Before commencing on this project, I had never conducted a survival analysis but anecdotally I had heard that it was a fairly complex statistical analysis that presupposed a lot of prior knowledge. Queue **imposter syndrome**![1](#e29c61b1-5d21-416f-b84f-f40666677ed1)

Thoughts like “How am I going to do this?”, “I don’t know how to do this”, “Can I even do this?”, “Oh god, what if I fail to understand this and screw up my thesis”, raced through my mind. To top it all off, I have a self-imposed deadline on my thesis (cf. [Parkinson’s law](https://en.wikipedia.org/wiki/Parkinson%27s_law)). After all, I need to write the thesis to graduate and I need to graduate to get my clinical license.

Taken together, I had the goal of commencing the write-up of my thesis and to do so I needed to familiarize myself with the dataset (which, as I briefly described above, is fairly extensive).

## The Reason for My Problem

Although I have undertaken a number of research projects before, I this particular thesis project felt different. Maybe because it feels like the stakes are high. Maybe because the dataset is large. But most probably because I didn’t know where to start:

1. 1. Should I start with the literature review?
    2. Should I begin with analyzing the data?
    3. Should I read up on the mechanics underpinning the data analysis first?

Clearly, my mind was scattered and in dire need of organization. Not only did I not have my priorities straightened out, I didn’t even know what I should prioritize doing! All I knew was that I had a thesis project that I needed to do.

My thesis at Stockholm University spanned over 12,000 words, so telling myself “Just write the thesis” was not a very directive goal. Regardless, that’s exactly what I tried to tell myself but I was getting nowhere.

I just felt more and more stressed as time passed; I found myself procrastinating by occupying myself with other projects (which admittedly, I don’t regret as they also needed to be done, but that’s neither here nor there). I even felt a sense of dread just thinking about it, accompanied by feelings of guilt, shame, and embarrassment. I felt guilty for not having started, I felt ashamed for not knowing how to analyze the data, and I was embarrassed about not keeping to my self-imposed deadlines[2](#250ed96d-f714-4669-b1aa-c73004a135b8).

# **Finding a New Approach to Overcome My Problem of Procrastination**

Clearly, I needed to think about this differently. I couldn’t “just write the thesis”, as that is a monumental task that entails far too many subsets of tasks that I hadn’t thought through yet. Yet, the thesis needed to be written[3](#605ac4b5-c56d-4b96-8468-11a4f1c763a0), and my previous attempts to tell me to “just do it” were leading to negative unproductive self-thoughts and procrastination. I was feeling too overwhelmed to get any productive work going.

## Overcoming the Overwhelm

As I have already alluded to, the task of writing up my thesis was too big. Just thinking about it induced more [cognitive load](https://en.wikipedia.org/wiki/Cognitive_load) than I could manage. Thus, I figured I’d practice what I preach and actually organize my thoughts by writing them out (see [clip](https://youtube.com/clip/UgkxYpgKtYg_reaX0ShSscXDWU_bXurxCuH4?si=XgYwYuJsAoEHf-kP)). This quickly reminded me of the fact that writing is the equivalent of organizing one’s thoughts (cf. writing is organized thinking), and I realized that I had been going at this thesis project in the wrong way.

Somewhat predictably, since I didn’t have my thoughts organized, I didn’t have a clear target. And since I didn’t have a clear target, I had no idea what I was aiming at. One way to ensure you never achieve your full potential is to fail to set a target and not track what you’re aiming at, and I fell victim to this trap. Writing my thesis felt so important that I failed to consider the fundamentals of learning science and actually reflect on what I was struggling with.

When I finally sat down and reflected on what my actual struggle entailed, I quickly realized that I needed to break the task of writing my thesis down into smaller and more manageable components. Put differently, I needed to generate subgoals for me to tackle.

### Subgoal Analysis

Subgoal analysis describes the process of breaking down complex tasks into smaller, more manageable components or subgoals. Each subgoal represents a step or a partial solution that contributes to the overall goal. Thus, I needed to break down the task of writing down my thesis into smaller and smaller steps and components until I felt like doing the first step was manageable. I needed to feel like the chance of making a mistake at any individual step was very low.

By dividing a complex task (like writing a thesis) into smaller parts, cognitive load is reduced, in turn making it easier to process and understand each step along the way. Moreover, this provides a clear structure and sequence to follow, in turn allowing oneself to focus only on one aspect of the task at a time, facilitating mastery of each subgoal before moving on to the next.

This approach not only helps identify the crucial steps needed to accomplish the final goal (writing my thesis), but it also utilizes the principles of incremental [continuous improvement](https://jamesclear.com/continuous-improvement). This improvement compounds over time and drives engagement through the attainment of subgoals. Consequently, motivation to complete the task and persist is increased.

However, I needed a few iterations before I accurately identified my sticking point. Initially, my subgoal analysis looked like this:

1. 1. Do a literature review
    2. Formulate hypotheses
    3. Analyze the data
    4. Write up the results
    5. Write the discussion

This is not a very directive subgoal analysis and upon further reflection, I realized that I felt completely at ease with all of these steps except for the data analytical component. In other words, my sticking point was the data analysis component.

#### The Data Analysis Subgoals

Armed with this information, I decided to break down the data analysis subgoal into more detailed parts. My aim was to define subgoals that were small enough to make the monstrous data analysis component manageable, while also directing my workflow effectively. Below is a boiled-down snapshot (i.e., with some details omitted to ensure the integrity of the project) of what I ended up with:

1. Familiarize myself with the dataset.
2. Extract the relevant data points for survival analysis in a new data frame.
3. Extract the descriptive statistics variables.
4. Create a codebook for the dataset.
5. Recode variables as needed.
6. Use the write.csv function in R to safe this new dataset.
7. Get a grasp of the way dates are coded in the dataset for the monthly assessment data.
8. Familiarize myself with survival analysis:
    1. Read about it
    2. Take notes on how to set up dataset for survival analysis
    3. Understand the mechanics of survival analysis
9. Look into the logistical regression for predictors of dropout (cf. “t_o find potential predictors of treatment outcomes \[including treatment adherence and drop-out\], logistic regression analysis on background variables will be performed_”).
    1. Outline what predictors make sense to use
    2. Extract the relevant variables
    3. Build a logistical regression model using a robust model (cf. Andy Field) or a Bayesian logistic regression model (cf. Andrew Gelman)

All of a sudden, the data analysis didn’t seem like such a big deal anymore. I can familiarize myself with a dataset… I have done that countless times before. I can also separate relevant datapoints from irrelevant datapoint… I have also done that before. I can code the variables that pertain to the descriptive statistics for the research participants… I have also done that before.

Hopefully, you can see where I am going with this. The task of writing my thesis wasn’t causing me problems because I didn’t know how to write an academic manuscript. My struggles were related to trying to do everything at once and then blaming myself for not being able to do that immediately. I had fallen victim to the trap of not specifying my target and not analyzing what steps were necessary to achieve that target.

# Conclusion

This may be my most personal post to date. I have detailed my struggle with commencing my thesis work and outlined why that was presenting me with feelings of overwhelm and causing me to procrastinate. In short, I had failed to consider the fundamentals; I didn’t specify my target and I didn’t properly align my aim. In other words, I was trying to do too much at the same time and felt everything was equally important, in turn driving up my cognitive load too much for me to get any meaningful work done.

Although my solution of writing down my problem to organize my thoughts and then doing a subgoal analysis of my problem may seem simple, it was enormously effective. I can assure you that had I not taken the time to write out what I was struggling with, it would have taken me far longer to realize that the thesis itself wasn’t the problem but instead insecurity regarding the data analysis. I was undoubtedly willfully blind (to some degree) to this insecurity before writing out my thoughts and pinpointing my sticking point. However, almost immediately upon setting aside time to specify my problem, write it out, and analyze its subcomponents, I felt relieved. Not only was I relieved to realize that what I had construed as a monstrous struggle turned out to be no big deal but also was I relieved to have a plan of action.

At the time of writing this, I have started writing up my thesis, familiarized myself with survival analysis, and am on track to keep my self-imposed deadline for submission. All because I went back to the basics and reflected on my thoughts. Thus, if you are feeling overwhelmed or catch yourself procrastinating more than you usually do, I challenge you to set aside some time to sit down, reflect on why you feel that way, organize your thoughts (by writing them down), and break the procrastinated task down into minuscule subtasks that you feel are so easy that you can start today!

## My Protocol for Overcoming Feeling Overwhelmed 

If you are feeling overwhelmed by a task, try the following protocol:

1\. **Set aside some time** to sit down **and reflect** on why you feel that way

2\. **Organize your thoughts** (by writing them down)

3\. **Break the task down into** minuscule **subtasks** that you feel are easy to do

#### **Footnotes**
