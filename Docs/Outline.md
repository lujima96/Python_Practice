Lucas's Python, ML, and AI Course
Updated: November 18, 2026
Starting point and direction
- IT and software development background, including APIs, SQL, Docker, reporting, and internal applications.
- Completed a frontend bootcamp with a Vite/React application and a backend bootcamp with a layered Java/Spring Boot application, including a business layer and API. Most Java coursework was completed unassisted; AI helped with frontend work during overtime and with production systems at work.
- Has not coded manually in a while and has limited Python experience. Explicitly wants the full ground-up Python experience, with computer science foundations, independent coding fluency, and interview preparation. Do not skip fundamentals based on previous bootcamps or production projects.
- Identifies problem decomposition as a strength, supported by teaching experience. Use familiar practical contexts while teaching implementation from the beginning.
- Self-assessed Python independence: needs help with most basics. Start at the beginning; do not infer independent Python proficiency from past projects.
- Original availability: 6–10 hours per week. Subsequently explored a pace of roughly 1.5 lesson-sized sessions daily (approximately 11–16 hours/week for 60–90 minute lessons). Adjust to actual sustainable practice; later projects may span several sessions.
- Interests: understand and build AI, machine learning, and deep learning projects, including designing and training models. LLM-powered applications are one interest within this broader goal. Do not steer the curriculum mainly toward integrating existing LLMs.
- Direction: full Python and CS foundations leading to classical ML, mathematical understanding, implementing small learning algorithms, and designing, training, evaluating, and deploying neural networks. Explore job targets after hands-on work across these areas.
- Learning format: from Lesson 4 onward, use engaging RPG-style missions, meaningful progression, XP, and a capstone/boss challenge where appropriate. Keep technical explanations clear, define concepts explicitly, and use substantive tasks rather than decorative fantasy labels. Hints do not cost XP; pace and cosmetic scoring do not override learning.
- Development setup: Pop!_OS, Python installed, VS Code.
- Unknowns to resolve: math comfort, budget, and eventual target jobs. Avoid paid requirements until discussed.
Learning method
Design one lesson and practice assignment at a time. Explain unfamiliar terms, show a small example, then assign a different problem. Review submitted work before moving on. Use hints before full solutions. A topic can move quickly once the learner can explain it, implement it, and adapt it to a new example.

Keep complete coverage of Python fundamentals. Pair syntax with explanations of execution, data representation, and reasoning. Build independent implementation gradually, using documentation when needed and an initial self-written attempt for practice. Give meaningful corrections without making every minor style issue or additional exercise a prerequisite for progression; respect the learner's decision to move on.

As lessons progress, include a small computer science connection, a coding exercise with gradually less scaffolding, and a short interview-style explanation or debugging prompt. Begin with untimed practice. Add timed mock interviews after the relevant skills are established. Explain new terms when introduced.

Use two learning sessions of roughly 90 minutes, one independent practice session of roughly two hours, and one review session of roughly one hour each week. Additional available time goes to practice and project improvements. Lessons may span multiple sessions. A week is a planning unit, not a deadline.

Use initial independent attempts for foundational checkpoints; later teach effective AI-assisted development and verification as an explicit skill.
Curriculum outline
Stage	Topics	Checkpoint
0. Setup and orientation	Interpreter, editor, terminal, scripts, errors; later virtual environments and packages	Run a saved Python script and explain its output
1. Python fundamentals	Variables, assignment, numbers, strings, booleans, input, conversion, conditionals, loops	Build a small inventory or cost calculator independently
2. Functions and collections	Functions, parameters, return, scope, lists, dictionaries, tuples, sets, iteration, mutability, comprehensions; references, call stack, choosing data structures	Process records using reusable functions and explain the choice of structures
3. Practical Python	Files, CSV, JSON, exceptions, modules, HTTP APIs, environment variables, tests, debugging, logging, type hints, classes as needed	Build a reliable data-processing tool; then try a small model-backed application
4. Data skills	SQL refresh, NumPy, pandas, joins, missing data, duplicates, dates, plotting, exploratory analysis	Produce a reproducible analysis from messy data
5. Applied math and statistics	Algebra, functions, vectors, matrices, probability, distributions, sampling, uncertainty, derivatives, gradient descent	Explain and implement the calculations behind a simple model
6. Classical ML	Problem framing, baselines, regression, classification, trees, ensembles, preprocessing, feature engineering, train/validation/test splits, cross-validation, metrics, leakage, tuning; introductory clustering and time-aware evaluation; implement small regression/optimization algorithms	Train and evaluate models honestly on unseen data; explain their calculations and errors
7. Deep learning and model training	Small neural networks implemented with NumPy; forward passes, gradients and backpropagation; PyTorch tensors, automatic differentiation, datasets, batches, custom networks, losses, optimizers, training/validation loops, regularization, CNNs and model debugging	Implement a small educational network; then design, train, evaluate, and save a PyTorch model from initialized weights
8. Modern AI and extensions	Sequence modeling, embeddings, attention and transformer concepts; small text-model experiments and pretrained-model adaptation; model APIs, structured outputs, retrieval/RAG, tool use, evaluation, privacy, latency and cost	Build an additional text or AI-system project and explain the modeling or integration decisions
9. Production systems	API serving, containers, deployment, automated checks, experiment tracking, data/model versions, monitoring, drift, access control	Deploy and troubleshoot a reproducible ML or AI application
10. Hiring preparation	Consolidate ongoing Python/SQL and algorithm practice; ML reasoning, basic system design, project explanations, behavioral examples, mock interviews, resume alignment, reviewing actual job requirements	Demonstrate project ownership and skills for selected roles


