---
title: "Runtime application self-protection (RASP) for APIs and microservices"
description: "As teams migrate to microservices, securing them becomes an important question. Microservices' security needs demand new approaches like RASP"
published: false
---


[![](https://web.archive.org/web/20230526173527im_/https://i0.wp.com/blog.sqreen.com/wp-content/uploads/2019/12/PI_Days_2019__RASP_for_microservices.png?fit=820%2C312&ssl=1)](https://web.archive.org/web/20230526173527/https://i0.wp.com/blog.sqreen.com/wp-content/uploads/2019/12/PI_Days_2019__RASP_for_microservices.png?fit=2379%2C905&ssl=1)[**](https://web.archive.org/web/20230526173527/https://twitter.com/share?&text=APIdays%3A%20RASP%20for%20APIs%20and%20microservices&url=https://blog.sqreen.com/apidays-2019-rasp-for-apis-and-microservices/)[**](https://web.archive.org/web/20230526173527/https://www.linkedin.com/shareArticle?mini=true&url=https://blog.sqreen.com/apidays-2019-rasp-for-apis-and-microservices/)[**](https://web.archive.org/web/20230526173527/mailto:/?subject=APIdays%3A%20RASP%20for%20APIs%20and%20microservices&body=APIdays%3A%20RASP%20for%20APIs%20and%20microservices%20https://blog.sqreen.com/apidays-2019-rasp-for-apis-and-microservices/)

This week, I had the opportunity to speak at APIdays in Paris. As is often the case, APIdays was frequented by a super interesting mix of technologists, looking for the latest product evolutions, but also by strategists, looking for the newest trends and ways to ensure that they are building for their company’s future.
The trendy subjects this time were around microservices and service mesh, API management through API gateways, and how to transition an organization towards APIs and microservices.
The talk I gave, RASP for APIs and microservices, was exactly in that subject area. Thinking about the ways[runtime application self-protection](https://web.archive.org/web/20230526173527/https://www.sqreen.com/web-application-security/what-is-rasp)(RASP) and[Sqreen](https://web.archive.org/web/20230526173527/https://www.sqreen.com/runtime-application-self-protection)can help secure microservices architecture is a very exciting subject and I wanted to share our insights.

## The rise of microservices
Today, many organizations are moving to microservices. This shift is usually made from a starting point of monoliths. As the team working on a monolith grows, it gets harder and harder to be efficient: sharing a database, the same codebase, makes it super hard to not step on another team’s feet while working on a new feature.
One solution to this problem is microservices. Moving from a monolith to a microservice is usually made by breaking apart business functions that existed in the monolith. Generally speaking, those new bricks should be:

- Decoupled
- API addressed
The goal for microservices is that each service is independent from the others, and can be queried without the client knowing what is underneath implementation. This also allows huge flexibility, as the team responsible for a given microservice can switch their database or specialize the microservice implementation into a new programming language without having to make changes across the entire organization, as the other teams only rely on the API to query that service.
Also, adding a new feature could be done by adding a new microservice. The risks are limited and the other teams can easily query it.  

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEUAAP+KeNJXAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAApJREFUCNdjYAAAAAIAAeIhvDMAAAAASUVORK5CYII=)![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEUAAP+KeNJXAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAApJREFUCNdjYAAAAAIAAeIhvDMAAAAASUVORK5CYII=)

A good way to express this change is the following:

- Monoliths have objects, interfaces, and function calls.
- Microservices have services, interfaces, and network calls.

## How do you protect microservices?
So as teams consider[moving to microservices from a monolith](https://web.archive.org/web/20230526173527/https://blog.sqreen.com/top-10-security-traps-to-avoid-when-migrating-from-a-monolith-to-microservices/), several questions arise. One big area to consider is around security. Plenty of ways exist for securing monoliths. The older and best known is the Web Application Firewall (WAF), a tool that will be placed before the monolith and act as a reverse proxy, analyzing the raw HTTP requests going through and comparing them with patterns in order to detect attacks.
WAFs are common for monoliths, but how do they work for microservices? Relying on a WAF for a microservices infrastructure would look like this:
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEUAAP+KeNJXAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAApJREFUCNdjYAAAAAIAAeIhvDMAAAAASUVORK5CYII=)

Right away we can see that this isn’t optimal. The business context is much harder to understand in this layout, and given the nested view, there is no way attacks targeting internal services can be detected.
Using an in-app security approach such as RASP can directly address these new limitations. With such an approach, instead of having a security solution sitting on the network’s edge, the security is sitting inside the application. Sitting inside the app has several advantages, especially when applied at the scale of microservices:

- Automatic configuration. In-app security can automatically detect the framework, language, databases, 3rd parties, etc.
- Detection of vulnerabilities without false positives and with actionable reports. Given the runtime context knowledge that comes from being inside the application, in-app security like RASP can eliminate false positives by only blocking requests that actually would trigger a vulnerability. They also offer vulnerability identification down to the line of code, providing developer-oriented information such as the stack trace.
Here’s what security looks like if you move from a WAF to a RASP for microservices:
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEUAAP+KeNJXAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAApJREFUCNdjYAAAAAIAAeIhvDMAAAAASUVORK5CYII=)

Being inside the service allows for a much better understanding of what’s happening inside each of the individual microservices. But it also allows you to go much further: it can give insights about the whole network.
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEUAAP+KeNJXAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAApJREFUCNdjYAAAAAIAAeIhvDMAAAAASUVORK5CYII=)

