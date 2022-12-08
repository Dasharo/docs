# Documentation guidelines

That document can be treated as an onboarding into creating and maintaining
documentation in projects developed by Dasharo Team. It is a set of general
rules and tips that you should have in mind while writing guides to any projects
in Dasharo repositories.

## Table of content

- [General rules](#general-rules)
- [Document type](#document-type)
- [Useful tools](#useful-tools)
- [Formatting](#formatting)

## General rules

- **Make a plan** - before starting a new document, you should know how it will
look. It is good to prepare a table of content first, and then fill up planned
chapters.
- **Read twice before publish** - everyone make mistakes. Before committing
your changes, it is good to read this again and make sure that you do not make
any typos, a dump of commands output is correct, or there are no other mistakes.
- **Goal of document** - Documentation is not written for everyone. Some
documents contain only a list of commands with minor descriptions, some of them
were created to describe research results, and others may be written for
non-technical persons with a huge amount of data that are obvious and
unnecessary to read by developers. Because of that, you should always know for
who you are writing that document - it may be developers, testers, or
non-technical management.
- **Hierarchy of information** - most important information should always be
on top of the document. We should start with the title, short description, and
table of contexts. The rest of the chapters should start with the most important
one.
- **30/90 rule** - It is good to ask your reporter or someone else to do a quick
review where approx 30% of the work was done. At this moment, you probably have
prepared the initial draft of the document with a table of content and some
remarks about content in planned chapters. The second review should be done when
90%  of the work is finished, and the document is almost done. With that
workflow, you can make sure that you are on the same page with a reporter.
- **Existing resources** - We should not duplicate content that was previously
described in another document. Some steps or explanations are related to a few
documents, and it is not necessary to write the same again. It is good to use
references to existing documents (like hyperlinks) - because of that, updating
and maintenance of documentation are easier because the change in one document
is related to several others. Also, if you see that a related document is
outdated, it will be a much better choice to review and update them instead of
writing another new one from scratch.
- **Maintenance** - documentation may be outdated after a few changes. We should
keep that in mind and prepare an updated schedule. One of the ideas is to mark
related documents in every pull request with technical changes. Of course, the
best solution is to improve documentation with every change in
code/architecture, but it is not always possible due to deadlines or lack of
time. Marking documents to update in the future allows us to do that on better
occasions - and we prevent situations where the reader must inform us that the
documentation is highly outdated - or even useless.
- **Archive** - Projects are changing, and some topics from the past are not
existing now. If the document describes the working of a non-existing mechanism,
we should move it to the special folder with archived content. We can go back to
that solution in the future, but it must be moved out to as not to mislead the
reader.

## Document type

Good documentation should be written in one of four modes.
It can be a tutorial, how-to guide, technical reference, or explanation.
These modes were proposed by [Diataxis](https://diataxis.fr/) framework, and we
want to follow that method in the future. Generally:

- **Tutorials** are learning-oriented, and their purpose is to take the reader
_by the hand through a series of steps_ to complete a project of some kind. It
may be a getting started guide, end2end process, or preparing the working
environment.
- **How-to-guides** should be written as a _step list that is required to
solve the problem_. They are goal-oriented, which is the main difference between
tutorials: how-to guides lead to solving some problems and are not focused on
the learning experience. For example, building system images or modifying boot
parameters.
- **Reference** guides are technical descriptions, and it is
information-oriented. It is only information about some technical thing without
an explanation of it in the larger context. A good example of that is a
requirement list, description of functions or variables used in the program, or
list of supported platforms.
- **Explanation** is a discussion focused on the understanding of some topic,
like boot flow, description of specific communication protocol, or device
provisioning. That document should explain the subject, not instruct how to do
something.

We should not create documents that are not related to these modes.

## Useful tools

- [grammarly.com](grammarly.com) - online writing assistant who can improve
your grammar and make the document clear. A premium account is a very useful
option, but it is not a must. Core functionalities are available for free.
**It is highly recommended to use the Grammarly tool before committing
changes.**
- [hemingwayapp.com](hemingwayapp.com) - make your writing clear. Sometimes it
catches things that are not detected by Grammarly.
- [draw.io](draw.io) - we use that to prepare diagrams.
- [paste.dasharo.com](paste.dasharo.com) - pastebin alternative hosted by
Dasharo.
- [asciinema.org](https://asciinema.org) - free and open-source solution for
recording terminal sessions. Sometimes - especially in more complex cases, it
is good to present command sequences in this way.

## Formatting

General rules of formatting documents:

- Use markdown preview to verify that document is rendering correctly. That
feature is available in VS code, Github/Gitlab web IDE, and other tools.
- Line with code should not have more than 80 characters. To follow that rule,
it is good to set the line at width 80 in your IDE.
[Here](https://stackoverflow.com/a/52455857) is how to do it in VS code.

We also maintain the repository
[Dasharo/dev-tools-configs](https://github.com/Dasharo/dev-tools-configs/)
with editors configs used by our community. Feel free to create PR with your
configuration - you can give your proposition to improve existing settings or
create configs for editors that don't exist yet in our repository.
A properly configurated editor simplifies correct formatting.
