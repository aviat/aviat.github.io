---
title: "Serverless security: how do you protect what you aren't able to see?"
description: "Serverless security is a challenge, given the lack of visibility and evolving technology. Learn more about serverless and how to secure it"
---


[![Serverless security](https://web.archive.org/web/20230401045742im_/https://i0.wp.com/blog.sqreen.com/wp-content/uploads/2020/12/Serverless.png?fit=820%2C312&ssl=1)](https://web.archive.org/web/20230401045742/https://i0.wp.com/blog.sqreen.com/wp-content/uploads/2020/12/Serverless.png?fit=2379%2C905&ssl=1)[**](https://web.archive.org/web/20230401045742/https://twitter.com/share?&text=Serverless%20security%3A%20how%20do%20you%20protect%20what%20you%20aren%E2%80%99t%20able%20to%20see%3F&url=https://blog.sqreen.com/serverless-security-apidays/)[**](https://web.archive.org/web/20230401045742/https://www.linkedin.com/shareArticle?mini=true&url=https://blog.sqreen.com/serverless-security-apidays/)[**](https://web.archive.org/web/20230401045742/mailto:/?subject=Serverless%20security%3A%20how%20do%20you%20protect%20what%20you%20aren%E2%80%99t%20able%20to%20see%3F&body=Serverless%20security%3A%20how%20do%20you%20protect%20what%20you%20aren%E2%80%99t%20able%20to%20see%3F%20https://blog.sqreen.com/serverless-security-apidays/)

Serverless security is a fascinating topic. As more organizations move to distributed architectures and new ways of running their services, new security considerations arise. I spoke about this topic at[APIdays Paris 2020](https://web.archive.org/web/20230401045742/https://www.apidays.co/paris/)last week, and today, I wanted to recap some of what I covered.

# What is serverless?
Let’s start with the basics: what exactly is serverless, and what does it change in the ways we create software? One way to understand what serverless is changing is to think about it from an evolutionary perspective, similar to the move from monolithic to microservices.
In a monolithic application, 100% of the code is written by developers. Different business modules and functions are linked together using code.
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEUAAP+KeNJXAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAApJREFUCNdjYAAAAAIAAeIhvDMAAAAASUVORK5CYII=)

In a[microservices architecture](https://web.archive.org/web/20230401045742/https://blog.sqreen.com/apidays-2019-rasp-for-apis-and-microservices/), the glue is still in the developer code, but the media is the network. Hence, a great deal of infrastructure is required to ensure that the different services communicate safely and reliably with one another:
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEUAAP+KeNJXAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAApJREFUCNdjYAAAAAIAAeIhvDMAAAAASUVORK5CYII=)

And then come the serverless architecture. This simple comparison already shows several differences brought on by serverless:

1. The orchestration amongst the function is done with the infrastructure / with ops. Hence, the developers will have to do much more ops than they ever did.
1. The links between services is much simpler than the link between microservices, as the services rely on cloud components that usually have built-in authorization, authentication, and cryptography.
1. The number of serverless items to deal with is**much higher**than the number of microservices for the same business outcome.
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEUAAP+KeNJXAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAApJREFUCNdjYAAAAAIAAeIhvDMAAAAASUVORK5CYII=)

This example of a full serverless architecture is starting to appear in the wild, and we call it “native serverless applications.”
Native serverless applications are not the only serverless deployments; there are also the ad-hoc ones. Ad hoc deployments often arise not because of a thoughtful strategic decision to move to serverless, but rather because serverless functions are easy to deploy, and often much easier than going through the typical processes in place in a company. Sometimes, serverless is also the only way to use a particular cloud service.
Last but not least, defining serverless is tricky as it is moving fast. New actors are announcing serverless functions regularly — see CloudFlare, Netlify, Fastly, and more. Also, serverless is taking place in new parts of the infrastructures, lately on the edge. These changes make it a bit hard to pin down.
As such, best practices are still not perfectly stable and are unlikely to be until the tools become mature enough, and the industry becomes more experienced with them. Despite the in-flux nature of serverless, there’s clear movement and progress being made here, and it’s something to take seriously.

# How does the shift to serverless impact security?
The changes described above have several consequences. One of them is the absence of a mental model regarding serverless architectures. This makes reasoning in terms of serverless pretty hard.
There is also an important lack of tools or products to enforce security pillars in serverless, such as protection or monitoring.
We can describe the state of security in the world of serverless on three different levels:

## What’s solved

1. System updates (well, unless you deploy[full dockers](https://web.archive.org/web/20230401045742/https://aws.amazon.com/blogs/aws/new-for-aws-lambda-container-image-support/)in your serverless)
1. Network level security

## What are the new challenges

1. No way to visualize deployments
1. Best practices still change rapidly
1. Entrypoints vary widely (HTTP? Queue? Stream? Database?)
1. Higher coupling to the cloud provider requires high cloud security

## What’s still a challenge, but times 20

1. Developers do 20⨉ more ops
1. 1 microservice = 20⨉ functions

  1. 20⨉ vulnerable dependencies?
  1. 20⨉ ownership tracking?
  1. 20⨉ threat modeling?
  1. 20⨉ faster new function appearance?
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEUAAP+KeNJXAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAApJREFUCNdjYAAAAAIAAeIhvDMAAAAASUVORK5CYII=)
# How do you protect serverless infrastructure?
While there are lots of changes happening around serverless, there are several established security practices that can move the needle should you implement them.

## Enforce your cloud security posture
Use Infrastructure as Code (IaC: Terraform, Cloud Formation, etc.). This will help to shift your infrastructure left, monitor the changes that happen to it, and compare if the definition is drifting from what’s actually happening in production. Serverless app developers own both the code and a part of the infrastructure, hence IaC will help monitor any changes made to the infrastructure.
Then for each serverless deployment, beware of their permissions, and use the principle of least privilege for your serverless functions. Use a reasonable granularity however; don’t build one different role for each function!
Last, but not least, monitor your costs (and be ready to block abuses). A serverless abuse can cost a lot, and worst case scenario, prevent your application from working if some services stop because of a lack of credits.

## Focus your efforts on application security
The core of the development process doesn’t change for serverless applications. The application is still performing business logic, and interacting with third party components like APIs or databases. Hence, the same vulnerabilities still apply here, which means the[OWASP Top 10](https://web.archive.org/web/20230401045742/https://www.sqreen.com/web-application-security/the-owasp-top-ten)is still very relevant and one to consider as you build your protections.
There is one new challenge that arises here around scalability. Developers will deploy between 5 to 20 functions for every one microservice. Hence without a coherent, unified way to deploy serverless, things will get out of sync and descend into anarchy, without any way to understand the status of your serverless deployments.

## Embrace continuous evolution
Beyond the number of services, another dimension is the speed of evolution. A bug fix, or a simple new feature, can be transformed into a brand new serverless function being pushed to production. Hence, the appearance of serverless is much less predictable, with a much shorter time scale than with other kinds of architectures.
The good news is that several tools will help with the time scale side of things:

- IaC will help proactively detect when a new serverless function is being pushed. Plugged into the CI, it can also ensure that this function complies with the controls in place in your company.
- The cloud is made for rapid deployment. Cloud APIs enable listing all of the serverless functions, and can help detect in a reactive way when something was created.

## Make it easy for developers to make the safest choice
This concept is often referred to as “[the paved road](https://web.archive.org/web/20230401045742/https://blog.sqreen.com/how-to-use-frameworks-to-implement-your-security-paved-road/)” in the world of app sec. The goal is to have a very straightforward process to kick off a new serverless deployment. There are several benefits to taking a paved road approach:

1. Every team or developer will be using the same structure
1. All security best practices can be baked in
1. Integrations to CI, CD, etc. can be already plugged
1. The code repositories best practices can be already enforced (CODEOWNERS file, mandatory pull requests, master locked, etc.)
1. Relevant & safe code examples can be put in — they will drive the developers towards using the libraries recommended by the company (and this can be coupled with CI to validate usage)
1. Secret deployment can be documented to prevent common mistakes such as hardcoding or committing secrets in the repositories.

# How will serverless security evolve?
The definition of serverless, the usages, and the tools are evolving very fast, so it is difficult to predict what tomorrow’s deployment will look like. However, the common, immutable point to any serverless service is the developer’s code. We believe at Sqreen that the right and only place to protect your serverless is inside the code of your applications, to leverage as much insights as possible from the function execution, and to be independent from the infrastructure where it is deployed, no matter whether it is on the edge or on any cloud vendor.
We’re currently working on our serverless support, so please get in touch with us at[hey@sqreen.com](https://web.archive.org/web/20230401045742/mailto:hey@sqreen.com), or on Twitter at[@SqreenIO](https://web.archive.org/web/20230401045742/https://twitter.com/SqreenIO)if you want to check it out!
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEUAAP+KeNJXAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAApJREFUCNdjYAAAAAIAAeIhvDMAAAAASUVORK5CYII=)

[**Share](https://web.archive.org/web/20230401045742/https://www.facebook.com/sharer.php?u=https://blog.sqreen.com/serverless-security-apidays/)[**Tweet](https://web.archive.org/web/20230401045742/https://twitter.com/share?&text=Serverless%20security%3A%20how%20do%20you%20protect%20what%20you%20aren%E2%80%99t%20able%20to%20see%3F&url=https://blog.sqreen.com/serverless-security-apidays/)[**Share](https://web.archive.org/web/20230401045742/https://www.linkedin.com/shareArticle?mini=true&url=https://blog.sqreen.com/serverless-security-apidays/)[**Share](https://web.archive.org/web/20230401045742/mailto:/?subject=Serverless%20security%3A%20how%20do%20you%20protect%20what%20you%20aren%E2%80%99t%20able%20to%20see%3F&body=Serverless%20security%3A%20how%20do%20you%20protect%20what%20you%20aren%E2%80%99t%20able%20to%20see%3F%20https://blog.sqreen.com/serverless-security-apidays/)[![](https://web.archive.org/web/20230401045742im_/https://secure.gravatar.com/avatar/630bcbf98d335080f59e77b73f55c510?s=120&d=mm&r=g)](https://web.archive.org/web/20230401045742/https://blog.sqreen.com/author/user-3/)
##### [Jb](https://web.archive.org/web/20230401045742/https://blog.sqreen.com/author/user-3/)
Jean-Baptiste Aviat spent half a decade hunting vulnerabilities at Apple, helping developers solve them, and developing security software. He is now CTO at Sqreen.

#### Get your bi-weekly security dose
Hand-picked security content for Developers, DevOps and Security. No Spam. Just awesome content.

##### Related Tags

- [APIdays](https://web.archive.org/web/20230401045742/https://blog.sqreen.com/tag/apidays/),
- [serverless](https://web.archive.org/web/20230401045742/https://blog.sqreen.com/tag/serverless/)
**Subscribe**Notify ofnew follow-up commentsnew replies to my comments![guest](https://web.archive.org/web/20230401045742im_/https://secure.gravatar.com/avatar/?s=56&d=mm&r=g)Label{}[+]**Name***Email***Website![guest](https://web.archive.org/web/20230401045742im_/https://secure.gravatar.com/avatar/?s=56&d=mm&r=g)Label{}[+]**Name***Email***Website0Comments******Inline FeedbacksView all commentsLoad More Comments