Math is introduced where it becomes useful, with focused lessons when needed. Stages overlap: testing starts with small functions; documentation and project communication start early; deployment begins with a small application before the production stage.
Computer science, fluency, and interview practice
These threads run throughout the Python-to-AI curriculum. Include focused lessons when a concept needs more room; do not assume the table is one lesson per row.
When	Computer science focus	Fluency and interview practice
Variables and expressions	Types, values, names/references, evaluation order, changing program state	Trace short programs, explain reassignment, repair type errors
Conditions	Boolean logic, execution paths, priority, boundary cases	Explain why a branch runs; choose tests below, at, and above a cutoff
Loops	Iteration, accumulators, termination, off-by-one errors	Implement counting, totals, filtering, and repeated input; trace changing state
Collections	Lists as dynamic arrays; dictionaries and sets as hash-based structures; tradeoffs for lookup, ordering, and duplicates	Choose structures for records, deduplication, counting, and grouping
Functions	Decomposition, inputs/outputs, scope, call stack, references, mutation, side effects	Turn requirements into small functions; compare return values with printing; test edge cases
After loops, functions, and collections	Time and space complexity (Big O), linear and binary search, sorting principles, introductory recursion	Explain how work and memory grow; practice simple algorithm problems and improve a first solution
Further data structure practice	Stacks, queues, basic linked-list concepts, trees and graphs; introduce Python tools as needed	Trace and implement representative operations; use basic traversal/search exercises appropriate to selected roles
Practical applications	Modules, abstraction, object-oriented design, composition, error handling, tests, databases, HTTP, concurrency basics as relevant	Read and modify unfamiliar code; debug failures; explain design tradeoffs; practice SQL joins and aggregation
ML and AI projects	Data pipelines, evaluation, generalization, service boundaries, reliability, latency and cost	Defend model/metric choices; explain project architecture and failures; practice relevant system design


For interview problems, build the habit of clarifying requirements, working through examples, describing a plan, implementing it, testing boundaries, and explaining complexity when that concept has been taught. Practice communicating technical decisions and drawing behavioral examples from teaching, IT support, and production development. Scope later algorithm depth to actual target roles, while retaining the fundamentals.
Model-building milestones
1. Implement a small regression model and gradient descent using basic numerical code, then NumPy. Connect the code to loss functions, derivatives, vectors, and matrices.
2. Implement a small educational neural network with a forward pass and backward gradient calculations. Use simple datasets, explain the calculations, and check whether learning behaves as expected.
3. Design a PyTorch network, train it from initialized weights, and understand automatic differentiation, batches, losses, optimizers, and training/validation loops.
4. Train a practical neural classifier, such as an image classifier with a small convolutional network. Compare a baseline, inspect mistakes, diagnose overfitting, and report held-out performance.
5. Explore a sequence/text or small transformer project after the prerequisites. Choose the depth based on interest, hardware, and budget; large foundation-model pretraining is not a required milestone.
An early application calling an existing model can remain an optional motivational project after practical Python. It supplements model-building work. The core progression includes actual training, mathematical understanding, evaluation, and debugging across classical ML and deep learning.
First four weeks: provisional
1. Setup, assignment, numbers, strings, print, and reading basic errors.
2. Input and conversion, booleans, comparisons, conditionals.
3. Loops and lists, tracing execution, debugging.
4. Functions and a small inventory or cost-calculation project.
Adjust after submitted work; add sessions for dictionaries and files as needed before later projects. Do not skip basics to meet this schedule. Estimate the broader timeline after several weeks of observed practice.
Portfolio direction
Develop two substantial trained-model projects from smaller exercises, using public or synthetic data:
1. Predictive ML: cost or demand prediction, a simple baseline, time-appropriate evaluation, error analysis, and a deployed interface.
2. Deep learning: design and train a neural model, document the architecture and training choices, inspect learning curves and failure cases, compare an appropriate baseline, and deploy an inference interface.
Keep small implementations of learning algorithms and educational neural networks as evidence of understanding. A document/support assistant or other model-integrated application can be an additional project if useful; it does not replace the trained-model portfolio work.

