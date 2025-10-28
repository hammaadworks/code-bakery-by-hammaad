1. ask your agent to read the @data/kb to know the bmad workflow to 
guide you out when stuck in a workflow

2. sometimes the agents don't doc-out you need to check it or else you'll have a nice convo and clear the context. hahahahah

3. Major: store in the memory of AGENTS.md to use `read-modify-write` strategy or else it'll just overwrite and
by chance you are gitignoring it then, tata bye bye
[RMW Gotcha](assets/bmad_rmw_gotcha.mov)

4. commit the .bmad directory if you wanna work in jules to delegate some implementations

5. Maintain an archived sprints directory to keep track of the previous sprints and their context.
[Archived Sprints](assets/archived_sprints.png)

6. Overall it is just
analyst -> brief.md
pm -> prd.md
ux -> front_end_spec.md
architect -> architecture.md
po -> checklist
po -> shard the prd and architecture
--- loop
sm -> create draft
qa -> risk, design
dev -> implement
qa -> trace, review
---

7. Please always verify all changes after any agent, completes a step be it story, code, review, etc. You are just a human in the loop and AI is still needs your supervision, you might want to do some silly tweaks such as downloading a new library or tweaking some design/document changes, just small changes here in there, which AI might have missed and might save you circles and hours of debugging, especially designed docs and minor code/devops tweaks.

8. Especially while working with cli or tui, I strongly recommend you make a git ignored file where you maintain a chat history easier to copy paste, edit, all while using TTS. cause sometimes the cli might not be responsive and you might miss a track of necessary chats you had in the session. Useful when you generally are dealing with a repeatable sequence.

9. Story creation and development might not be in a sequential order. Sometimes while course correcting, you might not execute stories in same order, rather, you might want to execute a new story out of the order to facilitated changes and meet requirements of previous stories, and then come back to execute the previous ones. That's why we highly recommend to use `sm` for `next-story` creation and go incremental story wise.