In order to understand the impact this paradigm has on microservices security, let’s deep dive on the security challenges of microservices.

## Protecting individual services
Each microservice has the same security challenges as a monolith:

- OWASP top 10 vulnerabilities (injections, out of date 3rd parties, etc.)
- Business logic issues
And some new ones…

- No input should be trusted. Microservices can give a false sense of security as services clients or consumers use are internal (i.e. only used by other teams).
- Don’t trust the network. Each request received by a service need to be authenticated and authorized. This paradigm is called zero trust. Also, service communications need to be confidential (using e.g. TLS). This is sometimes referred to as Application Layer Transport Security.

---

**Why you shouldn’t trust the network for microservices**
One way to picture microservices is as parts of a monolith, distributed across the network and communicating through APIs rather than function calls. Let’s assume that anyone in the world could perform function calls to any part of your monolith: would you be confident that you don’t have a vulnerability? Probably not! So, would you be confident if anyone was able to query any of your microservices? Despite the coding paradigm being quite different, you probably wouldn’t be confident… So how can we assume that anyone could query any of your microservices? Several vulnerabilities, once exploited by attackers, can provide the ability to query internal services. For instance:

- Server Side Request Forgery (SSRF): the vulnerable service can be tricked into querying arbitrary IP addresses.
- SQL injection: many SQL servers allow you to perform network queries ([see an MSSQL example here](https://web.archive.org/web/20230526173527/https://gist.github.com/jarrettmeyer/5990daf0db3b1f4fd759df6ed4099685)).
- Remote Code Execution (RCE): any vulnerability for which the outcome is an RCE can allow attackers to build arbitrary network queries.

---

Another unique security concern for microservices is asynchronous workers. They are attacked with different exploitation mechanisms, but are definitely valid targets. They are often the vector of SSRF attacks, that can be used to turn an asynchronous worker into an attacker-controlled HTTP client, able to query any microservice of the infrastructure.
Last but not least, observability is needed at the service level:

- The code: vulnerable packages, new routes, vulnerable functions, and so on
- The business logic: Who are my clients / my servers? Am I performing business-sensitive operations? Is there PII (Personally Identifiable Information) flowing in my code?
- The users: account theft attacks, user performing attacks, etc.

## Protect the whole infrastructure
The first challenge at the scale of microservices is to understand what’s running in your infrastructure. What services have been pushed? Are they up to date? Are they exposed to the internet? What framework or ORM are they using?
Security teams need up-to-date information and prompt updates as soon as new services satisfy the previous queries.
A service inventory like what follows can be used to gather all the data points from the deployed services:
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEUAAP+KeNJXAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAApJREFUCNdjYAAAAAIAAeIhvDMAAAAASUVORK5CYII=)

A paradigm that need to be taken for granted is that the network should be considered insecure.
The direct consequence is that all the service-to-service communications need to be ciphered, but also authenticated, and the authorization of the actor performing the request should be validated. That’s the zero trust paradigm.
Last but not least, attacks detected in nested services need to be attributed to an external actor. If we only look at the one stage removed attacker, we’ll often end up with another microservice. That information isn’t super useful on its own; what we want is the external attacker IP. Service A attacking Service B is not relevant: we need to be able to find what the external actor IP is that managed to actually perform an attack, but not the IP of the service A.

### How do you respond to attacks?
There are several potential ways to respond to attacks against your microservices.

#### Block the actor at the edge
This paradigm is the most radical. Blocked actors can be blocked either in the API gateway or further down in the CDN. They won’t hit any service but it also prevents 100% access to the service, which can be unwanted in the case of shared IP addresses (e.g. a corporate HTTP proxy).
If the API gateway is authentication aware, it can also be used to block users (rather than just IPs).
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEUAAP+KeNJXAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAApJREFUCNdjYAAAAAIAAeIhvDMAAAAASUVORK5CYII=)
#### Block only sensitive services
This more elaborated response allows you to block only a subset of services. For instance, you could block services that aren’t read-only, or services that manipulate sensitive data only. This makes potential blocking errors less impactful since they’re narrower.
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEUAAP+KeNJXAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAApJREFUCNdjYAAAAAIAAeIhvDMAAAAASUVORK5CYII=)
#### Decrease the rights of a given actor
A given actor could be given a specific authorization as long as they are considered suspicious. This is the best pattern for preventing sensitive functions from getting called by a given actor while maintaining a high availability to the services.
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEUAAP+KeNJXAAAAAXRSTlMAQObYZgAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAApJREFUCNdjYAAAAAIAAeIhvDMAAAAASUVORK5CYII=)
## Securing microservices with a RASP
Microservices are rising in popularity for good reason. They are a huge help for an organization’s velocity given their technical and organizational benefits. Implementing microservices comes with new considerations however. One key consideration is that microservices represent a brand new challenge from a security point of view and have an important cost.
As we move to the future of architecture, we must also move to the future of security. Traditional security approaches for monoliths like WAFs run into limitations with a microservices architecture. The answer is to move to an in-app security approach. A RASP is an ideal in-app security option that can provide insights at the service level as well as at the infrastructure level. This keeps your microservices safe while also surfacing new levels of insights into your application components and security incidents so that you can remediate and improve your security in an agile manner.
As our architectures evolve, everything must evolve along with it, security included. RASP represents the corresponding evolutionary step in security to match the move from monoliths to microservices. You can get all the advantages of microservices without opening yourself up to a poor security posture.
[**Share](https://web.archive.org/web/20230526173527/https://www.facebook.com/sharer.php?u=https://blog.sqreen.com/apidays-2019-rasp-for-apis-and-microservices/)[**Tweet](https://web.archive.org/web/20230526173527/https://twitter.com/share?&text=APIdays%3A%20RASP%20for%20APIs%20and%20microservices&url=https://blog.sqreen.com/apidays-2019-rasp-for-apis-and-microservices/)[**Share](https://web.archive.org/web/20230526173527/https://www.linkedin.com/shareArticle?mini=true&url=https://blog.sqreen.com/apidays-2019-rasp-for-apis-and-microservices/)[**Share](https://web.archive.org/web/20230526173527/mailto:/?subject=APIdays%3A%20RASP%20for%20APIs%20and%20microservices&body=APIdays%3A%20RASP%20for%20APIs%20and%20microservices%20https://blog.sqreen.com/apidays-2019-rasp-for-apis-and-microservices/)[![](https://web.archive.org/web/20230526173527im_/https://secure.gravatar.com/avatar/630bcbf98d335080f59e77b73f55c510?s=120&d=mm&r=g)](https://web.archive.org/web/20230526173527/https://blog.sqreen.com/author/user-3/)
##### [Jb](https://web.archive.org/web/20230526173527/https://blog.sqreen.com/author/user-3/)
Jean-Baptiste Aviat spent half a decade hunting vulnerabilities at Apple, helping developers solve them, and developing security software. He is now CTO at Sqreen.

#### Get your bi-weekly security dose
Hand-picked security content for Developers, DevOps and Security. No Spam. Just awesome content.

##### Related Tags

- [API](https://web.archive.org/web/20230526173527/https://blog.sqreen.com/tag/api/),
- [microservices](https://web.archive.org/web/20230526173527/https://blog.sqreen.com/tag/microservices/),
- [RASP](https://web.archive.org/web/20230526173527/https://blog.sqreen.com/tag/rasp/)
**Subscribe**Notify ofnew follow-up commentsnew replies to my comments![guest](https://web.archive.org/web/20230526173527im_/https://secure.gravatar.com/avatar/?s=56&d=mm&r=g)Label{}[+]**Name***Email***Website![guest](https://web.archive.org/web/20230526173527im_/https://secure.gravatar.com/avatar/?s=56&d=mm&r=g)Label{}[+]**Name***Email***Website0Comments******Inline FeedbacksView all commentsLoad More Comments
