---
title: "How to use frameworks to implement your Security Paved Road"
description: "A practical guide on implementing security frameworks effectively"
---

[![](https://web.archive.org/web/20230604000803im_/https://i0.wp.com/blog.sqreen.com/wp-content/uploads/2020/12/Frameworks-for-your-security-paved-road-1.png?fit=820%2C312&ssl=1)](https://web.archive.org/web/20230604000803/https://i0.wp.com/blog.sqreen.com/wp-content/uploads/2020/12/Frameworks-for-your-security-paved-road-1.png?fit=2379%2C905&ssl=1)[**](https://web.archive.org/web/20230604000803/https://twitter.com/share?&text=How%20to%20use%20frameworks%20to%20implement%20your%20Security%20Paved%20Road&url=https://blog.sqreen.com/how-to-use-frameworks-to-implement-your-security-paved-road/)[**](https://web.archive.org/web/20230604000803/https://www.linkedin.com/shareArticle?mini=true&url=https://blog.sqreen.com/how-to-use-frameworks-to-implement-your-security-paved-road/)[**](https://web.archive.org/web/20230604000803/mailto:/?subject=How%20to%20use%20frameworks%20to%20implement%20your%20Security%20Paved%20Road&body=How%20to%20use%20frameworks%20to%20implement%20your%20Security%20Paved%20Road%20https://blog.sqreen.com/how-to-use-frameworks-to-implement-your-security-paved-road/)

I recently sat down with Sr. Research Lead at Synopsys and framework specialist,[Ksenia Peguero](https://web.archive.org/web/20230604000803/https://twitter.com/KseniaDmitrieva), on Episode 2 of the AppSec Builders Podcast. In the episode,[“Framework Security with Ksenia Peguero: Paved Road Foundation”](https://web.archive.org/web/20230604000803/https://www.appsecbuilders.com/episode/framework-security-with-ksenia-peguero-the-paved-road-foundation), we discussed how to upgrade your security through your frameworks using the Paved Road foundation. In this post, I wanted to share some learnings from that discussion.

## The Security Paved Road
Legacy security approaches were built as gatekeepers. Today, the challenge that any security team faces is to enable developers to ship things as quickly and efficiently as possible, while maintaining an appropriate level of security. One of the ways to enable this is through building tools and processes to ensure that developers can build secure things by default. Of course, those tools and processes need to be super close to the developer’s workflow in order to be adopted. This is called the Security Paved Road.
An ideal Paved Road would allow engineers to be fully autonomous in deployment with little to no bottlenecks from security teams.
The Security Paved Road was originally[coined by Netflix](https://web.archive.org/web/20230604000803/https://medium.com/@NetflixTechBlog/scaling-appsec-at-netflix-6a13d7ab6043)Security and Engineering teams to drive adoption of their default security controls and enable developers to release quality software at a high velocity.

## Using frameworks to implement your Security Paved Road
The framework level is an ideal place to implement plenty of the Security Paved Road best practices. The security team can, for instance, ensure that the examples to kick off new API endpoints are aligned to security standards, or that the way that new services are created uses the right framework template.
For most companies using a distributed architecture, where new services are regularly created, strong security foundations can be achieved by using a template. Teams can clone this template each time they prepare a new service (whether it’s a monolith, a microservice, a serverless function, etc.) to reduce risk without disrupting the developer’s workflow.
While each framework is different, there are several common dimensions security teams can influence to help developers get the most out of them.

## Framework security dimensions

### Framework components
Some frameworks are very opinionated (e.g. Ruby on Rails, Django, Sails), while others offer a wider degree of flexibility to the developers (e.g. Express or Flask). The security team has to recommend extensive best practices to security owners that align with the framework in question (e.g. how to access data stores, how to validate input, or how to perform requests to external services).

### Framework configuration
Most frameworks have extensive security options. Some of them have secure defaults, while others don’t. Some depend on your architecture. The security team should harden the framework configuration by enforcing the defaults to their secure mode, e.g. default CSRF protection, or prevent user controlled serialized sessions) regardless of which framework is used.
This is also the right time to thoroughly read the security elements of the framework’s documentation.

### Authentication and authorization
The security team should also implement best practices around authentication and authorization. At a minimum, the team should define a standard library for authentication, such as Devise or Passeport, and for authorization, such as[CanCanCan](https://web.archive.org/web/20230604000803/https://github.com/CanCanCommunity/cancancan).

### The framework as a place to enforce company standards
Using a framework foundation has many benefits, that go way beyond security. Having coherent deployments across services, a common place where ops and other teams can improve and populate with best practices over time is extremely valuable. For instanc,e a good practice to identify repository owners is to use a CODEOWNERS file ([Github](https://web.archive.org/web/20230604000803/https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/about-code-owners),[Gitlab](https://web.archive.org/web/20230604000803/https://docs.gitlab.com/ee/user/project/code_owners.html)). This will help Ops teams find out who they should call when a service is failing. This can be enforced in the CI. Such mechanisms make the Paved Road a benefit for the entire company. Examples could be using the right logging framework, the right audit log, etc.

### CI around the framework
On top of building secure defaults, the security team can leverage the CI to ensure that secure defaults don’t drift away from the initial configuration, both at the code and configuration levels. The CI can not only spot security issues but also help enforce coding best practices, such as warning a developer when they are using a known dangerous method (e.g. unescaped templates, raw database queries, calls to external services without using an SSRF safe library, etc.). It can also check that known best practices are enforced, such as ensuring that a validation library is called in any API endpoint, or links in static HTML use the noopener attribute.
Security-specific static analysis tools such as Semgrep have been built with such use cases in mind.

### Framework security history
Some frameworks have a lengthy security history and promptly react to vulnerability reports. Others have such a small attack surface that they rarely suffer from vulnerabilities. Security teams should monitor the right channels to be informed early of framework vulnerabilities, so they can patch anything that arises quickly.

## Conclusion
The security coverage and functions of a framework can be very deep or very light from one framework to another. As is often the case with security, extensiveness comes at the cost of complexity. Complexity increases the attack surface, and paradoxically, brings security challenges. The paradox fades when considering that the challenges of integrating external libraries or solutions are much harder to do than enabling things that are integrated within the framework – while adding a similar attack surface.
Choosing the right framework, or building the right secure defaults for your existing frameworks, is often the most impactful way to guide your company developments in a secure direction.
Want more? Listen to the full AppSec Builders episode of[“Framework Security with Ksenia Peguero: Paved Road Foundation”](https://web.archive.org/web/20230604000803/https://www.appsecbuilders.com/episode/framework-security-with-ksenia-peguero-the-paved-road-foundation)on any streaming platform.
[**Share](https://web.archive.org/web/20230604000803/https://www.facebook.com/sharer.php?u=https://blog.sqreen.com/how-to-use-frameworks-to-implement-your-security-paved-road/)[**Tweet](https://web.archive.org/web/20230604000803/https://twitter.com/share?&text=How%20to%20use%20frameworks%20to%20implement%20your%20Security%20Paved%20Road&url=https://blog.sqreen.com/how-to-use-frameworks-to-implement-your-security-paved-road/)[**Share](https://web.archive.org/web/20230604000803/https://www.linkedin.com/shareArticle?mini=true&url=https://blog.sqreen.com/how-to-use-frameworks-to-implement-your-security-paved-road/)[**Share](https://web.archive.org/web/20230604000803/mailto:/?subject=How%20to%20use%20frameworks%20to%20implement%20your%20Security%20Paved%20Road&body=How%20to%20use%20frameworks%20to%20implement%20your%20Security%20Paved%20Road%20https://blog.sqreen.com/how-to-use-frameworks-to-implement-your-security-paved-road/)[![](https://web.archive.org/web/20230604000803im_/https://secure.gravatar.com/avatar/630bcbf98d335080f59e77b73f55c510?s=120&d=mm&r=g)](https://web.archive.org/web/20230604000803/https://blog.sqreen.com/author/user-3/)
##### [Jb](https://web.archive.org/web/20230604000803/https://blog.sqreen.com/author/user-3/)
Jean-Baptiste Aviat spent half a decade hunting vulnerabilities at Apple, helping developers solve them, and developing security software. He is now CTO at Sqreen.

#### Get your bi-weekly security dose
Hand-picked security content for Developers, DevOps and Security. No Spam. Just awesome content.
**Subscribe**Notify ofnew follow-up commentsnew replies to my comments![guest](https://web.archive.org/web/20230604000803im_/https://secure.gravatar.com/avatar/?s=56&d=mm&r=g)Label{}[+]**Name***Email***Website![guest](https://web.archive.org/web/20230604000803im_/https://secure.gravatar.com/avatar/?s=56&d=mm&r=g)Label{}[+]**Name***Email***Website0Comments******Inline FeedbacksView all commentsLoad More Comments