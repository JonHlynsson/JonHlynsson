---
title: "When Simplicity Wins: Effective Use of Inferential Statistics"
date: 2024-06-16
postTags: [blog rant]
---

I have been thinking about statistical data analysis a lot lately. There are two types of statistics: Descriptive statistics and inferential statistics.

Like the names allude to, descriptive statistics describe your data while inferential statistics allow you to infer something about your data. 

In a scholarly article, you’d expect to see descriptive statistics when the sample characteristics are delineated. Information such as age and gender distribution fall under this category. Conversely, if you want to evaluate whether there are statistically significant differences between groups on some key variable, then you’d employ some inferential statistical method. I have been thinking about this latter category lately. 

Specifically, I have been pondering **what** method is **appropriate** _when_, _where_, and _why_.

### The Complexity of Inferential Statistics

There appears to be a trend towards using more and more complex inferential statistical methods in recent years. As computing power increases and complex statistical procedures become increasingly more accessible to people, the concomitant increase in the use of novel and complex statistical methods has become evident.

I recently came across a paper that evaluated the factor structure of a common relationship satisfaction instrument (I won’t name them here as it seems inappropriate to single any one paper out given the prevalence of this problem). To derive a factor structure, one must conduct a factor analysis. However, the way one goes about doing that can vary substantially. There are different ways of rotating the factor solution (a factor rotation simplifies the factor structure to facilitate interpretability) and different ways of conceptualizing the factor structure. You can derive a hierarchical factor structure, a bifactor structure, or a simple structure, to name a few. The guiding principle must, however, be theory: If there is a theoretical case to be made for a hierarchical factor structure, then you should undoubtedly derive a hierarchical factor structure. However, you should not derive a hierarchical factor structure just because that produces the best fit for the data. In other words, theory trumps model fit.

In the paper that evaluated the factor structure of the aforementioned relationship satisfaction instrument, the authors concluded that a bifactor exploratory structural equation model yielded the best fit for the data. Now, having read both the paper in question and a fair chunk of other papers purporting to evaluate the factor structure of this same instrument, my curiosity was piqued. This was the first (and only) paper that had resulted in such a strange and unnecessarily complex factor structure for this instrument. This led me to think about why the authors had decided to settle on this factor solution. From their paper, only one plausible answer came to mind: Because it had the best model fit.

This exemplifies the problem with complex statistical procedures. They presuppose a fair bit of a priori knowledge in psychometrics (although the same can be said for all inferential statistical procedures). However, this presupposition is far too often false. Psychometrics and statistical training are not prioritized in all graduate programs which leads to an illusion of knowledge of these potential pitfalls.

### If the Data Doesn’t Fit the Statistical Procedure, Don’t Force It!

Relatedly, one must consider the appropriateness of a given statistical procedure given the data that is available. For instance, if a statistical procedure presupposes that if an event happens then it cannot happen again but your data has events that happen many times, then said procedure is inappropriate for your data set. In other words, it is important to use methods that are appropriate for the data instead of opting for methods that are trendy but inappropriate for the data.

More complex does not necessarily equal better! 

Let’s remember that **Occam’s razor** is equally applicable for guiding **the selection of statistical procedures** as it is for _explaining behavior_.
