# HelloActions-DestinyJordan
# Testing automatic execution

# Explain the Workflow
29. What is the purpose of the on section? It defines the events that trigger the workflow.
30. What does workflow_dispatch do? Allows for immediate manual on-demand execution (manual runs).
31. What does runs-on specify? It specifies a fresh virtual host machine for the job.
32. Why is actions/checkout needed? It is needed because since the runners start out empty, it copies the repository's files onto it.
33. What does the language setup action do? It installs a specific version of a language.
34. What is the difference between compiling and running the program? Compiling translates source code into something the computer can execute. Running executes the program.
35. Where can you see the program output? You can see the program output in the actions tab, under the workflow run, under the job's steps.
36. What is the difference between a workflow, a job, and a step? A workflow is the automated process in the .yml file, a job is the steps that run together in a runner, and a step is a single task inside a job.
