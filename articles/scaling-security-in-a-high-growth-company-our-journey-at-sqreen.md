---
title: "Scaling security in a high growth company: our journey at Sqreen"
description: "Scaling security as your company grows is a challenge. Learn how Sqreen approaches prioritizing security efforts and our next steps."
published: false
---


[![](https://web.archive.org/web/20230604013008im_/https://i0.wp.com/blog.sqreen.com/wp-content/uploads/2020/12/scale-security.png?fit=820%2C312&ssl=1)](https://web.archive.org/web/20230604013008/https://i0.wp.com/blog.sqreen.com/wp-content/uploads/2020/12/scale-security.png?fit=2379%2C905&ssl=1)[**](https://web.archive.org/web/20230604013008/https://twitter.com/share?&text=Scaling%20security%20in%20a%20high%20growth%20company%3A%20our%20journey%20at%20Sqreen&url=https://blog.sqreen.com/scaling-security-journey/)[**](https://web.archive.org/web/20230604013008/https://www.linkedin.com/shareArticle?mini=true&url=https://blog.sqreen.com/scaling-security-journey/)[**](https://web.archive.org/web/20230604013008/mailto:/?subject=Scaling%20security%20in%20a%20high%20growth%20company%3A%20our%20journey%20at%20Sqreen&body=Scaling%20security%20in%20a%20high%20growth%20company%3A%20our%20journey%20at%20Sqreen%20https://blog.sqreen.com/scaling-security-journey/)

Five years after founding Sqreen, many things have tremendously changed. One of them is our approach to security. It’s often said that[security is a journey](https://web.archive.org/web/20230604013008/https://blog.sqreen.com/security-interview-adam-baldwin-on-iterating-security-at-npm/)without end. That it’s about continuous improvement and iteration as your company and applications change. At Sqreen, we are scaling rapidly, and as a security-minded CTO in a security company, I wanted to share how we’re scaling security during this time of growth.
One of the many examples of how scaling changes security is around hiring. A couple years ago, I was interviewing each and every engineer, assessing their technical skills amongst others, and my go-to question was “do you know XSS?” It’s a great question to understand one’s curiosity, humility, and technical knowledge. Hence I had a great understanding of everyone’s level in terms of security, and my closeness to the development side of the house was enough to oversee the security of everything deployed.
As Sqreen has grown, our processes have changed, and I’m not assessing our engineers’ technical skills myself anymore. As such, I’m not as tuned in to everyone’s security level.
Moving further away from the project’s design also put me in a harder position to challenge the choices we’re making from a security standpoint. This is of course natural and a positive development for a scaling company, but it means we had to start being more intentional with our processes and security culture.
As we grew, we hired several extremely talented security engineers, with the goal of contributing to the product (i.e. building defenses that benefit our customer’s production, rather than contributing to Sqreen’s own security). This was helpful to sprinkle a bit of security culture and mindset amongst all the teams, but not enough. We needed to move forward on the next step of our security journey!

## What’s pushing us to move forward
The question of why we should focus on security may seem like an obvious one to answer, but it’s important to recognize that the different drivers behind it are not all the same. As a growing company, several stimuli push us to act on security:

1. Self consciousness. My co-founder and I are both security geeks, and we have extremely high standards for privacy and security.
1. Company sustainability. We’re a security company. Any breach of security would have 10 times the impact on our customers’ trust than it could have in other companies.
1. Business incentives. As a B2B company, our customers ask us for security certifications and want to do their due diligence to ensure our security standards are up to par.

## How do you get started on scaling security?
For any security leader,[the main challenge](https://web.archive.org/web/20230604013008/https://blog.sqreen.com/getting-security-to-scale-learnings-from-modern-app-sec-teams/)is not about identifying what needs to be done, but rather prioritizing how to do it. As most things take time to implement, not everything can be done (unless a team has infinite resources, which is… rare).
In the security world, the best way to prioritize is to begin with the risks that your business is facing. Spending time on a security measure that improves something no customer cares about is probably useless, or at least a lower priority.
The next axis of prioritization is the actual business constraints:

1. What the customers want. In our case, that’s currently[SOC 2](https://web.archive.org/web/20230604013008/https://blog.sqreen.com/soc-2-compliance-guide-for-startups/).
1. What your resources allow for. The sales and product engineering teams also have business constraints and therefore can’t spend all of their time working on the security roadmap.
Security is critical, but security without a business is nothing.
The compound of these constraints (risk, business requirements, and team capacity) is a good driver to build a security roadmap. The highest risk items that are aligned with business requirements should go first. Of course, the hard part comes with high risk items that are unrelated to the business. They take team capacity to handle, but aren’t moving anything business-related forward in the short term. However, they are a security debt, and get more difficult to change and fix as time goes by. They need to be looked at the same way as you would look at technical debt: something that needs to be improved in order to prevent yourself from reaching a breaking point where you can no longer move forward.

## Sqreen’s risk model
So let’s bring it back to us at Sqreen here. How are we prioritizing our security efforts? Here’s the high level framework we’re using to categorize our main assets:

1. The most valuable asset in the Sqreen risk model is by far our customer’s production, hence the Sqreen agents that are running in our customer’s production environments. The compromising of a Sqreen agent poses similar risks as the compromising of any other dependency in the application. We’re also building our agents under the assumption that the Sqreen backend could be compromised.
1. The next most valuable asset is our customer’s data. Our customers trust us with several kinds of data, from their vulnerabilities to their attack surface, their users, the inventory of their applications, and so on.
1. Third, our company assets. This includes items like our sales pipeline, or the personal information of our employees.
The likelihood of breach for any of those is important to assess. When assessing their risk, we also need to understand their attack surface, and identify the threat level they are each facing.

## The next steps in our security journey
We are performing a continuous investment on all parts of Sqreen to ensure that every user and Sqreener transparently benefits from the best possible level of security. The biggest steps forward that we have taken over the past few months concern the agents:

- We have performed penetration testing focused on the perimeter of the agents
- [We launched a bug bounty on HackerOne](https://web.archive.org/web/20230604013008/https://hackerone.com/sqreen), on the perimeter of the agents only. The perimeter will gradually increase to cover all of Sqreen’s production assets as our capacity to handle those reports scales.
For next steps, Sqreen is committed to achieve a SOC 2 certification by 2021. The perimeter will include our customer production and our customer data. If you’re interested in this project, we’re hiring for this:[check our job offer here](https://web.archive.org/web/20230604013008/https://jobs.lever.co/sqreen-2/2c5a7543-97b3-4078-916c-d26a6c03c132)!

## Sqreen’s philosophy on security: now and the future
The Sqreen culture has a direct impact on how we consider our internal security. Our mission of democratizing security is also a great guideline to not prioritize security to the detriment of usability.
For us at Sqreen, when we take the balance of these constraints and our risk profile, we filter them through the end goal of our security: above all is the protection of our customers, their production services, and their data.
As we consider which security measures to implement, we strive to build simple ones that have a strong impact on the goal we’re aiming to achieve. This requires empathy and understanding our users’ use cases – whether they are customers or employees at Sqreen. Effective security measures are the ones that don’t get in the way of the users.
Now, as I mentioned above, our current focus is around SOC 2, as that fulfills requests from our customers and indicates a level of security preparedness within the company. However, achieving certification isn’t the end of the security journey, but rather one step forward towards the higher goal of protecting our customers.
This can be summed up in three sentences:

- Above all is the protection of our customers: their production, and their data.
- Effective security measures are the ones that don’t get in the way of the users.
- Certification is one step forward towards on our security journey, not the end state.
It’s important to have clear goals on what you want to accomplish in the next step of your security journey, but don’t lose sight of the fact that the journey is always ongoing beyond that. For us at Sqreen, we’ll keep you updated on how our security continues to evolve into the future. Stay tuned!
[**Share](https://web.archive.org/web/20230604013008/https://www.facebook.com/sharer.php?u=https://blog.sqreen.com/scaling-security-journey/)[**Tweet](https://web.archive.org/web/20230604013008/https://twitter.com/share?&text=Scaling%20security%20in%20a%20high%20growth%20company%3A%20our%20journey%20at%20Sqreen&url=https://blog.sqreen.com/scaling-security-journey/)[**Share](https://web.archive.org/web/20230604013008/https://www.linkedin.com/shareArticle?mini=true&url=https://blog.sqreen.com/scaling-security-journey/)[**Share](https://web.archive.org/web/20230604013008/mailto:/?subject=Scaling%20security%20in%20a%20high%20growth%20company%3A%20our%20journey%20at%20Sqreen&body=Scaling%20security%20in%20a%20high%20growth%20company%3A%20our%20journey%20at%20Sqreen%20https://blog.sqreen.com/scaling-security-journey/)[![](https://web.archive.org/web/20230604013008im_/https://secure.gravatar.com/avatar/630bcbf98d335080f59e77b73f55c510?s=120&d=mm&r=g)](https://web.archive.org/web/20230604013008/https://blog.sqreen.com/author/user-3/)
##### [Jb](https://web.archive.org/web/20230604013008/https://blog.sqreen.com/author/user-3/)
Jean-Baptiste Aviat spent half a decade hunting vulnerabilities at Apple, helping developers solve them, and developing security software. He is now CTO at Sqreen.

#### Get your bi-weekly security dose
Hand-picked security content for Developers, DevOps and Security. No Spam. Just awesome content.

##### Related Tags

- [security culture](https://web.archive.org/web/20230604013008/https://blog.sqreen.com/tag/security-culture/),
- [soc 2](https://web.archive.org/web/20230604013008/https://blog.sqreen.com/tag/soc-2/),
- [Sqreen](https://web.archive.org/web/20230604013008/https://blog.sqreen.com/tag/sqreen/)
**Subscribe**Notify ofnew follow-up commentsnew replies to my comments![guest](https://web.archive.org/web/20230604013008im_/https://secure.gravatar.com/avatar/?s=56&d=mm&r=g)Label{}[+]**Name***Email***Website![guest](https://web.archive.org/web/20230604013008im_/https://secure.gravatar.com/avatar/?s=56&d=mm&r=g)Label{}[+]**Name***Email***Website0Comments******Inline FeedbacksView all commentsLoad More Comments