Job-readiness checks: independently scope and implement a project; use SQL and prepare data; choose a sensible baseline; evaluate with appropriate metrics and splits; explain limitations; test, deploy, and debug the application; discuss engineering decisions; handle relevant interview exercises. Reassess against actual selected job descriptions before applying.
Lesson 1: execution, values, variables, and output
Status: submitted and reviewed; moved forward at the learner's request. Core concepts demonstrated; case-sensitive variable fix and a change-and-rerun check were discussed.

Suggested time: 30–60 minutes. Work through the examples and attempt the exercises without generated solutions. An incomplete attempt is useful evidence for feedback.

Goal: read a short program, explain each assignment, and write a small calculation with named values.
1. Programs execute instructions
For these straight-line examples, Python executes one statement at a time from top to bottom. The interpreter is the program that executes Python code.
print("Inventory check")
print(12)
print(...) displays a value. Text enclosed in quotes is a string. 12 without quotes is an integer, a whole-number value. Parentheses contain what you pass to print. Put each statement on its own line.
2. Names refer to values
item_name = "Label roll"
quantity = 12

print(item_name)
print(quantity)
= performs assignment: Python evaluates the right side, then binds the name on the left to the result. Here item_name refers to a string and quantity refers to an integer. Assignment does not ask whether two things are equal. Use descriptive names, and underscores to separate words. A name cannot contain spaces or start with a digit.

print("quantity") displays the literal text quantity. print(quantity) looks up the value associated with the name quantity. Variable names are case-sensitive: quantity and Quantity are different names.
3. Calculate and reassign
boxes = 3
labels_per_box = 100
total_labels = boxes * labels_per_box

print("Total labels:", total_labels)
* multiplies. + adds, - subtracts, and / divides numeric values. print can receive multiple values separated by commas; here it displays the label and the calculated number with a space between them.

Assignment stores the result calculated at that moment. Changing boxes later does not automatically recalculate total_labels. You must execute the calculation again to update that value.
Practice A: predict before running
Write the two output values, then explain your reasoning:
quantity = 8
total = quantity * 3
quantity = 10

print(quantity)
print(total)
Practice B: write your own code
A storeroom has 6 boxes with 24 label rolls per box, and 17 individual rolls are used. Define boxes, rolls_per_box, and rolls_used. Calculate starting_rolls and remaining_rolls from those variables. Print both results with readable labels. Use calculations rather than typing the final answers directly into print.
Practice C: explain the difference
Explain what each line prints and why:
print("remaining_rolls")
print(remaining_rolls)
For the second line, assume your Practice B code has already run.
Reply format
Send your Practice A predictions, Practice B code, and Practice C explanation. Include your computer's OS and whether Python and a code editor are installed so setup can be adapted to your environment. If setup is not ready, you can write code and predict output here without running it.
Progress record
Item	Status	Evidence / next step
Learning preferences	Established	Full ground-up Python; CS, fluency, and interview practice throughout; design/train/evaluate ML and deep learning models; RPG-style lessons
Development setup	Established	Pop!_OS; Python installed; VS Code
Lesson 1	Reviewed; moved forward	Correct assignment/arithmetic explanations and delivery logic; capitalization correction discussed
Lesson 2	Complete; reviewed	Correct independent exercises; understood input conversion, f-strings, string methods, and self-corrected a reassignment prediction; guided prompt-vs-response strip placement corrected
Lesson 3	Complete; reviewed	Correct core Boolean/branching logic; inventory status/calculation gating verified in 10 cases and prompt decisions at boundaries; discussed validation output, direct Boolean assignment, redundant checks, type-comparison comments, and preserving prompt case
Lesson 4	Assigned	RPG loop missions: for/range, counters, accumulators, continue, while, break, termination, invariants, and a deterministic combat game; optional scalar optimization experiment
Math starting point	Unknown	Assess before math-dependent material


Reference foundations
- Google ML prerequisites: https://developers.google.com/machine-learning/crash-course/prereqs-and-prework
- scikit-learn common pitfalls: https://scikit-learn.org/stable/common_pitfalls.html
- Hugging Face LLM course: https://huggingface.co/learn/llm-course/chapter1/1
These are reference materials for lesson design, not extra courses assigned to the learner.